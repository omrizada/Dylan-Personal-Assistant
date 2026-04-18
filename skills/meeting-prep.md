# Meeting Prep

Pre-meeting briefing that pulls together attendee context, relevant project status, and suggested talking points into a scannable 1-page prep doc. Routes to [[chief-of-staff]] for orchestration, then [[analyst]] for context synthesis and [[writer]] for the brief.

## When to Use

- Before any meeting where you want to walk in prepared
- When you need a quick refresher on attendees and their context
- Before important calls where you need talking points ready

## Arguments

- **meeting** (required): The meeting name, topic, or "next meeting" to auto-detect.
  - Examples:
    - `Board sync`
    - `next meeting`
    - `1:1 with Sarah`
    - `Product roadmap review`

## Instructions

1. **Find the meeting.** Use Google Calendar MCP to locate the meeting:
   - If argument is "next meeting", find the next upcoming event
   - Otherwise, search for a matching event by name
   - Extract: title, time, attendees, description/agenda, location/link

2. **Load brain context.** Read relevant brain files:
   - `brain/context/stakeholders.md` -- cross-reference attendees to get backgrounds, roles, what they care about
   - `brain/context/projects.md` -- find projects relevant to this meeting's topic or attendees
   - `brain/learnings/session-notes.md` -- check for prior meeting notes or context with these people
   - `brain/context/decisions-log.md` -- any pending or recent decisions relevant to the meeting topic
   - `brain/context/followups.md` -- any open commitments involving the attendees

3. **The [[analyst]] synthesizes context.** Pull together:
   - Who each attendee is (role, relationship, what they care about)
   - What projects or topics connect to this meeting
   - Any open items, commitments, or unresolved questions with these people
   - Recent decisions or changes that are relevant

4. **The [[writer]] structures the prep brief:**

   ```
   MEETING PREP: [Meeting Title]
   [Date] [Time]
   ==============================

   ATTENDEES
   ---------
   - Name -- Role, Organization
     Context: what they care about, recent interactions
   - ...

   AGENDA / PURPOSE
   ----------------
   - From calendar description, or inferred from context
   - Key topics likely to come up

   RELEVANT STATUS
   ---------------
   - Project/topic -- current status, recent changes
   - ...

   OPEN ITEMS WITH ATTENDEES
   -------------------------
   - Person: commitment/question -- status
   - ...

   SUGGESTED TALKING POINTS
   ------------------------
   1. Point -- why it matters, what to aim for
   2. ...

   QUESTIONS TO ASK
   ----------------
   - Question -- why it's important to raise
   - ...

   WATCH FOR
   ---------
   - Sensitivities, risks, or dynamics to be aware of
   ```

5. **Output directly in conversation.** Do not save to a file -- this is a quick-reference prep that should be immediately visible.

6. **Offer follow-up options:**
   - "Want me to draft an agenda to send to attendees?" (triggers `/draft`)
   - "Want me to research any of these topics before the meeting?" (triggers `/research`)
