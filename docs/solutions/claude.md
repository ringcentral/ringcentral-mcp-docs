---
title: Claude solutions for RingCentral
description: RingCentral resource center for Claude — connectors, plugins, and setup guides.
---

# Claude solutions for RingCentral

<p align="center">
  <img src="../../assets/logo-claude.png" alt="Claude logo" style="height:56px;width:auto;margin:1.5rem 0 2rem;">
</p>

This page is the resource center for using RingCentral with Claude — every connector and plugin available today, what's coming next, and how to install them.

## Run your business in one chat

<div class="rc-banner-promo" style="background: linear-gradient(135deg, #FF6B35 0%, #8B5CF6 100%); border-radius: 8px; padding: 1.5rem 2rem; margin: 2rem 0; color: white; box-shadow: 0 8px 20px rgba(255, 107, 53, 0.15);">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.3rem; font-weight: 600;">Claude for Small Business + RingCentral</h3>
      <p style="margin: 0; font-size: 0.95rem; opacity: 0.95;">Connect your phone, team chat, and CRM—15-minute setup.</p>
    </div>
    <a href="../claude-small-business/" style="display: inline-block; background: white; color: #FF6B35; padding: 0.5rem 1.25rem; border-radius: 6px; font-weight: 600; text-decoration: none; white-space: nowrap; margin-left: 1.5rem;">
      Setup guide →
    </a>
  </div>
</div>

## Connectors & plugins

<div class="rc-solutions-grid rc-solutions-grid--iconbadge">

  <a href="https://claude.ai/directory/ringcentral-chat" class="rc-sol-card" target="_blank" rel="noopener">
    <span class="rc-sol__icon"><i class="fa-solid fa-comment-dots"></i></span>
    <div class="rc-sol__title">RingCentral Chat connector</div>
    <p class="rc-sol__desc">Team messaging in Claude — catch up on chats, search history, and post updates on your behalf.</p>
    <span class="rc-sol__link">Set up →</span>
    <div markdown="1" style="display: none;">
[Claude Chat Connector](https://claude.ai/directory/ringcentral-chat)
    </div>
  </a>

  <div class="rc-sol-card rc-sol-card--disabled">
    <span class="rc-sol__icon"><i class="fa-solid fa-phone"></i></span>
    <div class="rc-sol__title">RingCentral Phone connector</div>
    <p class="rc-sol__desc">Call logs, AI call notes, SMS, fax, and voicemail — directly inside Claude.</p>
    <span class="rc-sol__link rc-sol__link--disabled">Coming soon</span>
    <a href="../../servers/ringex-phone-setup/#tab-Claude" class="rc-sol__link">Install the connector manually →<div markdown="1" style="display: none;">
[RingEx Phone Setup](../../servers/ringex-phone-setup/#tab-Claude)
</div></a>
  </div>

  <div class="rc-sol-card">
    <span class="rc-sol__icon"><i class="fa-solid fa-puzzle-piece"></i></span>
    <div class="rc-sol__title">RingCentral Plugin</div>
    <p class="rc-sol__desc">A bundled Claude Code / Cowork plugin with RingCentral skills — SMS, voicemail, call recaps, colleague lookup, and more.</p>
    <div style="display: flex; gap: 0.75rem;">
      <a href="https://claude.ai/customize/plugins/id/2cc3de0a-bd3d-4a5d-8a54-98097cc05689%40anthropic-plugin-directory" target="_blank" rel="noopener" class="rc-sol__link" style="flex: 1;">Install →<div markdown="1" style="display: none;">
[Claude Plugin Directory](https://claude.ai/customize/plugins/id/2cc3de0a-bd3d-4a5d-8a54-98097cc05689%40anthropic-plugin-directory)
</div></a>
      <a href="../../downloads/ringcentral-plugin.zip" download class="rc-sol__link" style="flex: 1;">Download →<div markdown="1" style="display: none;">
[RingCentral Plugin Download](../../downloads/ringcentral-plugin.zip)
</div></a>
    </div>
  </div>

  <a href="../../downloads/appconnect-connector-skills.zip" download class="rc-sol-card">
    <span class="rc-sol__icon"><i class="fa-solid fa-plug"></i></span>
    <div class="rc-sol__title">App Connect Developer Plugin</div>
    <p class="rc-sol__desc">Skills for building your own App Connect CRM connector — scaffolding, auth, contact matching, call logging, and deploy.</p>
    <span class="rc-sol__link">Download →</span>
    <div markdown="1" style="display: none;">
[App Connect Developer Plugin](../../downloads/appconnect-connector-skills.zip)
    </div>
  </a>

</div>

## Installing a plugin manually

Once you have a plugin's `.zip` file, install it directly in Claude:

1. Go to **Settings**.
2. Click **Plugins**.
3. From the pull-down, select **Upload plugin**.
4. Select the plugin `.zip` file.
5. Presto!

## More resources

- [RingEX Chat setup guide](../servers/ringex-chat-setup.md) — full walkthrough for adding the Chat connector to Claude.ai or Claude Desktop.
- [RingEX Phone setup guide](../servers/ringex-phone-setup.md) — server details for when the Phone connector ships.
- [App Connect setup guide](../servers/app-connect-setup.md) — connect the App Connect MCP server and link your CRM.
- [Solutions overview](index.md) — browse all use cases powered by RingCentral's MCP servers.
