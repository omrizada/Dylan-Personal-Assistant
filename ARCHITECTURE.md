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
2. The **Input Guard** screens the message for prompt injection, credential extraction, and social engineering
3. The **Account Manager** for that channel receives the message. Each AM has a distinct personality and context loaded from `channels/<name>/context.md`
4. The AM decides whether to handle it directly or escalate to the **Chief of Staff**
4. The Chief of Staff **routes** the request to the appropriate specialist agent(s)
5. Specialist agents read from the **Brain** (markdown files) for context
6. The response flows back through the AM, which adapts tone for the channel
7. The **Librarian** evaluates whether the interaction should update the Brain

## Directory Structure

```
personal-assistant-template/
├── CLAUDE.md                  # Main system prompt — compressed (~150 lines)
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
│   ├── AGENT_INDEX.md         # Compact routing table (AMs + specialists)
│   ├── chief-of-staff.md      # Orchestrator agent
│   ├── analyst.md             # Deep analysis agent
│   ├── strategist.md          # Strategic planning agent
│   ├── writer.md              # Document creation agent
│   ├── critic.md              # Devil's advocate agent
│   ├── market-researcher.md   # External research agent
│   ├── onboarding-coach.md    # Brain population agent
│   ├── librarian.md           # Knowledge management agent
│   ├── security-scanner.md    # Automated security scanning agent
│   ├── input-guard.md         # Message screening agent (prompt injection defense)
│   └── account-managers/
│       ├── _am-base.md        # Shared AM behavior (all AMs reference this)
│       ├── work-am.md         # Work channel AM
│       ├── side-project-am.md # Side project channel AM
│       ├── personal-am.md     # Personal channel AM
│       ├── general-am.md      # General channel AM
│       └── dev-am.md          # Development channel AM
│
├── skills/                    # Slash command definitions
│   ├── _skill-pattern.md      # Shared skill structure template
│   ├── do.md                  # /do — universal command router
│   ├── brief.md               # /brief — morning briefing
│   ├── analyze.md             # /analyze — deep analysis
│   ├── strategize.md          # /strategize — strategic session
│   ├── draft.md               # /draft — document creation
│   ├── challenge.md           # /challenge — devil's advocate
│   ├── research.md            # /research — market research
│   ├── ingest.md              # /ingest — resource processing
│   ├── onboard.md             # /onboard — brain onboarding
│   ├── learn.md               # /learn — manual teaching
│   ├── status.md              # /status — system health check
│   ├── decide.md              # /decide — decision framework
│   ├── digest.md              # /digest — weekly digest
│   ├── weekly-review.md       # /weekly-review — end-of-week retrospective
│   ├── meeting-prep.md        # /meeting-prep — pre-meeting briefing
│   ├── followup.md            # /followup — commitment tracking
│   ├── triage.md              # /triage — email triage
│   ├── premortem.md           # /premortem — failure analysis
│   ├── report.md              # /report — audience-tailored status reports
│   ├── reflect.md             # /reflect — guided reflection
│   ├── repurpose.md           # /repurpose — content repurposing
│   ├── prioritize.md          # /prioritize — multi-framework prioritization
│   ├── okr.md                 # /okr — OKR tracking
│   ├── delegate.md            # /delegate — delegation tracking
│   ├── extract-wisdom.md      # /extract-wisdom — content extraction
│   ├── negotiate.md           # /negotiate — negotiation prep
│   ├── postmortem.md          # /postmortem — after-action review
│   └── coach.md               # /coach — leadership coaching
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
│   ├── LOADING_PROTOCOL.md    # Tiered loading rules (hot/warm/cold)
│   ├── frameworks.md          # Shared analytical/strategic/coaching frameworks
│   ├── context/               # Who you are and what you're doing
│   │   ├── role-and-goals.md
│   │   ├── projects.md
│   │   ├── stakeholders.md
│   │   ├── decisions-log.md
│   │   ├── terminology.md
│   │   ├── followups.md
│   │   └── okrs.md
│   ├── preferences/           # How you like things done
│   │   ├── communication.md
│   │   ├── analysis-style.md
│   │   ├── document-style.md
│   │   └── priorities.md
│   ├── learnings/             # Patterns from interactions
│   │   ├── patterns.md
│   │   ├── feedback.md
│   │   ├── strategies.md
│   │   ├── session-notes.md
│   │   └── reflections.md
│   ├── channels/              # Per-channel brain context
│   │   ├── work/
│   │   ├── side-project/
│   │   ├── personal/
│   │   ├── general/
│   │   └── development/
│   │       ├── backlog.md
│   │       ├── architecture.md
│   │       ├── security-log.md
│   │       └── audit-log.md
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

## Componentization (v5)

The system uses shared components to reduce duplication and keep files focused:

| Component | Location | Purpose |
|-----------|----------|---------|
| **CLAUDE.md** | Root | Compressed to ~150 lines. References AGENT_INDEX and LOADING_PROTOCOL instead of inline tables/rules. |
| **Agent Index** | `agents/AGENT_INDEX.md` | Compact routing table for all 15 agents. CLAUDE.md points here instead of listing agents inline. |
| **Loading Protocol** | `brain/LOADING_PROTOCOL.md` | Single source of truth for brain file loading tiers (hot/warm/cold). All agents reference this. |
| **Frameworks Library** | `brain/frameworks.md` | Shared analytical, strategic, coaching, and negotiation frameworks. Agents reference by name. |
| **AM Base** | `agents/account-managers/_am-base.md` | Shared Account Manager behavior. Each AM file adds only channel-specific content. |
| **Skill Pattern** | `skills/_skill-pattern.md` | Template structure for creating new skills. Includes brain loading shorthand and output routing. |
| **Universal Router** | `skills/do.md` | `/do` command that maps natural language intent to the right skill. Users only need to remember one command. |

### Design Principles

1. **Single responsibility**: Each file owns one concept. No duplication across files.
2. **Reference, don't repeat**: Agents say "Follow LOADING_PROTOCOL.md" instead of listing brain files inline.
3. **Compressed CLAUDE.md**: The main prompt is a compact index (~150 lines) that points to detailed definitions elsewhere.
4. **Shared base + overrides**: AMs inherit from `_am-base.md` and add only channel-specific behavior.

## Brain Connectivity Design

Every brain file MUST be connected to at least one other file via `[[wikilinks]]`. This ensures the knowledge graph has no orphan nodes and all information is discoverable through traversal.

### Connection Rules
1. **No orphans**: Every file links to at least one other file
2. **Bidirectional awareness**: If A links to B, B should ideally link back to A
3. **Hub files**: `Dashboard.md`, `BRAIN_INDEX.md`, and `projects.md` serve as high-connectivity hubs
4. **Cross-domain links**: Work and Side Project files share connections through `role-and-goals.md` and `priorities.md`
5. **Resource chains**: Summary → Insights → Projects → Stakeholders forms a natural chain

### Life Domain Separation

The brain supports multiple life domains that are separate but share fundamentals:

```
brain/
├── context/          ← SHARED (role, goals, decisions apply everywhere)
├── preferences/      ← SHARED (your style is consistent across domains)
├── learnings/        ← SHARED (patterns transcend domains)
├── channels/
│   ├── work/         ← DOMAIN-SPECIFIC (primary job)
│   ├── side-project/ ← DOMAIN-SPECIFIC (side hustle)
│   ├── personal/     ← DOMAIN-SPECIFIC (life admin)
│   └── development/  ← DOMAIN-SPECIFIC (system meta)
└── resources/        ← MIXED (organized by source, linked to relevant domain)
```

**Shared fundamentals** (`context/`, `preferences/`, `learnings/`):
- `role-and-goals.md` captures ALL roles (work + side project + personal)
- `priorities.md` ranks across domains (work deadline vs personal commitment)
- `communication.md` is your voice everywhere
- `patterns.md` captures cross-domain insights

**Domain-specific** (`channels/`):
- Each domain has its own brain subdirectory
- Account Managers only load their domain's files
- Prevents context bleed (work context doesn't leak into personal)

**Connection points** between domains:
- `role-and-goals.md` is the master hub linking all domains
- `priorities.md` enables cross-domain prioritization
- `Dashboard.md` shows everything in one view
- Resource insights can link across domains when relevant

### Wikilink Conventions
- Link to filename without extension: `[[projects]]`, `[[stakeholders]]`
- For subdirectory files: `[[brain/channels/work/context|Work Context]]`
- Use display names for clarity: `[[stakeholders|Jane Smith]]`
- Add links naturally within existing text, not as separate "Related" sections

## The Brain

The brain is a collection of markdown files that serve as the assistant's long-term memory. Files are organized into **three loading tiers** (Hot/Warm/Cold) to optimize context window usage — see `BRAIN_INDEX.md` for the full tier mapping. It has four layers:

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

### Specialist Agents (10)

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
| Security Scanner | Automated security scans via Caterpillar | Agent/skill/config file changes |
| Input Guard | Message screening for prompt injection and social engineering | Every incoming Telegram message |

### Multi-Agent Workflows

Some requests trigger multiple agents in sequence:

- **Analyze then Strategize**: Analyst breaks down the situation, Strategist develops the plan
- **Research then Analyze**: Market Researcher gathers data, Analyst synthesizes it
- **Strategize then Critique**: Strategist proposes, Critic stress-tests
- **Write then Review**: Writer drafts, Critic reviews for gaps

## Slash Commands

| Command | Agent | Purpose |
|---------|-------|---------|
| `/do` | Universal Router | Describe what you want in plain language; routes to the right skill |
| `/brief` | Chief of Staff | Morning briefing with current state and pending decisions |
| `/analyze` | Analyst | Deep structured analysis of a topic or resource |
| `/strategize` | Strategist | Strategic thinking session with frameworks |
| `/draft` | Writer | Create a document matching your style preferences |
| `/challenge` | Critic | Devil's advocate session to stress-test thinking |
| `/research` | Market Researcher | Web research on competitors, markets, trends |
| `/ingest` | Librarian | Process a document into the brain |
| `/onboard` | Onboarding Coach | Populate the brain through interactive Q&A |
| `/learn` | Librarian | Manually teach the system something new |
| `/status` | Chief of Staff | System health — brain freshness, security, backlog |
| `/decide` | Strategist + Critic | Structured decision framework with stress testing |
| `/digest` | Librarian | Weekly digest of brain updates and learnings |
| `/weekly-review` | Chief of Staff + Strategist | End-of-week retrospective and next-week planning |
| `/meeting-prep` | Chief of Staff + Analyst + Writer | Pre-meeting briefing with attendee context |
| `/followup` | Writer | Track commitments, surface overdue items, draft nudges |
| `/triage` | Chief of Staff + Analyst + Writer | Scan, classify, and draft responses for emails |
| `/premortem` | Critic + Strategist | Structured failure analysis before launching initiatives |
| `/report` | Writer + Analyst | Auto-generate status reports for different audiences |
| `/reflect` | Onboarding Coach | Guided reflection with spaced repetition of insights |
| `/repurpose` | Writer | Transform content into multiple formats for channels |
| `/prioritize` | Strategist | Multi-framework task prioritization |
| `/okr` | Strategist | Define, track, and review quarterly OKRs |
| `/delegate` | Chief of Staff + Writer | Track delegated tasks with automated follow-ups |
| `/extract-wisdom` | Analyst + Librarian | Quick extraction of key ideas from content |
| `/negotiate` | Strategist + Critic | Structured negotiation preparation |
| `/postmortem` | Analyst + Critic | Blameless after-action review with root cause analysis |
| `/coach` | Strategist + Writer | Leadership coaching for difficult conversations |

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
