# Claude Agents & Skills Management

This document outlines how Claude agents and skills are managed across RingCentral's plugin and documentation repositories.

## Repository Structure

Skills are maintained in **two repositories** to serve different purposes:

1. **`ringcentral-mcp-docs`** (this repository)
   - Documentation and reference for all RingCentral Claude skills
   - Source of truth for skill specifications and behavior
   - Primary location for skill development and iteration

2. **`ringex-claude-plugin`** (separate plugin repository)
   - Packaged Claude plugin for distribution
   - Skills deployed to end users
   - Plugin configuration and manifest files

## Skill Synchronization

### When to Sync

**Sync from documentation → plugin:**
- After finalizing a new skill in this documentation repository
- After bug fixes or feature updates to a skill
- Before any plugin release or submission to Claude marketplace

**Sync from plugin → documentation:**
- When a skill receives critical fixes in production that aren't yet documented
- To keep documentation up-to-date with deployed versions
- After community feedback or issues are resolved in the plugin

### How to Sync

#### From Documentation to Plugin

1. **Verify the skill is finalized** in `skills/` directory
2. **Update the skill version** if applicable
3. **Copy the skill** to `../ringex-claude-plugin/skills/`
   ```bash
   cp -r skills/<skill-name> ../ringex-claude-plugin/skills/<skill-name>
   ```
4. **Test the skill** in the plugin environment
5. **Update plugin version** in `.claude-plugin/plugin.json` if significant changes were made
6. **Commit both repositories** with matching version references

#### From Plugin to Documentation

1. **Document the changes** made in the plugin
2. **Copy updated skill** back to documentation repository
   ```bash
   cp -r ../ringex-claude-plugin/skills/<skill-name> skills/<skill-name>
   ```
3. **Update documentation** if behavior or usage changed
4. **Verify the change** aligns with the current specification
5. **Commit both repositories** with cross-references

### Checklist for Skill Updates

Before syncing, ensure:

- [ ] Skill code has been tested
- [ ] Skill documentation (README, inline comments) is up-to-date
- [ ] Version numbers are consistent across repositories
- [ ] No breaking changes to the skill's public interface
- [ ] If API changes: update dependent skills that reference it
- [ ] Commit messages reference both repositories (if applicable)

## File Structure

### Skills Directory

```
skills/
├── call-followup-email/
├── call-recap/
├── colleague-lookup/
├── communications-brief/
├── fax-inbox/
├── manage-adaptive-cards/
├── manage-events/
├── manage-notes/
├── manage-tasks/
├── manage-teams/
├── manage-webhooks/
├── post-to-chat/
├── read-team-chat/
├── send-sms/
├── sms-inbox/
└── voicemail-inbox/
```

Each skill folder contains:
- `SKILL.md` — Skill specification and documentation
- Implementation files (varies by skill type)
- Tests (if applicable)

## Preventing Drift

To keep repositories in sync:

1. **Use a checklist** when making skill updates (see above)
2. **Link commits** across repositories in commit messages
   ```
   Update <skill-name>

   Sync with ringex-claude-plugin/<commit-hash>
   Related: ringcentral-mcp-docs/<commit-hash>
   ```
3. **Document breaking changes** in a CHANGELOG if skills are frequently updated
4. **Review before merge** — ensure changes are mirrored in both repos

## Versioning

- **Plugin version** (`plugin.json`): Incremented when plugin is released
- **Skill version**: Individual skills may have their own versioning if they're distributed separately
- **Keep these in sync** across repositories to avoid confusion

## Link Validation & Markdown Conversion

### The Hybrid Markdown Link Pattern

When converting HTML links to markdown format for mkdocs link validation, use the **hybrid approach** to preserve both styling and validation:

**Problem:** HTML href attributes don't get validated by mkdocs link validators. Markdown links do. But converting HTML to markdown breaks CSS styling and layout.

**Solution:** Keep the HTML structure visible, add hidden markdown links for validation:

```html
<a href="path/" class="rc-sol-card">
  <span class="rc-sol__icon">...</span>
  <div class="rc-sol__title">Title</div>
  <p class="rc-sol__desc">Description</p>
  <span class="rc-sol__link">Link text →</span>
  <div markdown="1" style="display: none;">
[Link text](path/)
  </div>
</a>
```

### How It Works

1. **Visible structure** — HTML `<a>` tag with `href` provides:
   - Proper CSS styling and layout
   - Clickable buttons and links
   - Click functionality for the card

2. **Hidden markdown** — `<div markdown="1" style="display: none;">` provides:
   - Markdown link syntax for mkdocs validation
   - Link checker compatibility
   - No visual impact (hidden with `display: none`)

3. **mkdocs processing** — The `md_in_html` extension (already enabled in `mkdocs.yml`):
   - Processes the hidden markdown content
   - Validates links in the markdown syntax
   - Doesn't render the hidden div visually

### When to Apply

Apply this pattern when:
- Converting HTML href links to support mkdocs link validation
- Keeping card/button styling is critical
- Both visual presentation and link validation are required

**Files already using this pattern:**
- `docs/solutions/index.md` — 6 cards
- `docs/solutions/claude.md` — 4 cards + links
- `docs/solutions/chatgpt.md` — 2 cards
- `docs/servers/index.md` — 4 server cards
- `docs/support.md` — 4 cards
- `docs/skills/index.md` — 16 skill cards
- `docs/servers/ringex-chat-setup.md` — 2 install cards
- `docs/servers/ringex-phone-setup.md` — 1 install card

### Implementation Checklist

When applying this pattern to new links:

- [ ] Identify the HTML link (`<a href="...">`) and its URL
- [ ] Extract the link text
- [ ] Add a hidden div before the closing `</a>` tag:
  ```html
  <div markdown="1" style="display: none;">
  [Link text](url)
  </div>
  ```
- [ ] Verify the page still renders correctly
- [ ] Verify mkdocs link validator picks up the markdown link
- [ ] Test that the HTML link is still clickable

## Questions or Issues?

If a skill update creates conflicts or inconsistencies:
1. Document the issue
2. Decide which repository is the source of truth for that skill
3. Update the other repository to match
4. Add a note in this file if it becomes a recurring issue
