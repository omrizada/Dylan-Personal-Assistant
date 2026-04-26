# Weekly Operations Cycle

End-of-week review + planning for next week. See also [[strategist]], [[analyst]], [[brain/OUTPUT_CONTRACTS|Output Contracts]].

## Trigger
- "weekly review"
- "end of week wrap-up"
- "plan next week"
- Scheduled: Friday afternoon cron

## Steps

### Step 1: Review
- **Skill**: /weekly-review
- **Agent**: Chief of Staff -> Strategist
- **Output contract**: /weekly-review (completed, slipped, decisions, patterns, next_week_priorities)

### Step 2: Followup Check
- **Skill**: /followup check
- **Output contract**: /followup (overdue, due_soon, nudge_drafts)

### Step 3: OKR Progress
- **Skill**: /okr check
- **Condition**: Only if OKRs are defined in brain/context/okrs.md
- **Output**: OKR status dashboard

### Step 4: Brain Health
- **Skill**: /status
- **Output**: Stale files, security scan age, backlog items

### Step 5: Synthesize
- **Agent**: Chief of Staff
- **Input**: Steps 1-4 combined
- **Output**: Unified weekly summary with action items for next week

## Output
- Saved to: `output/documents/{date}-weekly-ops.md`
- Brain updates: session-notes.md, projects.md (if status changed)
