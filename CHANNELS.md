# Channels Guide

How the multi-channel system works and how to customize it.

## How Channels Work

Each channel is a **Telegram Forum topic** inside a single group. When you send a message in a topic, the system:

1. Identifies which topic the message came from
2. Loads the matching Account Manager personality from `channels/<name>/context.md`
3. Loads channel-specific brain context from `brain/channels/<name>/`
4. Processes the request with the appropriate tone and context
5. Responds in the same topic

This means you can send "give me a status update" in the Work topic and the Side Project topic and get different answers -- each scoped to the right context.

## Default Channels

| Channel | Topic Name | Personality | Purpose |
|---------|-----------|-------------|---------|
| Work | Work | Strategic, professional | Primary job tasks, meetings, stakeholders |
| Side Project | Side Project | Action-oriented, hustle | Side business or startup |
| Personal | Personal | Warm, casual | Calendar, reminders, life admin |
| General | General | Friendly, quick | Off-topic questions, random queries |
| Development | Development | Technical, concise | System bugs, feature requests, architecture |

## Creating the Telegram Forum Group

### Step 1: Create a Group

1. Open Telegram
2. Tap the compose/new message button
3. Select "New Group"
4. Name it (e.g., "My PA" or "Assistant")
5. Add your bot as a member
6. Create the group

### Step 2: Enable Topics

1. Open the group
2. Tap the group name to open settings
3. Tap "Edit"
4. Enable "Topics" (this converts the group into a Forum)
5. Save

### Step 3: Create Topics

Once Topics is enabled, you will see a "General" topic already created. Create the remaining topics:

1. Tap the "+" button to create a new topic
2. Name it exactly as shown in the table above: **Work**, **Side Project**, **Personal**, **Development**
3. The "General" topic already exists by default

Topic names are matched case-insensitively by the system, but keeping them consistent helps.

### Step 4: Set Bot as Admin

1. Go to group settings > Members
2. Find your bot
3. Promote to Admin with permissions to read and send messages

## Adding a New Channel

To add a new channel (e.g., "Health" or "Finance"):

### 1. Create the Topic

Create a new topic in your Telegram Forum group with the desired name.

### 2. Create the Channel Context File

Create `channels/<name>/context.md` with the Account Manager definition:

```markdown
# <Name> Channel

## Account Manager Personality

You are {{USER_FIRST_NAME}}'s <Name> Account Manager.

**Tone**: [Describe the personality -- warm, professional, technical, etc.]
**Style**: [Communication style -- concise, detailed, casual, formal]
**Focus**: [What this channel is about]

## Channel Scope

This channel handles:
- [Topic 1]
- [Topic 2]
- [Topic 3]

## Context

[Any standing context the AM should always know about this domain]

## Routing Rules

- Simple questions about [domain]: Handle directly
- Complex analysis: Route to Analyst
- Strategic planning: Route to Strategist
- Everything else: Route to Chief of Staff
```

### 3. Create the Channel Brain Directory

Create `brain/channels/<name>/` with an initial context file:

```markdown
---
last_updated:
confidence: low
source: template
---

# <Name> Channel Brain

## Active Items
<!-- Current items being tracked in this channel -->

## Key Context
<!-- Important background information -->
```

### 4. Update CLAUDE.md

Add the new channel to the channel routing section in `CLAUDE.md` so the system knows about it.

## Removing a Channel

1. Delete the topic from the Telegram Forum group (or just archive it)
2. Optionally remove `channels/<name>/` and `brain/channels/<name>/`
3. The system will simply not route to channels that don't have a context file

## Renaming a Channel

1. Rename the topic in the Telegram Forum group
2. Rename the directory: `channels/old-name/` to `channels/new-name/`
3. Rename the brain directory: `brain/channels/old-name/` to `brain/channels/new-name/`
4. Update any references in `CLAUDE.md`

## Customizing Account Manager Personalities

Each AM personality is defined in `channels/<name>/context.md`. You can customize:

### Tone
The emotional register. Examples:
- **Professional**: "Based on the quarterly data, I recommend..."
- **Casual**: "Hey! So looking at the numbers..."
- **Technical**: "The P95 latency increased 23ms after the deploy..."
- **Motivational**: "Let's crush this. Here's the plan..."

### Response Length
Add instructions like:
- "Keep responses under 3 sentences unless asked for detail"
- "Default to comprehensive responses with bullet points"
- "Use one-liners for simple questions, paragraphs for complex ones"

### Domain Expertise
Tell the AM what it should know about:
- "You understand SaaS metrics: MRR, churn, CAC, LTV"
- "You know the team structure and reporting lines"
- "You're familiar with the tech stack: React, Node, PostgreSQL"

### Proactive Behaviors
Define what the AM should do without being asked:
- "Flag if a deadline is within 48 hours"
- "Suggest breaks if the conversation has been going for 2+ hours"
- "Remind about weekly review every Friday"

## Adding Integrations Per Channel

Channels can have different integrations enabled. Add integration instructions to the channel context file:

### Calendar Integration (Work Channel)
```markdown
## Integrations
- **Calendar**: Check Google Calendar for meeting context when discussing schedule
- When I ask "what's next", show my next 3 calendar events
```

### GitHub Integration (Development Channel)
```markdown
## Integrations
- **GitHub**: Reference open issues and PRs when discussing bugs
- Link to relevant code when explaining architecture decisions
```

### Task Management (Side Project Channel)
```markdown
## Integrations
- **ClickUp**: Check project board for task status
- When I say "update status", create a ClickUp task update
```

The available integrations depend on which MCP servers and plugins are installed in your Claude Code setup.

## Channel-Specific Brain

Each channel maintains its own brain context in `brain/channels/<name>/`. This allows:

- The Work AM to remember your current sprint goals
- The Side Project AM to track your startup metrics
- The Personal AM to know your recurring appointments
- The Development AM to maintain a backlog of system improvements

Channel brain files follow the same auto-learning rules as the main brain -- the Librarian updates them after significant interactions in that channel.
