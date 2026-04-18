---
last_updated:
---

# {{USER_FIRST_NAME}}'s Brain Dashboard

## Quick Navigation

### Context
- [[role-and-goals]] — Who you are, objectives
- [[projects]] — Active projects, status, priorities
- [[stakeholders]] — Key people and roles
- [[decisions-log]] — Key decisions made
- [[terminology]] — Domain terms and definitions

### Preferences
- [[communication]] — Tone, format, detail level
- [[analysis-style]] — Framework and presentation preferences
- [[document-style]] — Templates, formatting, structure
- [[priorities]] — What matters most, decision weights

### Learnings
- [[patterns]] — Recurring patterns in work and decisions
- [[feedback]] — What worked, corrections received
- [[strategies]] — Successful strategies and frameworks

### Channels
- [[brain/channels/work/context|Work]] — Primary job context
- [[brain/channels/side-project/context|Side Project]] — Side project context
- [[brain/channels/personal/preferences|Personal]] — Calendar, scheduling
- [[brain/channels/development/backlog|Dev Backlog]] — System bugs and features
- [[brain/channels/development/architecture|Architecture]] — System design

---

## Brain Health

```dataview
TABLE last_updated AS "Updated", confidence AS "Confidence", source AS "Source"
FROM "brain"
WHERE file.name != "Dashboard" AND file.name != "BRAIN_INDEX"
SORT last_updated DESC
```

## Recent Changes

```dataview
TABLE file.mtime AS "Modified"
FROM "brain"
SORT file.mtime DESC
LIMIT 10
```
