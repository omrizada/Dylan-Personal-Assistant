# Architecture

## System Overview

```
                         ┌──────────────────────┐
                         │      Telegram         │
                         │   Forum Group         │
                         └──────┬───────────────┘
                                │
              ┌─────────────────┼─────────────────────┐
              │                 │                       │
        ┌─────┴────┐    ┌─────┴──────┐         ┌─────┴────┐
        │  Work    │    │Side Project│   ...    │  Dev     │
        │  Topic   │    │  Topic     │         │  Topic   │
        └─────┬────┘    └─────┬──────┘         └─────┬────┘
              │                │                       │
        ┌─────┴────┐    ┌─────┴──────┐         ┌─────┴────┐
        │  Work    │    │Side Project│         │  Dev     │
        │  AM      │    │  AM        │         │  AM      │
        └─────┬────┘    └─────┬──────┘         └─────┬────┘
              │                │                       │
              └────────────────┼───────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │   Chief of Staff    │
                    │   (Orchestrator)    │
                    └──────────┬──────────┘
                               │
          ┌────────┬───────┬───┴───┬────────┬──────────┐
          │        │       │       │        │          │
       ┌──┴──┐ ┌──┴──┐ ┌──┴──┐ ┌──┴──┐ ┌──┴──┐  ┌───┴────┐
       │Anal-│ │Stra-│ │Writ-│ │Crit-│ │Mkt  │  │Library │
       │yst  │ │tgst │ │er   │ │ic   │ │Rsrch│  │& more  │
       └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘  └───┬────┘
          │        │       │       │        │          │
          └────────┴───────┴───┬───┴────────┴──────────┘
                               │
                    ┌──────────┴──────────┐
                    │       Brain         │
                    │  (Markdown Files)   │
                    └─────────────────────┘
```

## Communication Flow

1. **You** send a message in a Telegram topic (e.g., the "Work" topic)
2. The **Account Manager** for that channel receives the message. Each AM has a distinct personality and context loaded from `channels/<name>/context.md`
3. The AM decides whether to handle it directly or escalate to the **Chief of Staff**
4. The Chief of Staff **routes** the request to the appropriate specialist agent(s)
5. Specialist agents read from the **Brain** (markdown files) for context
6. The response flows back through the AM, which adapts tone for the channel
7. The **Librarian** evaluates whether the interaction should update the Brain

## Directory Structure

```
personal-assistant-template/
├── CLAUDE.md                  # Main system prompt (Claude Code reads this)
├── README.md                  # This file
├── SETUP.md                   # Setup instructions
├── ARCHITECTURE.md            # You are here
├── CHANNELS.md                # Channel customization guide
├── ADAPTING.md                # Platform adaptation guide
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT license
├── config.example.md          # Variable reference
│
├── agents/                    # Agent definitions (system prompts)
│   ├── chief-of-staff.md      # Orchestrator agent
│   ├── analyst.md             # Deep analysis agent
│   ├── strategist.md          # Strategic planning agent
│   ├── writer.md              # Document creation agent
│   ├── critic.md              # Devil's advocate agent
│   ├── market-researcher.md   # External research agent
│   ├── onboarding-coach.md    # Brain population agent
│   └── librarian.md           # Knowledge management agent
│
├── skills/                    # Slash command definitions
│   ├── brief.md               # /brief — morning briefing
│   ├── analyze.md             # /analyze — deep analysis
│   ├── strategize.md          # /strategize — strategic session
│   ├── draft.md               # /draft — document creation
│   ├── challenge.md           # /challenge — devil's advocate
│   ├── research.md            # /research — market research
│   ├── ingest.md              # /ingest — resource processing
│   ├── onboard.md             # /onboard — brain onboarding
│   └── learn.md               # /learn — manual teaching
│
├── channels/                  # Channel configurations
│   ├── work/
│   │   └── context.md         # Work channel AM personality + context
│   ├── side-project/
│   │   └── context.md         # Side project channel
│   ├── personal/
│   │   └── context.md         # Personal channel
│   ├── general/
│   │   └── context.md         # General channel
│   └── development/
│       └── context.md         # Development channel
│
├── brain/                     # Self-learning knowledge base
│   ├── BRAIN_INDEX.md         # Master index of all brain files
│   ├── context/               # Who you are and what you're doing
│   │   ├── role-and-goals.md
│   │   ├── projects.md
│   │   ├── stakeholders.md
│   │   ├── decisions-log.md
│   │   └── terminology.md
│   ├── preferences/           # How you like things done
│   │   ├── communication.md
│   │   ├── analysis-style.md
│   │   ├── document-style.md
│   │   └── priorities.md
│   ├── learnings/             # Patterns from interactions
│   │   ├── patterns.md
│   │   ├── feedback.md
│   │   └── strategies.md
│   ├── channels/              # Per-channel brain context
│   │   ├── work/
│   │   ├── side-project/
│   │   ├── personal/
│   │   ├── general/
│   │   └── development/
│   └── resources/             # Digested external resources
│       ├── summaries/
│       └── insights/
│
├── resources/                 # Raw input files (never committed)
│
├── output/                    # Generated deliverables
│   ├── documents/
│   ├── analyses/
│   └── strategies/
│
└── scripts/
    └── setup.sh               # Interactive setup script
```

## The Brain

The brain is a collection of markdown files that serve as the assistant's long-term memory. It has four layers:

### Context Layer (`brain/context/`)
Who you are and what you are working on. Contains your role, active projects, key people, past decisions, and domain terminology. This is the factual foundation.

### Preferences Layer (`brain/preferences/`)
How you like things done. Communication tone, analysis frameworks, document formatting, and priority weights. These shape every response.

### Learnings Layer (`brain/learnings/`)
Patterns discovered through interactions. What worked, what didn't, corrections you gave, and strategies that proved effective. This is how the system improves over time.

### Resources Layer (`brain/resources/`)
Digested knowledge from documents you feed the system via `/ingest`. Summaries of each resource plus cross-cutting insights that connect ideas across resources.

### Channel Brain (`brain/channels/`)
Per-channel context that lets each Account Manager maintain specialized knowledge. The Work channel brain knows about your job; the Side Project brain knows about your startup.

### How the Brain Grows

The brain grows through three mechanisms:

1. **Onboarding** (`/onboard`): Interactive Q&A session that populates the initial brain files
2. **Auto-learning**: After significant interactions, the Librarian evaluates whether to update brain files. Learnings files are updated automatically; context and preference files require your confirmation.
3. **Manual teaching** (`/learn`): You can directly tell the system something new

### Brain Rules

- Brain files never exceed 500 lines. If a file grows too large, the Librarian splits it.
- Context and preference updates are proposed to you before being written.
- Learning updates (patterns, feedback, strategies) are written automatically.
- The `BRAIN_INDEX.md` is always kept up to date with last-modified dates.
- Brain files are gitignored by default (they contain personal data).

## Agent Team

### Account Managers (5)

Each Telegram topic maps to an Account Manager. The AM is the user-facing personality layer. It:
- Receives messages from the user
- Loads channel-specific context from `channels/<name>/context.md` and `brain/channels/<name>/`
- Handles simple requests directly
- Escalates complex requests to the Chief of Staff
- Adapts the response tone to match the channel personality

### Specialist Agents (8)

| Agent | Expertise | Typical Triggers |
|-------|-----------|-----------------|
| Chief of Staff | Orchestration, routing, multi-agent coordination | Complex/ambiguous requests, briefings |
| Analyst | Data analysis, pattern recognition, frameworks | "analyze", "break down", metrics |
| Strategist | Planning, decision frameworks, roadmaps | "strategy", "prioritize", tradeoffs |
| Writer | Document creation, editing, tone adaptation | "write", "draft", "edit" |
| Critic | Devil's advocate, risk assessment, blind spots | "challenge", "what am I missing" |
| Market Researcher | External research, competitive intelligence | "research", "competitors", "benchmark" |
| Onboarding Coach | Brain population, preference gathering | `/onboard`, weekly check-ins |
| Librarian | Knowledge management, resource processing | `/ingest`, brain maintenance |

### Multi-Agent Workflows

Some requests trigger multiple agents in sequence:

- **Analyze then Strategize**: Analyst breaks down the situation, Strategist develops the plan
- **Research then Analyze**: Market Researcher gathers data, Analyst synthesizes it
- **Strategize then Critique**: Strategist proposes, Critic stress-tests
- **Write then Review**: Writer drafts, Critic reviews for gaps

## Slash Commands

| Command | Agent | Purpose |
|---------|-------|---------|
| `/brief` | Chief of Staff | Morning briefing with current state and pending decisions |
| `/analyze` | Analyst | Deep structured analysis of a topic or resource |
| `/strategize` | Strategist | Strategic thinking session with frameworks |
| `/draft` | Writer | Create a document matching your style preferences |
| `/challenge` | Critic | Devil's advocate session to stress-test thinking |
| `/research` | Market Researcher | Web research on competitors, markets, trends |
| `/ingest` | Librarian | Process a document into the brain |
| `/onboard` | Onboarding Coach | Populate the brain through interactive Q&A |
| `/learn` | Librarian | Manually teach the system something new |

## Auto-Learning System

After every significant interaction, the Librarian evaluates whether brain files should be updated:

| Signal | Brain File Updated |
|--------|--------------------|
| New person mentioned with role | `brain/context/stakeholders.md` |
| New term or jargon used | `brain/context/terminology.md` |
| Project status changed | `brain/context/projects.md` |
| Decision made with rationale | `brain/context/decisions-log.md` |
| User corrected the system | `brain/learnings/feedback.md` |
| Preference expressed | `brain/preferences/` (with confirmation) |
| Strategy worked or failed | `brain/learnings/strategies.md` |
| Recurring pattern observed | `brain/learnings/patterns.md` |

## Graceful Degradation

The system works at different capability levels depending on available integrations:

| Integration | What It Enables | Without It |
|-------------|----------------|------------|
| Telegram plugin | Multi-channel messaging | Use directly in Claude Code terminal |
| WebSearch | Market research, current data | Research agent limited to brain knowledge |
| WebFetch | URL content retrieval | Cannot fetch external pages |
| CronCreate | Scheduled briefings, reminders | Manual-only triggering |
| MCP tools (Calendar, Email, etc.) | Direct integrations | Copy-paste workflow |

The core value -- the brain, agents, and slash commands -- works with Claude Code alone, no plugins required.
