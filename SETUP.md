# Setup Guide

Step-by-step instructions for getting your personal assistant team running.

## Prerequisites

- **Claude Code** installed and working ([install guide](https://claude.ai/code))
- **Telegram account** with a phone number
- A terminal (macOS Terminal, iTerm2, Linux terminal, or WSL on Windows)

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/personal-assistant-template.git
cd personal-assistant-template
```

## Step 2: Run the Setup Script

The setup script configures your name and optional integrations:

```bash
bash scripts/setup.sh
```

It will ask for:
- Your full name and first name
- Telegram bot username (optional, can do later)
- Telegram group chat ID (optional)
- Your Telegram user ID (optional)
- Side project repo path (optional)

All optional fields can be skipped by pressing Enter. You can always configure them later by editing the files manually (see Manual Configuration below).

## Step 3: Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot`
3. Choose a display name (e.g., "My Assistant")
4. Choose a username (e.g., `my_assistant_bot`) — must end in `bot`
5. BotFather will give you a **bot token** like `1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ`. Save this.
6. Send `/mybots` to BotFather, select your bot, then **Bot Settings** > **Group Privacy** > **Turn off** (so the bot can read group messages)

## Step 4: Install Obsidian (Optional but Recommended)

Obsidian gives you a visual graph view, rich editing, and mobile access to your brain files.

1. **Install Obsidian** (free):
   ```bash
   brew install --cask obsidian
   ```
   Or download from [obsidian.md](https://obsidian.md).

2. The setup wizard can do this for you — it detects whether Obsidian is installed and offers to install it.

3. **Open the brain folder as a vault**: In Obsidian, click "Open folder as vault" and select the `brain/` directory inside your project.

4. **Install the Dataview plugin**: Go to Settings → Community Plugins → Browse → search "Dataview" → Install → Enable. This powers the dynamic dashboards in `Dashboard.md`.

## Step 5: Install Caterpillar (Optional — Security Scanner)

Caterpillar scans your agent and skill files for security threats.

```bash
npm install -g @alice-io/caterpillar
```

Run a baseline scan:
```bash
caterpillar scan . --mode offline
```

The Security Scanner agent will use Caterpillar automatically when you create or modify agent/skill files.

## Step 6: Install the Telegram Plugin

In Claude Code:

```
/plugin install telegram@claude-plugins-official
```

## Step 7: Configure the Bot Token

In Claude Code:

```
/telegram:configure YOUR_BOT_TOKEN
```

Replace `YOUR_BOT_TOKEN` with the token from BotFather.

## Step 8: Create a Telegram Forum Group

1. Open Telegram and create a new **Group**
2. Name it something like "My Assistant" or "PA Team"
3. Go to group settings > **Edit** > enable **Topics** (this turns it into a Forum group)
4. Create 5 topics:
   - **Work** — for your primary job
   - **Side Project** — for your side hustle
   - **Personal** — for calendar, reminders, life admin
   - **General** — for off-topic questions
   - **Development** — for system bugs and feature requests

## Step 9: Add the Bot to the Group

1. Go to your Forum group settings
2. Add your bot as a member
3. Promote it to **Admin** (it needs admin rights to read and send messages in topics)

## Step 10: Get Your IDs

### Group Chat ID

The easiest way to get your group chat ID:
1. Add `@RawDataBot` to your group temporarily
2. It will print a JSON message containing the chat ID (a negative number like `-1001234567890`)
3. Remove `@RawDataBot` from the group

### Your User ID

Send a message to `@RawDataBot` in a private chat. It will show your user ID.

### Update Configuration

If you didn't provide these during setup, update them now:

1. Edit `CLAUDE.md` and replace `{{TELEGRAM_GROUP_ID}}` with your group chat ID
2. Replace `{{TELEGRAM_USER_ID}}` with your user ID
3. Replace `{{BOT_USERNAME}}` with your bot username (e.g., `@my_assistant_bot`)

## Step 11: Pair Your Account

In Claude Code:

```
/telegram:access
```

Follow the prompts to pair your Telegram account and add the group.

## Step 12: Launch

```bash
claude --channels plugin:telegram@claude-plugins-official
```

The assistant is now listening on your Telegram group. Send a message in any topic to test it.

## Step 13: Onboard

Send `/onboard` in any channel. The Onboarding Coach will walk you through a series of questions to populate the brain with your context:

- Your role and responsibilities
- Active projects and priorities
- Key stakeholders
- Communication preferences
- Decision-making style

This takes about 10-15 minutes and dramatically improves the assistant's usefulness.

## Step 14: Test Each Channel

Send a test message in each topic to verify the Account Managers respond with the correct personality:

- **Work**: "What's on my plate this week?"
- **Side Project**: "Give me a status update"
- **Personal**: "Remind me to call the dentist tomorrow"
- **General**: "What's the weather like in Tel Aviv?"
- **Development**: "List current system limitations"

---

## Manual Configuration

If you prefer not to use the setup script, or need to change values later, edit the following files directly. Search for `{{VARIABLE_NAME}}` placeholders and replace them:

| Variable | Where Used | Description |
|----------|-----------|-------------|
| `{{USER_NAME}}` | CLAUDE.md, brain files | Your full name |
| `{{USER_FIRST_NAME}}` | CLAUDE.md, agent files | Your first name |
| `{{BOT_USERNAME}}` | CLAUDE.md | Your Telegram bot username (e.g., @mybot) |
| `{{TELEGRAM_GROUP_ID}}` | CLAUDE.md | Telegram Forum group chat ID |
| `{{TELEGRAM_USER_ID}}` | CLAUDE.md | Your Telegram user ID |
| `{{PROJECT_DIR}}` | CLAUDE.md | Absolute path to this project directory |
| `{{SIDE_PROJECT_REPO_PATH}}` | channels/side-project/context.md | Path to side project repo (optional) |

See [config.example.md](config.example.md) for a full reference of all variables.

---

## Troubleshooting

### Bot doesn't respond in the group
- Verify the bot is an admin in the group
- Check that Group Privacy is turned **off** in BotFather settings
- Ensure you launched with `--channels plugin:telegram@claude-plugins-official`

### Bot responds but doesn't know who I am
- Run `/onboard` to populate the brain
- Check that `brain/context/role-and-goals.md` has content

### Wrong personality in a channel
- Check the topic name matches one of: Work, Side Project, Personal, General, Development
- Check the channel context file in `channels/<channel>/context.md`

### Plugin not found
- Run `/plugin install telegram@claude-plugins-official` in Claude Code
- Ensure Claude Code is up to date
