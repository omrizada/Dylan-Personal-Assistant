# Contributing

Thanks for your interest in improving the Personal Assistant Template.

## How to Contribute

1. **Fork** the repository
2. **Create a branch** for your change: `git checkout -b feat/my-improvement`
3. **Make your changes** and test them
4. **Commit** with a conventional commit message: `feat: add health channel template`
5. **Push** and open a Pull Request

## What to Contribute

Good contributions:
- New agent definitions in `agents/`
- New skill definitions in `skills/`
- New channel templates in `channels/`
- Improvements to brain templates
- Documentation fixes and clarifications
- Setup script improvements (cross-platform support, etc.)
- Adaptation guides for new platforms

## What NOT to Commit

Never commit personal data:
- Populated brain files (anything in `brain/` with real data)
- Resources (anything in `resources/`)
- Generated output (anything in `output/`)
- Telegram tokens or chat IDs
- Any file containing real names, companies, or personal information

The `.gitignore` is configured to prevent most of these, but double-check your commits.

## Guidelines

- Keep agent definitions focused and under 500 lines
- Brain templates should have clear field descriptions and examples
- Test your changes by running `/onboard` with a fresh brain
- Follow the existing file structure and naming conventions
- Use `{{VARIABLE_NAME}}` syntax for any user-specific values

## Questions?

Open an issue if something is unclear.
