# Delegation Tracker

Track delegated tasks with automated follow-up reminders. Routes to [[chief-of-staff]] for orchestration and [[writer]] for check-in message drafts.

## When to Use

- When assigning a task to someone and want to track it
- When checking on outstanding delegations
- When following up on overdue tasks

## Arguments

- **assignment** (optional): `"assignee: task: deadline"` format
  - Examples:
    - `"Sarah: Complete Monday board setup: 2026-04-25"`
    - `"Dev team: Send revised proposal to client: 2026-04-10"`
- **subcommand** (optional): `status` or `check`
  - `/delegate status` -- show all active delegations
  - `/delegate check` -- surface overdue items and draft follow-ups

## Instructions

### Creating a Delegation

1. **Parse the assignment.** Extract assignee, task description, and deadline from the argument string (format: `assignee: task: deadline`).

2. **Create a ClickUp task.** Use the ClickUp MCP to:
   - Create a task with the delegated item as the title
   - Assign to the appropriate person (resolve via `clickup_find_member_by_name`)
   - Set the due date to the provided deadline
   - Add a tag: `delegated`

3. **Log to brain.** Append the delegation to `brain/context/followups.md`:
   ```
   - [ ] [Assignee]: [Task] — Due: [Deadline] — ClickUp: [task link]
     Delegated: [today's date]
   ```

4. **Schedule a reminder.** Use CronCreate to schedule a check-in reminder for the deadline date. The reminder should trigger a `/delegate check` for this specific item.

5. **Confirm to {{USER_FIRST_NAME}}.** Output:
   ```
   DELEGATED
   ---------
   To: [Assignee]
   Task: [Task description]
   Deadline: [Date]
   ClickUp: [task link]
   Reminder: Set for [deadline date]
   ```

### `/delegate status`

1. **Load followups.** Read `brain/context/followups.md`.

2. **Load ClickUp tasks.** Filter ClickUp tasks with the `delegated` tag to get current statuses.

3. **Output a status board:**
   ```
   ACTIVE DELEGATIONS
   ==================

   ON TRACK
   --------
   - [Assignee]: [Task] — Due in [X days] ([date])

   DUE SOON (within 3 days)
   ------------------------
   - [Assignee]: [Task] — Due in [X days] ([date])

   OVERDUE
   -------
   - [Assignee]: [Task] — [X days] overdue ([date])

   COMPLETED
   ---------
   - [Assignee]: [Task] — Completed [date]
   ```

### `/delegate check`

1. **Identify overdue and due-soon items.** Read `brain/context/followups.md` and cross-reference with ClickUp task statuses.

2. **Load stakeholder context.** Read `brain/context/stakeholders.md` for context on each assignee (communication style, relationship).

3. **The [[writer]] drafts check-in messages** for each overdue or due-soon item:
   - Tone: friendly but direct (not passive-aggressive)
   - Include the specific task and original deadline
   - Ask for a status update or revised ETA
   - Adapt tone based on stakeholder relationship

4. **Output:**
   ```
   DELEGATION CHECK-IN
   ===================

   OVERDUE ([count])
   -----------------
   [Assignee]: [Task] — [X days] overdue
   Draft message:
   > [Check-in message]

   DUE SOON ([count])
   ------------------
   [Assignee]: [Task] — Due in [X days]
   Draft message:
   > [Gentle reminder message]
   ```

5. **Offer next steps:**
   - "Send these check-ins?" (via appropriate channel)
   - "Escalate any of these?"
   - "Extend a deadline?"

## Dependencies

- ClickUp MCP (task creation, status tracking, member resolution)
- CronCreate (deadline reminders)
