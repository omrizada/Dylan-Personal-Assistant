# Situational Leadership Coach

On-demand coaching for difficult conversations, feedback, conflict resolution, and team dynamics. Routes to [[strategist]] for framework selection and strategy, then [[writer]] for language, scripts, and role-play. Uses [[stakeholders]] context for the people involved.

## When to Use

- Before a difficult conversation (performance, conflict, bad news)
- When preparing to give feedback (positive or constructive)
- When navigating team conflict or interpersonal tension
- When someone needs motivation and you are not sure how to approach it
- After a conversation went poorly and you want to debrief

## Arguments

- **situation** (required): The situation you need coaching on
  - Examples:
    - `"Giving critical feedback to a senior team member who missed deliverables"`
    - `"Resolving conflict between two direct reports"`
    - `"Motivating a team after a failed launch"`
    - `"Having a compensation conversation with an underperforming employee"`
    - `"Debrief: the 1:1 with Sarah did not go well"`

## Instructions

1. **Load context.** Read brain files for relevant background:
   - `brain/context/stakeholders.md` -- context on the people involved (role, relationship, communication style, what they care about)
   - `brain/learnings/patterns.md` -- any prior patterns in how {{USER_FIRST_NAME}} handles these situations
   - `brain/learnings/feedback.md` -- any coaching corrections from past sessions

2. **Ask clarifying questions if needed.** Keep to 1-2 questions max:
   - What outcome do you want from this conversation?
   - What is the relationship like with this person?

3. **The [[strategist]] selects and applies the right framework:**

   ### Framework 1: SBI (Situation-Behavior-Impact)
   *Best for: Giving specific, behavioral feedback*

   ```
   SITUATION: [When/where did it happen?]
   BEHAVIOR: [What specifically did they do? Observable, not interpretive]
   IMPACT: [What was the effect on you, the team, or the outcome?]
   ```

   ### Framework 2: GROW (Goal-Reality-Options-Will)
   *Best for: Coaching conversations and helping someone solve their own problem*

   ```
   GOAL: What do you want to achieve in this conversation?
   REALITY: What is the current situation? What have you tried?
   OPTIONS: What could you do? (Generate multiple paths)
   WILL: What will you specifically do, by when?
   ```

   ### Framework 3: NVC (Nonviolent Communication)
   *Best for: Conflict resolution and emotionally charged situations*

   ```
   OBSERVATION: [What happened, without judgment]
   FEELING: [How it made you feel]
   NEED: [What underlying need is not being met]
   REQUEST: [Specific, actionable ask]
   ```

4. **The [[writer]] provides practical language:**

   ```
   COACHING: [Situation Summary]
   =============================

   FRAMEWORK: [Which framework and why]

   RECOMMENDED APPROACH
   --------------------
   - Open with: "[exact opening line]"
   - Key points to make:
     1. [Point] — "[suggested language]"
     2. [Point] — "[suggested language]"
   - Close with: "[exact closing line]"

   SCRIPTS YOU CAN ADAPT
   ---------------------
   Opening:
   > "[Full opening script — 2-3 sentences]"

   Delivering the core message:
   > "[Full script for the main point]"

   If they get defensive:
   > "[De-escalation script]"

   If they get emotional:
   > "[Empathy-first script]"

   Closing and next steps:
   > "[Wrap-up script with clear commitments]"

   WHAT TO AVOID
   -------------
   - [Common mistake 1] — say [this] instead of [that]
   - [Common mistake 2] — say [this] instead of [that]

   ROLE-PLAY
   ---------
   Ready to practice? I'll play [the other person] based on what we know about them.
   Tell me your opening line and I'll respond as they would.
   ```

5. **If this is a debrief (conversation already happened):**
   - Skip the scripts
   - Ask what happened and how it went
   - Analyze what worked and what did not
   - Suggest adjustments for next time
   - Capture learnings in `brain/learnings/patterns.md` if significant

6. **Output directly in conversation.** Do not save to a file unless {{USER_FIRST_NAME}} asks.

7. **Offer follow-up options:**
   - "Want to role-play this conversation?"
   - "Want me to adjust the approach for a different tone?"
   - "Want me to draft a follow-up message after the conversation?" (triggers `/draft`)
