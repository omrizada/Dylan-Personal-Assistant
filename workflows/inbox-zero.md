# Inbox Zero Pipeline

Triage email -> extract commitments -> delegate actions. See also [[analyst]], [[writer]], [[brain/OUTPUT_CONTRACTS|Output Contracts]].

## Trigger
- "process my inbox"
- "inbox zero"
- "triage my email"

## Steps

### Step 1: Triage
- **Skill**: /triage
- **Agent**: Analyst + Writer
- **Output contract**: /triage (urgent, needs_response, fyi, noise, action_items_extracted)

### Step 2: Extract Commitments
- **Skill**: /followup add (for each action item extracted)
- **Input**: Step 1 action_items_extracted
- **Action**: Add each commitment to brain/context/followups.md

### Step 3: Delegate (if applicable)
- **Skill**: /delegate (for delegatable action items)
- **Condition**: Only for items the user assigns to others
- **Action**: Create ClickUp tasks, schedule reminders

### Step 4: Draft Responses
- **Agent**: Writer
- **Input**: Step 1 urgent + needs_response items
- **Output**: Draft responses ready for user review

## Output
- Gmail drafts created for urgent items
- Followups logged in brain/context/followups.md
- ClickUp tasks created for delegated items
