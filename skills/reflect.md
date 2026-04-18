# Guided Reflection

Facilitate context-aware reflection sessions with spaced repetition of key insights. Invokes the [[onboarding-coach]] agent.

## When to Use

- End of day or end of week wind-down
- After a major decision, meeting, or milestone
- When feeling stuck or wanting to step back and think
- Periodic self-assessment and growth tracking

## Arguments

None. This skill generates prompts based on recent brain activity.

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/learnings/session-notes.md` -- recent session activity
   - `brain/learnings/patterns.md` -- observed patterns to probe
   - `brain/learnings/reflections.md` -- past reflections and scheduled reviews
   - `brain/learnings/strategies.md` -- strategies to evaluate
   - `brain/context/projects.md` -- active project context
   - `brain/context/decisions-log.md` -- recent decisions worth revisiting

2. **Check for spaced repetition reviews.** Before generating new prompts, check `brain/learnings/reflections.md` for entries where the next review date is today or overdue. Surface these first:
   - **1-day review**: Was the insight still relevant the next day?
   - **3-day review**: Has the pattern held or shifted?
   - **7-day review**: Did the insight lead to any action?
   - **30-day review**: Has this become a durable principle or was it situational?

3. **Generate 3-5 context-aware reflection prompts.** Draw from recent activity and brain content. Prompt types include:
   - **Decision reflection**: "What decision this week had the most uncertainty? What would reduce that uncertainty next time?"
   - **Project reflection**: "What would you do differently about [recent project event]?"
   - **Pattern reflection**: "You've [observed pattern] several times now. Is this intentional or something to change?"
   - **Stakeholder reflection**: "How is your working relationship with [stakeholder] evolving?"
   - **Strategy reflection**: "Is [current strategy] still the right approach given what you've learned?"
   - **Energy reflection**: "What gave you energy this week? What drained it?"

4. **Present prompts one at a time.** Wait for {{USER_FIRST_NAME}}'s response to each before moving to the next. Do not rush through them.

5. **Capture responses.** After the session, append each response to `brain/learnings/reflections.md` in this format:

   ```markdown
   ### [Date]

   **Prompt:** [The reflection question]
   **Response:** [{{USER_FIRST_NAME}}'s answer]
   **Tags:** [theme tags, e.g., #decision-making, #delegation, #strategy]
   **Next review:** [Date based on spaced repetition schedule — 1 day, 3 days, 7 days, 30 days from now]
   ```

6. **Monthly synthesis.** If there are 10+ entries in `brain/learnings/reflections.md`, offer to synthesize recurring themes:
   - Group reflections by tag
   - Identify the top 3 recurring themes
   - Note any shifts in thinking over time
   - Propose updates to `brain/learnings/patterns.md` or `brain/learnings/strategies.md` based on validated insights

7. **Update the brain index.** After writing to `brain/learnings/reflections.md`, update `brain/BRAIN_INDEX.md` with the new last-updated date.

8. **Offer follow-up options:**
   - "Want me to turn any of these insights into a strategy?" (triggers `/strategize`)
   - "Want me to update the brain with what we learned?" (triggers `/learn`)

See also: [[Dashboard]]
