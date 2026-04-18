#!/usr/bin/env python3
"""Dylan Setup Wizard - Local web server for guided setup."""

import http.server
import json
import subprocess
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

PROJECT_DIR = Path(__file__).parent.parent.resolve()
STATIC_DIR = Path(__file__).parent / "static"
PORT = 3456


class WizardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length)) if content_length else {}

        if path == '/api/check-deps':
            result = self._check_dependencies()
        elif path == '/api/apply-config':
            result = self._apply_configuration(body)
        elif path == '/api/run-command':
            result = self._run_command(body)
        else:
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def _check_dependencies(self):
        checks = {}
        dep_commands = [
            ('claude', 'which claude'),
            ('python', 'which python3'),
            ('obsidian', 'test -d /Applications/Obsidian.app && echo found'),
            ('gh', 'which gh'),
        ]
        for name, cmd in dep_commands:
            try:
                r = subprocess.run(
                    cmd, shell=True, capture_output=True, text=True, timeout=5
                )
                checks[name] = r.returncode == 0
            except Exception:
                checks[name] = False
        return checks

    def _apply_configuration(self, config):
        results = []
        replacements = {
            '{{USER_NAME}}': config.get('fullName', ''),
            '{{USER_FIRST_NAME}}': config.get('firstName', ''),
            '{{BOT_USERNAME}}': config.get('botUsername', '{{BOT_USERNAME}}'),
            '{{TELEGRAM_GROUP_ID}}': config.get('groupId', '{{TELEGRAM_GROUP_ID}}'),
            '{{TELEGRAM_USER_ID}}': config.get('userId', '{{TELEGRAM_USER_ID}}'),
            '{{PROJECT_DIR}}': str(PROJECT_DIR),
            '{{SIDE_PROJECT_REPO_PATH}}': config.get(
                'sideProjectPath', '{{SIDE_PROJECT_REPO_PATH}}'
            ),
        }

        for ext in ['*.md', '*.json']:
            for filepath in PROJECT_DIR.rglob(ext):
                if '.git' in filepath.parts or '.obsidian' in filepath.parts:
                    continue
                if STATIC_DIR in filepath.parents or filepath == STATIC_DIR:
                    continue
                try:
                    content = filepath.read_text(encoding='utf-8')
                    original = content
                    for search, replace in replacements.items():
                        if replace and replace != search:
                            content = content.replace(search, replace)
                    if content != original:
                        filepath.write_text(content, encoding='utf-8')
                        results.append({
                            'file': str(filepath.relative_to(PROJECT_DIR)),
                            'status': 'updated',
                        })
                except Exception as e:
                    results.append({
                        'file': str(filepath.relative_to(PROJECT_DIR)),
                        'status': 'error',
                        'error': str(e),
                    })

        bot_token = config.get('botToken', '')
        if bot_token:
            token_dir = Path.home() / '.claude' / 'channels' / 'telegram'
            token_dir.mkdir(parents=True, exist_ok=True)
            (token_dir / '.env').write_text(
                f'TELEGRAM_BOT_TOKEN={bot_token}\n'
            )
            results.append({
                'file': '~/.claude/channels/telegram/.env',
                'status': 'updated',
            })

            user_id = config.get('userId', '')
            group_id = config.get('groupId', '')
            access = {
                'dmPolicy': 'pairing',
                'allowFrom': [user_id] if user_id else [],
                'groups': {},
                'pending': {},
            }
            if group_id:
                access['groups'][group_id] = {
                    'requireMention': False,
                    'allowFrom': [user_id] if user_id else [],
                }
            (token_dir / 'access.json').write_text(
                json.dumps(access, indent=2) + '\n'
            )
            results.append({
                'file': '~/.claude/channels/telegram/access.json',
                'status': 'updated',
            })

        return {'results': results, 'total': len(results)}

    def _run_command(self, body):
        cmd = body.get('command', '')
        allowed_prefixes = ['which ', 'claude ', 'brew ', 'open ', 'obsidian']
        if not any(cmd.startswith(p) for p in allowed_prefixes):
            return {'success': False, 'error': 'Command not allowed'}
        try:
            r = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=30
            )
            return {
                'success': r.returncode == 0,
                'stdout': r.stdout,
                'stderr': r.stderr,
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    print(f"\n  \U0001f415 Dylan Setup Wizard")
    print(f"  Open http://localhost:{PORT} in your browser\n")
    server = http.server.HTTPServer(('localhost', PORT), WizardHandler)
    try:
        import webbrowser
        webbrowser.open(f'http://localhost:{PORT}')
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Wizard stopped.")
        server.server_close()
