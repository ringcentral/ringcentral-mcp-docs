# RingCentral Claude Plugin

This repository is the single source of truth for the **`ringcentral`** Claude Code plugin — skills, MCP server config, and hooks all live here alongside the docs site. Previously the plugin was maintained in a separate repo; those files have been merged in so that skill definitions, their documentation, and their published site stay in sync in one place.

## Why merge the plugin in here

- One set of skill files instead of two copies drifting apart.
- Skill docs published to the MCP docs site (`docs/skills/`) are generated straight from the plugin's `skills/*/SKILL.md` files, so the plugin and the docs can no longer disagree.
- One PR, one review, one release for a skill change.

## Repo layout

```
.
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest (name, version, description, author)
├── .mcp.json                    # MCP server config bundled with the plugin (phone, team-chat)
├── hooks/                       # mkdocs build hooks (NOT Claude Code plugin hooks)
│   ├── skill_downloads.py       # Generates skill download links/snippets for the docs site
│   └── fix_ringcentral_redirect.py
├── skills/                      # Plugin skills — canonical source, one dir per skill
│   ├── call-recap/SKILL.md
│   ├── colleague-lookup/SKILL.md
│   ├── send-sms/SKILL.md
│   └── ...
├── CLAUDE_PLUGIN_CHANGELOG.md   # Plugin version history
├── CLAUDE_PLUGIN_LICENSE        # MIT license for the plugin
├── CLAUDE_PLUGIN_README.md      # This file
├── mkdocs.yml / docs/ / requirements.txt   # MkDocs-Material docs site (separate concern, see README.md)
```

`README.md` at the repo root documents the MkDocs site itself (local dev, deploy). This file documents the plugin that happens to live in the same repo.

Note: `hooks/` here are **mkdocs build hooks**, not [Claude Code plugin hooks](https://code.claude.com/docs/en/hooks) (which would live at `hooks/hooks.json` at the plugin root). This plugin doesn't currently define any Claude Code hooks.

## Plugin identity

Defined in `.claude-plugin/plugin.json`:

- **name**: `ringcentral` — skills are invoked as `/ringcentral:<skill-name>`
- **version**: bump this on every change that should ship to installed users (see [version management](https://code.claude.com/docs/en/plugins-reference#version-management))
- **description / keywords / homepage / repository / license**: shown in the plugin manager and marketplace listing

## Working on a skill

1. Edit or add a folder under `skills/<skill-name>/SKILL.md`. Frontmatter needs at least a `description` clear enough for Claude to know when to trigger it.
2. If the skill should also appear on the docs site, add/update the matching page in `docs/skills/<skill-name>.md` (these pull skill content in via snippets — see `hooks/skill_downloads.py`) and add it to `nav:` in `mkdocs.yml`.
3. Bump `version` in `.claude-plugin/plugin.json` and add an entry to `CLAUDE_PLUGIN_CHANGELOG.md`.

## Testing locally

```bash
claude --plugin-dir .
```

Then in that session:

```
/ringcentral:send-sms
/reload-plugins   # pick up edits without restarting
```

Confirm skills show up under `/help` → Custom commands, and check `/context` for anything else the plugin defines.

## Validating before submission

Anthropic's public marketplace review runs `claude plugin validate` on submission. Run it locally first:

```bash
claude plugin validate .
```

Warnings don't fail validation by default; add `--strict` to treat them as errors and catch anything the reviewer would flag.

## Submitting to the public plugin directory

Per [Create plugins](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace), third-party plugins go through the `claude-community` marketplace:

1. Make sure `.claude-plugin/plugin.json` has an accurate `version`, `description`, `homepage`, `repository`, and `license`.
2. Run `claude plugin validate .` (add `--strict` to be thorough) and fix anything it flags.
3. Submit via the in-app form:
   - claude.ai: [claude.ai/admin-settings/directory/submissions/plugins/new](https://claude.ai/admin-settings/directory/submissions/plugins/new) (requires Team/Enterprise org + directory management access)
   - Console: [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit) (for individual authors)
4. Once approved, the plugin is pinned to a commit SHA in [`anthropics/claude-plugins-community`](https://github.com/anthropics/claude-plugins-community); CI there bumps the pin as new commits land on this repo. The public catalog syncs nightly, so check the community catalog's `marketplace.json` to confirm it's installable before announcing it.

Submitting to the form does **not** add the plugin to Anthropic's curated `claude-plugins-official` marketplace — that's a separate, Anthropic-controlled list.

## Versioning and releases

- `CLAUDE_PLUGIN_CHANGELOG.md` tracks plugin-facing changes (skills added/changed, MCP server bumps).
- Bump `.claude-plugin/plugin.json`'s `version` whenever a change should reach installed users — installed users only get updates when this field changes (except for `command`-sourced installs).
- The MCP servers referenced in `.mcp.json` (`phone`, `team-chat`) are versioned independently (currently RingEX v1.1.0); note server version bumps in the changelog too since they can change tool behavior even without a plugin version bump.

## License

MIT — see `CLAUDE_PLUGIN_LICENSE`.
