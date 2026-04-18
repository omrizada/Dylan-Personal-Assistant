---
last_updated: 2026-04-18
---

# Brain Loading Protocol

Single source of truth for when and how agents load brain files. All agents and skills reference this protocol instead of defining their own loading rules.

See also [[BRAIN_INDEX]] and [[Dashboard]].

## Universal Rules

1. Read this protocol at session start
2. Load hot-tier files for EVERY request
3. Check `valid_until` dates — flag stale facts
4. Load warm-tier files only when the topic matches
5. Load cold-tier files only when explicitly referenced
6. Never load all brain files at once — context window budget matters

## Tier Definitions

### Hot Tier (Always Loaded — every request)
| File | Why |
|------|-----|
| context/role-and-goals.md | Core identity |
| context/projects.md | Active work |
| preferences/priorities.md | Decision weights |

### Warm Tier (Loaded on Topic Match)
| File | Load When... |
|------|-------------|
| context/stakeholders.md | People are mentioned |
| context/terminology.md | Domain terms appear |
| context/decisions-log.md | Decisions referenced |
| context/followups.md | Commitments discussed |
| context/okrs.md | Goals/OKRs discussed |
| preferences/communication.md | Documents being created |
| preferences/analysis-style.md | Analysis being performed |
| preferences/document-style.md | Documents being created |
| channels/*/context.md | Request from that channel |

### Cold Tier (Loaded on Explicit Request Only)
| File | Load When... |
|------|-------------|
| resources/summaries/* | Specific resource referenced by name |
| resources/insights/* | Cross-cutting analysis needed |
| learnings/patterns.md | Pattern review or weekly check-in |
| learnings/feedback.md | System calibration |
| learnings/strategies.md | Strategy evaluation |
| learnings/session-notes.md | Session continuity |
| learnings/reflections.md | Reflection review |

## Agent Loading Profiles

| Agent | Hot (always) | Warm (add when relevant) |
|-------|-------------|-------------------------|
| Chief of Staff | Standard hot + BRAIN_INDEX | All — routes to specialists |
| Analyst | Standard hot + analysis-style | resources/summaries/*, terminology |
| Strategist | Standard hot + decisions-log | terminology, okrs |
| Writer | Standard hot + document-style, communication | stakeholders, terminology |
| Critic | Standard hot + decisions-log | terminology |
| Market Researcher | Standard hot + terminology | resources/insights/* |
| Librarian | Standard hot + BRAIN_INDEX | All — maintains brain |
| Onboarding Coach | Standard hot + all preferences | learnings/*, session-notes |
| Security Scanner | None — reads project files directly | N/A |
| Input Guard | None — screens messages only | N/A |

## Account Manager Loading Profiles

| AM | Channel Brain | Additional Warm Files |
|----|--------------|----------------------|
| Work AM | Standard hot + channels/work/context.md | stakeholders, terminology |
| Side Project AM | channels/side-project/* | side project codebase (read-only) |
| Personal AM | channels/personal/preferences.md | followups |
| General AM | None (stateless) | N/A |
| Dev AM | channels/development/* | BRAIN_INDEX, all project files |
