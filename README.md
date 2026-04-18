# AI Personal Assistant Team

A multi-channel AI personal assistant system built on Claude Code. Deploy your own team of 15 specialized agents that manage different areas of your life through Telegram.

## What Is This?

A "clone and configure" template for a personal AI assistant that:
- Operates through **5 Telegram channels** (topics in one group), each with a dedicated Account Manager
- Has a **team of 10 specialist agents** (Analyst, Strategist, Writer, Critic, Input Guard, Security Scanner, etc.) that work behind the scenes
- Maintains a **self-learning brain** with tiered memory loading that grows smarter with every interaction
- Supports **27 slash commands** including core skills (/brief, /analyze, /strategize, /draft, /challenge, /research, /ingest, /onboard, /learn, /status, /decide, /digest) and execution skills (/weekly-review, /meeting-prep, /followup, /triage, /premortem, /report, /reflect, /repurpose, /prioritize, /okr, /delegate, /extract-wisdom, /negotiate, /postmortem, /coach)
- Includes **security features**: Input Guard screens messages for prompt injection, Security Scanner audits agent files via Caterpillar

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
- **Self-learning brain** — auto-captures decisions, preferences, patterns with tiered memory loading (hot/warm/cold)
- **Security hardening** — Input Guard screens for injection attacks, audit log tracks agent actions
- **Resource ingestion** — feed it documents and it extracts knowledge
- **Weekly check-ins** — the system asks you questions to improve itself
- **Graceful degradation** — works with reduced features if integrations are missing

## Obsidian Integration

Your brain folder works as an [Obsidian](https://obsidian.md) vault out of the box. Open it to get:
- **Graph view** showing how all your knowledge connects
- **Visual editing** of any brain file
- **Dynamic dashboards** via Dataview plugin
- **Mobile access** to your brain

The setup wizard handles Obsidian configuration automatically.

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
