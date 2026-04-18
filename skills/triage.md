# Email Triage

Scan, classify, and draft responses for unread emails. Routes to [[chief-of-staff]] for orchestration, then [[analyst]] for classification and [[writer]] for response drafts.

## When to Use

- Start of day inbox processing
- When you're behind on email and need to catch up fast
- When you want a prioritized view of what needs attention
- Anytime you say "what's in my inbox" or "triage my email"

## Arguments

- **scope** (optional): How far back to scan. Defaults to unread.
  - Examples:
    - `unread` (default)
    - `today`
    - `last 24 hours`
    - `since Monday`

## Instructions

1. **Scan the inbox.** Use Gmail MCP to fetch recent unread emails:
   - Get message list matching the scope
   - For each message, extract: sender, subject, snippet/body, date, labels

2. **Load brain context.** Read relevant brain files:
   - `brain/context/stakeholders.md` -- to weight sender importance and identify known contacts
   - `brain/context/projects.md` -- to flag project-relevant emails
   - `brain/preferences/communication.md` -- for response drafting tone

3. **The [[analyst]] classifies each email** into one of four categories:

   | Category | Criteria | Action |
   |----------|----------|--------|
   | **Urgent** | Time-sensitive, from key stakeholder, requires immediate action | Flag and surface first |
   | **Needs Response** | Requires a reply but not time-critical | Draft a response |
   | **FYI** | Informational, no action needed, but worth knowing about | Brief summary |
   | **Noise** | Newsletters, marketing, automated notifications | Skip or batch-dismiss |

   Classification factors:
   - Sender importance (stakeholders.md match = higher priority)
   - Project relevance (projects.md match = higher priority)
   - Time sensitivity (mentions of deadlines, "ASAP", "urgent")
   - Whether a response is explicitly requested

4. **Structure the triage report:**

   ```
   EMAIL TRIAGE - [Today's Date]
   ==============================
   [X] emails scanned, [Y] need attention

   URGENT ([N])
   ------------
   - From: [sender] -- [subject]
     Context: [why it's urgent, connection to projects/stakeholders]
     Suggested action: [what to do]

   NEEDS RESPONSE ([N])
   --------------------
   - From: [sender] -- [subject]
     Summary: [1-2 sentence summary]
     Draft response: [short draft if straightforward]

   FYI ([N])
   ---------
   - [sender]: [subject] -- [1-line summary]

   NOISE ([N])
   -----------
   - [count] emails skipped (newsletters, notifications, etc.)

   ACTION ITEMS
   ------------
   Extracted from emails that require follow-through:
   - [ ] Action item from email X
   - [ ] Action item from email Y
   ```

5. **The [[writer]] drafts responses** for "Needs Response" emails:
   - Match {{USER_FIRST_NAME}}'s communication style from preferences
   - Keep responses concise and direct
   - For complex emails, draft a holding response and flag for deeper attention

6. **Output directly in conversation.** Do not save to a file.

7. **Offer follow-up options:**
   - "Want me to send any of these draft responses?"
   - "Want me to add any action items to followups?" (triggers `/followup add`)
   - "Want me to do a deeper analysis on any of these?" (triggers `/analyze`)
