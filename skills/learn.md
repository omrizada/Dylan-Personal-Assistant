# Quick Brain Update

Manually teach the system something new. Determines the right brain file(s) to update, shows the proposed change, and applies it.

## When to Use

- Teaching the system a new term, abbreviation, or shorthand
- Correcting a misunderstanding
- Adding context about a person, project, or decision
- Recording a preference or pet peeve
- Any time you say "remember this" or "from now on"

## Arguments

- **input** (required): What to remember. Natural language.
  - Examples:
    - `when I say "the bet" I mean the Job Post Bet initiative`
    - `Sarah just got promoted to VP of Product`
    - `I prefer tables over bullet lists for comparing options`
    - `we decided to delay the data pillar by 2 weeks`
    - `never use the word "synergy" in anything you write for me`

## Instructions

1. **Parse the input.** Determine what kind of knowledge this is:
   - **Terminology/shorthand** --> `brain/context/terminology.md`
   - **Person/stakeholder info** --> `brain/context/stakeholders.md`
   - **Project update** --> `brain/context/projects.md`
   - **Decision made** --> `brain/context/decisions-log.md`
   - **Role or goal change** --> `brain/context/role-and-goals.md`
   - **Communication preference** --> `brain/preferences/communication.md`
   - **Analysis preference** --> `brain/preferences/analysis-style.md`
   - **Document preference** --> `brain/preferences/document-style.md`
   - **Priority change** --> `brain/preferences/priorities.md`
   - **Pattern or learning** --> `brain/learnings/patterns.md`
   - **Feedback/correction** --> `brain/learnings/feedback.md`

   If the input spans multiple categories, update multiple files.

2. **Read the target brain file(s).** Understand what is already there to avoid duplicates and ensure the new information fits naturally.

3. **Propose the change.** Show {{USER_FIRST_NAME}} exactly what will be added or modified:
   - Quote the relevant section of the file before the change
   - Show what it will look like after the change
   - If the file does not exist yet, show the full proposed file content

4. **Wait for confirmation.** Do not write until {{USER_FIRST_NAME}} approves. If {{USER_FIRST_NAME}} suggests adjustments, revise the proposal.

5. **Apply the change.** Write to the brain file(s). Update the `last_updated` field in the frontmatter. Set `source: manual`.

6. **Update BRAIN_INDEX.md if needed.** If a new brain file was created or the scope of an existing file changed significantly, update the index.

7. **Confirm what was saved.** Brief confirmation message: what was updated and where.

### Rules

- **Minimal changes.** Only modify what is necessary. Do not rewrite entire files.
- **Preserve existing content.** Add to files, do not replace existing entries unless explicitly correcting them.
- **Handle conflicts.** If the new information contradicts something already in the brain, flag the conflict and ask which is correct.
- **Be fast.** This is meant to be a quick interaction. Do not over-engineer the change or ask unnecessary clarifying questions. If the intent is clear, propose the change immediately.
