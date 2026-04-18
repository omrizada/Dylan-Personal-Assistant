# Followup Tracker

Track commitments -- who owes what, by when -- and surface overdue items with nudge drafts. Maintains `brain/context/followups.md` as the ledger. See also [[writer]], [[Dashboard]].

## When to Use

- After a meeting where action items were assigned
- When you want to check what's overdue
- When you need to send a reminder to someone
- Anytime someone commits to doing something

## Subcommands

### `/followup add "person: task: deadline"`

Add a new commitment to the tracker.

- **person** (required): Who made the commitment
- **task** (required): What they committed to
- **deadline** (required): When it's due (date or relative like "Friday", "next week")

Examples:
- `/followup add "Sarah: send updated pitch deck: 2026-04-10"`
- `/followup add "Dev team: deploy v2.1 to staging: Friday"`
- `/followup add "Me: review Q1 board deck: tomorrow"`

### `/followup check`

Scan the followups ledger and surface status.

### `/followup nudge`

Draft reminder messages for overdue items.

## Instructions

### For `/followup add`

1. **Parse the input.** Extract person, task, and deadline from the argument string.
   - Resolve relative dates ("Friday", "next week", "tomorrow") to actual dates.
   - If parsing fails, ask for clarification rather than guessing.

2. **Load and update the ledger.** Read `brain/context/followups.md`.
   - Append a new row to the Active Commitments table:
     ```
     | Person | Commitment | Deadline | Status | Added |
     | [person] | [task] | [deadline] | pending | [today's date] |
     ```
   - Update the `last_updated` frontmatter date.

3. **Confirm.** Output a brief confirmation: "Tracked: [person] owes [task] by [deadline]."

### For `/followup check`

1. **Load the ledger.** Read `brain/context/followups.md`.

2. **Classify each active item:**
   - **Overdue**: deadline has passed, status is still pending
   - **Due soon**: deadline is within the next 3 days
   - **On track**: deadline is more than 3 days away

3. **Output a status report:**

   ```
   FOLLOWUP CHECK - [Today's Date]
   ================================

   OVERDUE
   -------
   - Person: task (due [date] -- [X] days overdue)
   - ...

   DUE SOON
   --------
   - Person: task (due [date])
   - ...

   ON TRACK
   --------
   - Person: task (due [date])
   - ...

   SUMMARY: [X] overdue, [Y] due soon, [Z] on track
   ```

4. **If items are overdue**, suggest: "Want me to draft nudge messages? Run `/followup nudge`."

### For `/followup nudge`

1. **Load the ledger.** Read `brain/context/followups.md`. Identify overdue items.

2. **Load brain context:**
   - `brain/context/stakeholders.md` -- to understand the relationship with each person
   - `brain/preferences/communication.md` -- to match {{USER_FIRST_NAME}}'s tone

3. **Route to [[writer]].** For each overdue item, draft a brief, warm reminder message:
   - Match the communication style to the relationship (formal for external, casual for close colleagues)
   - Reference the original commitment naturally
   - Suggest a new deadline or ask for an update
   - Keep it short -- 2-4 sentences max

4. **Output the drafts** directly in conversation, one per overdue item.

5. **Offer to send.** If Gmail MCP is available: "Want me to send any of these?"

### Completing Items

When {{USER_FIRST_NAME}} mentions that a followup is done:
1. Move the row from Active Commitments to Completed
2. Add the completion date and any relevant notes
3. Update the `last_updated` frontmatter date
