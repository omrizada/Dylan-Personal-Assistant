# Extract Wisdom

Quick content extraction that pulls key ideas and actionable insights from articles, transcripts, or pasted content. Lighter than `/ingest` -- does not create brain resource files. Routes to [[analyst]] for extraction, with [[librarian]] cross-referencing existing brain knowledge.

## When to Use

- When you read or watch something and want the signal without the noise
- When you want quick takeaways without a full ingestion into the brain
- When someone shares content and you need the gist fast

## Arguments

- **source** (required): A URL or pasted content (article, podcast transcript, video notes, thread)
  - Examples:
    - `https://example.com/article-on-ai-strategy`
    - Pasted text block directly in the message

## Instructions

1. **Get the content.** If a URL is provided, use WebFetch to retrieve it. If content is pasted directly, use that.

2. **The [[analyst]] extracts wisdom.** Analyze the content and produce:

   ```
   WISDOM EXTRACTION
   =================
   Source: [title or URL]
   Type: [article / podcast transcript / video notes / thread / other]

   KEY IDEAS (5)
   -------------
   1. [Idea] — [one-line explanation of why it matters]
   2. ...
   3. ...
   4. ...
   5. ...

   SURPRISING INSIGHTS (3)
   -----------------------
   1. [Insight] — [why it's counterintuitive or noteworthy]
   2. ...
   3. ...

   ACTIONABLE RECOMMENDATIONS
   --------------------------
   - [Action] — [who should do it, when, expected impact]
   - ...

   MEMORABLE QUOTES
   ----------------
   - "[Quote]" — [context or why it stands out]
   - ...

   CONNECTIONS TO YOUR WORLD
   -------------------------
   - [How this relates to an active project, pattern, or learning]
   - ...
   ```

3. **Cross-reference with brain.** Read these files to find connections:
   - `brain/context/projects.md` -- does this relate to anything {{USER_FIRST_NAME}} is working on?
   - `brain/learnings/patterns.md` -- does this confirm or challenge an existing pattern?
   - `brain/learnings/strategies.md` -- does this validate or contradict a known strategy?

4. **Output directly in conversation.** This is a quick extraction -- do NOT create files in `brain/resources/summaries/` or `brain/resources/insights/` (that is `/ingest`'s job).

5. **Offer follow-up options:**
   - "Want me to `/ingest` this for full processing into the brain?"
   - "Want me to `/learn` any of these insights?"
   - "Want me to dig deeper into any of these ideas?"

## Dependencies

- WebFetch (for URL-based content retrieval)
