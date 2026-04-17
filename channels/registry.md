# Channel Registry

Routes Telegram messages to the correct Account Manager based on **topic thread ID** within a single Forum group.

## Group Info

- **Group name**: {{USER_FIRST_NAME}}'s Assistant
- **Chat ID**: `{{TELEGRAM_GROUP_ID}}`
- **Mode**: Forum (Topics enabled)
- **Access**: Restricted to {{USER_FIRST_NAME}} (user ID `{{TELEGRAM_USER_ID}}`)

## Topic → Channel Mappings

| Thread ID | Topic Name | Channel | Account Manager | Brain Scope |
|-----------|-----------|---------|-----------------|-------------|
| `2` | Work | Work | `agents/account-managers/work-am.md` | `brain/context/`, `brain/resources/` |
| `3` | Side Project | Side Project | `agents/account-managers/side-project-am.md` | `brain/channels/side-project/` |
| `4` | Personal | Personal | `agents/account-managers/personal-am.md` | `brain/channels/personal/` |
| `5` | General | General | `agents/account-managers/general-am.md` | (none) |
| `6` | Development | Development | `agents/account-managers/dev-am.md` | `brain/channels/development/` |

## Routing Logic

When a Telegram message arrives from chat_id `{{TELEGRAM_GROUP_ID}}`:

1. Check the `message_thread_id` from the message metadata
2. Look up the thread ID in the table above to identify the channel
3. Load `channels/{channel}/context.md` for scope and config
4. Route to the channel's Account Manager agent
5. If `message_thread_id` is not in the table (e.g., General topic or unknown), route to the General AM
6. If message comes from DM (no thread ID, chat_id matches user `{{TELEGRAM_USER_ID}}`), use terminal behavior (direct team access)

## Notes

- All 5 topics share the same `chat_id` (`{{TELEGRAM_GROUP_ID}}`) -- differentiation is by `message_thread_id` only
- The bot has `requireMention: false` for this group, so it responds to all messages from {{USER_FIRST_NAME}}
- `allowFrom` restricts to {{USER_FIRST_NAME}}'s user ID only
