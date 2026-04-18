# System Status

Show system health: brain freshness, channel activity, security scan results.

## Instructions

1. Read `brain/BRAIN_INDEX.md` for file health
2. Check last_updated dates across all brain files
3. Read `brain/channels/development/security-log.md` for latest scan results
4. Read `brain/channels/development/audit-log.md` for recent activity
5. Read `brain/channels/development/backlog.md` for open items

## Output Format

```
## System Status

### Brain Health
- Total files: X
- Hot tier: [list with freshness]
- Stale files (>2 weeks): [list]
- Last brain update: [date]

### Security
- Last Caterpillar scan: [date] — [grade]
- Open security findings: [count]
- Audit log entries (last 7 days): [count]

### Development
- Open backlog items: [count]
- Last system change: [date]

### Channels
- Active channels: [list]
- Last activity per channel: [dates]
```
