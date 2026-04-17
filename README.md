# AI Personal Assistant Team

A multi-channel AI personal assistant system built on Claude Code. Deploy your own team of 13 specialized agents that manage different areas of your life through Telegram.

## What Is This?

A "clone and configure" template for a personal AI assistant that:
- Operates through **5 Telegram channels** (topics in one group), each with a dedicated Account Manager
- Has a **team of 8 specialist agents** (Analyst, Strategist, Writer, Critic, etc.) that work behind the scenes
- Maintains a **self-learning brain** of markdown files that grows smarter with every interaction
- Supports **9 slash commands** (/brief, /analyze, /strategize, /draft, /challenge, /research, /ingest, /onboard, /learn)

## How It Works

```
You (Telegram) → Account Manager → Chief of Staff → Team Agents
                                                   → Response back to you
```

Each channel has its own Account Manager with a distinct personality:
- **Work** — Strategic, professional (your primary job)
- **Side Project** — Startup-hustle, action-oriented (your side hustle)
- **Personal** — Warm, casual (calendar, reminders, life admin)
- **General** — Friendly, quick (off-topic questions)
- **Development** — Technical, concise (system bugs and features)

## Features

- **Multi-channel routing** via Telegram Forum topics
- **Account Manager layer** — you never talk to the team directly
- **Self-learning brain** — auto-captures decisions, preferences, patterns
- **Resource ingestion** — feed it documents and it extracts knowledge
- **Weekly check-ins** — the system asks you questions to improve itself
- **Graceful degradation** — works with reduced features if integrations are missing

## Quick Start

1. **Prerequisites**: [Claude Code](https://claude.ai/code) installed
2. **Clone**: `git clone https://github.com/YOUR_USERNAME/personal-assistant-template.git`
3. **Configure**: `cd personal-assistant-template && bash scripts/setup.sh`
4. **Launch**: `claude --channels plugin:telegram@claude-plugins-official`
5. **Onboard**: Send `/onboard` in any channel to teach the system about you

See [SETUP.md](SETUP.md) for detailed instructions.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design.

## Customizing Channels

See [CHANNELS.md](CHANNELS.md) for how to add, remove, or customize channels.

## Adapting for Other Platforms

While designed for Claude Code, the agent definitions and brain system can be adapted for other platforms. See [ADAPTING.md](ADAPTING.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE)
