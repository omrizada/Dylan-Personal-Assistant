# Do — Universal Command Router

The only command you need to remember. Describe what you want in plain language, and this skill picks the right command for you.

## How to Use

Just type `/do` followed by what you want:

```
/do prepare me for my meeting tomorrow
/do what's overdue on my plate
/do write a status update for the board
/do challenge my assumption about the talent strategy
/do remind me to call the dentist
```

## Routing Table

Match the user's intent to the best skill:

| If the user wants to... | Route to |
|------------------------|----------|
| Get caught up, morning update, "what's happening" | `/brief` |
| Analyze data, break down a document, interpret metrics | `/analyze` |
| Plan strategy, evaluate options, "how should we approach" | `/strategize` |
| Write a document, email, presentation, brief | `/draft` |
| Stress-test, poke holes, "what am I missing" | `/challenge` |
| Research competitors, market, best practices | `/research` |
| Process a document into the brain | `/ingest` |
| Teach the system something, correct it | `/learn` |
| Set up the brain, calibrate preferences | `/onboard` |
| Make a decision between options | `/decide` |
| System health, brain status, security | `/status` |
| Weekly summary of activity and changes | `/digest` |
| End-of-week review, plan next week | `/weekly-review` |
| Prepare for a meeting | `/meeting-prep` |
| Track a commitment, check what's overdue | `/followup` |
| Classify inbox, draft email responses | `/triage` |
| Imagine failure, "what could go wrong" | `/premortem` |
| Generate a status report for an audience | `/report` |
| Guided reflection, journal, review insights | `/reflect` |
| Turn content into LinkedIn/email/team formats | `/repurpose` |
| Rank tasks by priority frameworks | `/prioritize` |
| Set or track OKRs | `/okr` |
| Assign work, track delegations | `/delegate` |
| Quick takeaways from an article or content | `/extract-wisdom` |
| Prepare for a negotiation | `/negotiate` |
| After-action review, "what went wrong/right" | `/postmortem` |
| Leadership coaching, difficult conversation prep | `/coach` |

## Instructions

1. Read the user's request
2. Match their intent to the routing table above
3. If the match is clear (>80% confident): execute that skill directly with their input as arguments
4. If ambiguous (2-3 possible matches): briefly list the options and ask which they meant
5. If no match: handle the request directly without a skill, or suggest the closest option

## Examples

**User**: `/do I need to get ready for the standup tomorrow`
**Action**: Execute `/meeting-prep standup`

**User**: `/do what has Sarah not delivered yet`
**Action**: Execute `/followup check` and filter for Sarah

**User**: `/do turn my strategy doc into a LinkedIn post`
**Action**: Execute `/repurpose [content]`

**User**: `/do I'm nervous about the pricing conversation with the vendor`
**Action**: Execute `/negotiate pricing discussion with vendor`

**User**: `/do random question — what's the capital of Estonia`
**Action**: No skill match — answer directly: "Tallinn."
