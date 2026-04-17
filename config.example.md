# Configuration Variables

All variables use the `{{VARIABLE_NAME}}` format. Replace them manually or run `scripts/setup.sh`.

## Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{USER_NAME}}` | Your full name | `Jane Smith` |
| `{{USER_FIRST_NAME}}` | Your first name (used in casual contexts) | `Jane` |

## Telegram Variables (Optional)

| Variable | Description | Example |
|----------|-------------|---------|
| `{{BOT_USERNAME}}` | Your Telegram bot username | `@jane_assistant_bot` |
| `{{TELEGRAM_GROUP_ID}}` | Telegram Forum group chat ID | `-1001234567890` |
| `{{TELEGRAM_USER_ID}}` | Your Telegram user ID | `123456789` |

## Path Variables (Optional)

| Variable | Description | Example |
|----------|-------------|---------|
| `{{PROJECT_DIR}}` | Absolute path to this project | `/home/jane/personal-assistant-template` |
| `{{SIDE_PROJECT_REPO_PATH}}` | Path to side project codebase | `/home/jane/my-startup` |

## Where Variables Appear

- `CLAUDE.md` — Main system prompt (most variables)
- `channels/*/context.md` — Channel configurations
- `brain/context/role-and-goals.md` — Your role description
- `brain/channels/*/` — Channel-specific brain files

## How to Apply

### Option 1: Setup Script
```bash
bash scripts/setup.sh
```

### Option 2: Manual Find-and-Replace
Search for `{{` across all `.md` files and replace each variable with your value.

### Option 3: sed (Unix/Mac)
```bash
# Example: replace user name
find . -name "*.md" -exec sed -i '' 's/{{USER_NAME}}/Jane Smith/g' {} +
find . -name "*.md" -exec sed -i '' 's/{{USER_FIRST_NAME}}/Jane/g' {} +
```
