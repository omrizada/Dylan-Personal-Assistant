#!/bin/bash
# Personal Assistant Template - Setup Script

set -e

echo "================================"
echo "  AI Personal Assistant Setup"
echo "================================"
echo ""

# Get project directory
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Ask for user's name
read -p "What's your full name? " USER_NAME
read -p "What's your first name? " USER_FIRST_NAME

# Telegram setup (optional)
echo ""
echo "Telegram Setup (optional - press Enter to skip)"
echo "See SETUP.md for how to create a bot and group"
read -p "Telegram bot username (e.g., @mybot): " BOT_USERNAME
read -p "Telegram group chat ID (e.g., -1001234567890): " TELEGRAM_GROUP_ID
read -p "Your Telegram user ID: " TELEGRAM_USER_ID

# Side project repo (optional)
echo ""
read -p "Path to side project repo (optional, press Enter to skip): " SIDE_PROJECT_REPO_PATH

# Apply replacements
echo ""
echo "Applying configuration..."

# Function to replace in files
replace_in_files() {
    local search="$1"
    local replace="$2"
    if [ -n "$replace" ]; then
        find "$PROJECT_DIR" -type f \( -name "*.md" -o -name "*.json" \) | while read file; do
            if [[ "$file" != *"node_modules"* ]] && [[ "$file" != *".git"* ]]; then
                sed -i '' "s|$search|$replace|g" "$file" 2>/dev/null || true
            fi
        done
    fi
}

replace_in_files "{{USER_NAME}}" "$USER_NAME"
replace_in_files "{{USER_FIRST_NAME}}" "$USER_FIRST_NAME"
replace_in_files "{{BOT_USERNAME}}" "${BOT_USERNAME:-{{BOT_USERNAME}}}"
replace_in_files "{{TELEGRAM_GROUP_ID}}" "${TELEGRAM_GROUP_ID:-{{TELEGRAM_GROUP_ID}}}"
replace_in_files "{{TELEGRAM_USER_ID}}" "${TELEGRAM_USER_ID:-{{TELEGRAM_USER_ID}}}"
replace_in_files "{{PROJECT_DIR}}" "$PROJECT_DIR"
replace_in_files "{{SIDE_PROJECT_REPO_PATH}}" "${SIDE_PROJECT_REPO_PATH:-{{SIDE_PROJECT_REPO_PATH}}}"

echo "Configuration applied!"
echo ""
echo "Next steps:"
echo "  1. If you haven't set up Telegram yet, see SETUP.md"
echo "  2. Launch: claude --channels plugin:telegram@claude-plugins-official"
echo "  3. Run /onboard to teach the system about you"
echo ""
echo "Done!"
