# Content Repurposing

Transform one content asset into multiple formats optimized for different channels. Invokes the [[writer]] agent.

## When to Use

- You have a blog post, report, or document and want to distribute it across channels
- Need to announce something on multiple platforms with appropriate tone for each
- Want to maximize the reach of a single piece of content
- Turning internal content into external communications or vice versa

## Arguments

- **source** (required): The content to repurpose. Can be:
  - Pasted text directly in the conversation
  - A file path (e.g., `output/documents/2026-04-01-q1-summary.md`)
  - A URL to fetch content from

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/preferences/communication.md` -- tone, voice, and style preferences
   - `brain/preferences/document-style.md` -- formatting conventions
   - `brain/context/terminology.md` -- domain terms to use or avoid per audience
   - `brain/context/stakeholders.md` -- audience awareness

2. **Read the source content.** If the argument is a file path, read the file. If it is a URL, fetch the content. If it is pasted text, use it directly.

3. **Route to the writer agent.** Generate all five formats from the source content:

   ### LinkedIn Post
   - Professional tone, thought-leadership positioning
   - 150-300 words
   - Hook in the first line (pattern interrupt or bold claim)
   - 2-3 key insights from the content
   - End with a question or call-to-action to drive engagement
   - Include 3-5 relevant hashtags

   ### Twitter/X Thread
   - 5-7 tweets, each under 280 characters
   - Tweet 1: Hook — the most compelling or surprising takeaway
   - Tweets 2-6: One insight per tweet, conversational and punchy
   - Final tweet: Summary + CTA or link
   - Use thread numbering (1/, 2/, etc.)

   ### Email Newsletter Snippet
   - Casual, value-focused tone
   - 200-400 words
   - Subject line suggestion included
   - Opens with why this matters to the reader
   - Core insights in scannable format (bullets or short paragraphs)
   - Ends with a personal note or forward-looking thought

   ### Team Announcement
   - Internal, action-oriented tone
   - Direct and concise
   - Lead with the "so what" for the team
   - Include any action items or next steps
   - Acknowledge contributors where relevant

   ### Executive Bullet Points
   - 5 key takeaways, one sentence each
   - No fluff — each bullet must stand alone
   - Prioritized by business impact
   - Suitable for forwarding to leadership or pasting into a deck

4. **Adapt tone per format.** Use `brain/preferences/communication.md` as the baseline, then adjust:
   - LinkedIn: slightly more formal, authoritative
   - Twitter/X: conversational, punchy, accessible
   - Newsletter: warm, personal, value-driven
   - Team: direct, collegial, action-focused
   - Executive: crisp, data-oriented, strategic

5. **Present all formats in the conversation.** Clearly label each section. Do not save to file unless {{USER_FIRST_NAME}} asks.

6. **Offer follow-up options:**
   - "Want me to adjust tone or length on any of these?"
   - "Want me to save these to output/documents?" 
   - "Want me to draft a full email around the newsletter snippet?" (triggers `/draft`)

See also: [[communication]]
