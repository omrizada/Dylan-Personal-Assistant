---
last_updated:
---

# Brain Index

Master index of all brain files. Updated automatically when brain files change. See [[Dashboard]] for visual navigation.

## Context

| File | Description | Last Updated | Confidence |
|------|-------------|-------------|------------|
| `context/role-and-goals.md` | Role, responsibilities, objectives | — | low |
| `context/projects.md` | Active projects, status, priorities | — | low |
| `context/stakeholders.md` | Key people, roles, relationships | — | low |
| `context/decisions-log.md` | Key decisions and rationale | — | low |
| `context/terminology.md` | Domain-specific terms | — | low |
| `context/followups.md` | Commitments tracker (who owes what, by when) | — | low |
| `context/okrs.md` | Quarterly objectives and key results | — | low |

## Preferences

| File | Description | Last Updated | Confidence |
|------|-------------|-------------|------------|
| `preferences/communication.md` | Tone, format, detail level | — | low |
| `preferences/analysis-style.md` | Frameworks, presentation style | — | low |
| `preferences/document-style.md` | Templates, formatting, structure | — | low |
| `preferences/priorities.md` | Decision weights, what matters most | — | low |

## Learnings

| File | Description | Last Updated | Confidence |
|------|-------------|-------------|------------|
| `learnings/patterns.md` | Recurring patterns in work and decisions | — | low |
| `learnings/feedback.md` | Corrections and what worked/didn't | — | low |
| `learnings/strategies.md` | Successful strategies and frameworks | — | low |
| `learnings/session-notes.md` | Cross-session context and pending follow-ups | — | low |
| `learnings/reflections.md` | Guided reflection journal with spaced repetition | — | low |

## Channel Brains

| File | Description | Last Updated | Confidence |
|------|-------------|-------------|------------|
| `channels/work/context.md` | Work channel knowledge | — | low |
| `channels/side-project/context.md` | Side project channel knowledge | — | low |
| `channels/personal/preferences.md` | Personal channel preferences | — | low |
| `channels/development/backlog.md` | Development backlog | — | low |
| `channels/development/architecture.md` | System architecture notes | — | low |
| `channels/development/security-log.md` | Security scan results from Caterpillar | — | high |
| `channels/development/audit-log.md` | Input Guard + Librarian action audit log | — | high |
| `channels/development/checkpoint.md` | Multi-step operation checkpoints | — | high |

## Resources

| File | Description | Last Updated | Source |
|------|-------------|-------------|--------|
| *No resources ingested yet. Use `/ingest` to process documents.* | | | |

---

## Memory Tiers

Brain files are classified into loading tiers to optimize context window usage:

### Hot Tier (Always Loaded)
Load these for EVERY request, regardless of topic:
| File | Why |
|------|-----|
| context/role-and-goals.md | Core identity — who the user is |
| context/projects.md | Active work — what's happening now |
| preferences/priorities.md | Decision weights — what matters most |

### Warm Tier (Loaded on Topic Match)
Load these when the topic is relevant:
| File | Load When... |
|------|-------------|
| context/stakeholders.md | People are mentioned or involved |
| context/terminology.md | Domain-specific terms appear |
| context/decisions-log.md | Decisions are being made or referenced |
| preferences/communication.md | Documents are being created |
| preferences/analysis-style.md | Analysis is being performed |
| preferences/document-style.md | Documents are being created |
| channels/*/context.md | Request comes from that channel |

### Cold Tier (Loaded on Explicit Request)
Load these ONLY when specifically needed:
| File | Load When... |
|------|-------------|
| resources/summaries/* | Specific resource is referenced by name |
| resources/insights/* | Cross-cutting analysis is needed |
| learnings/patterns.md | Pattern review or weekly check-in |
| learnings/feedback.md | System calibration or correction review |
| learnings/strategies.md | Strategy evaluation |
