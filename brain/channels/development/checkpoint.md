---
last_updated:
confidence: high
source: system
---

# Operation Checkpoints

Tracks progress for multi-step batch operations (like /ingest of multiple files). If an operation is interrupted, it can resume from the last checkpoint.

See also [[backlog]], [[architecture]], [[Dashboard]].

## Format

```
### [Operation ID] — [Description]
- **Started**: [timestamp]
- **Status**: in-progress | completed | failed
- **Total steps**: [N]
- **Completed steps**: [list]
- **Current step**: [N]
- **Failed step**: [N, if any] — Error: [description]
- **Resume from**: [step N]
```

## Active Operations

*No active operations. Checkpoints are created automatically during batch /ingest and other multi-step operations.*

## Completed Operations

*Completed operations are archived here for reference.*
