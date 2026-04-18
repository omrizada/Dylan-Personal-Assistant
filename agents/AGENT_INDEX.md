# Agent Index

Compact routing reference. Load the FULL agent definition only after routing.

## Account Managers (Telegram channels)

| AM | File | Channel | Thread ID |
|----|------|---------|-----------|
| Work | work-am.md | Work | {{WORK_THREAD_ID}} |
| Side Project | side-project-am.md | Side Project | {{SIDE_PROJECT_THREAD_ID}} |
| Personal | personal-am.md | Personal | {{PERSONAL_THREAD_ID}} |
| General | general-am.md | General | {{GENERAL_THREAD_ID}} |
| Dev | dev-am.md | Development | {{DEV_THREAD_ID}} |

## Specialist Agents (Internal team)

| Agent | File | Route When |
|-------|------|-----------|
| Chief of Staff | chief-of-staff.md | Complex/ambiguous requests, multi-agent coordination, AM escalations |
| Analyst | analyst.md | "analyze", data interpretation, metrics, patterns, resource digestion |
| Strategist | strategist.md | "strategy", planning, decisions, roadmaps, OKRs, prioritization |
| Writer | writer.md | "write", "draft", documents, emails, reports, presentations |
| Critic | critic.md | "challenge", stress-test, risk assessment, blind spots |
| Market Researcher | market-researcher.md | "research", competitors, benchmarks, market trends |
| Librarian | librarian.md | /ingest, brain maintenance, knowledge retrieval, brain updates |
| Onboarding Coach | onboarding-coach.md | /onboard, weekly check-in, preference calibration |
| Security Scanner | security-scanner.md | AUTO: agent/skill/config file created or modified |
| Input Guard | input-guard.md | AUTO: all incoming Telegram messages (screens before AM) |

## Routing Priority

1. Telegram message → Input Guard screens → Channel Router → AM
2. AM handles directly OR escalates to Chief of Staff
3. Chief of Staff routes to 1+ specialists
4. Terminal (no Telegram) → direct to team, no AM layer
