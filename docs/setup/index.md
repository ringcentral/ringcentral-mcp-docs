---
title: Setup
description: Connect RingCentral MCP servers to your AI assistant.
hide:
  - toc
---

# Setup

Connect a RingCentral MCP server to your AI assistant in minutes. Choose your client below.

<div class="rc-solutions-grid">

  <a href="claude/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>
    </span>
    <div class="rc-sol__num">01</div>
    <div class="rc-sol__title">Claude</div>
    <p class="rc-sol__desc">Connect via Claude.ai Integrations or Claude Desktop Connectors. Supports all RingCentral MCP servers.</p>
    <span class="rc-sol__link">View instructions →</span>
  </a>

  <a href="chatgpt/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>
    </span>
    <div class="rc-sol__num">02</div>
    <div class="rc-sol__title">ChatGPT</div>
    <p class="rc-sol__desc">Connect via ChatGPT Connectors. Requires Pro, Team, Enterprise, or Edu subscription.</p>
    <span class="rc-sol__link">View instructions →</span>
  </a>

  <a href="codex/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8h16v10zm-2-1h-6v-2h6v2zM7.5 17l-1.41-1.41L8.67 13l-2.59-2.59L7.5 9l4 4-4 4z"/></svg>
    </span>
    <div class="rc-sol__num">03</div>
    <div class="rc-sol__title">Codex</div>
    <p class="rc-sol__desc">Connect via the Codex app's MCP Servers settings. Uses a dedicated server URL — see instructions.</p>
    <span class="rc-sol__link">View instructions →</span>
  </a>

</div>

---

## Server URLs

| Server | URL | Best for |
|--------|-----|----------|
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` | CRM contact lookup, call logging |
| RingCentral MCP | `https://mcp.labs.ringcentral.com/ringex` | RingCentral platform tools |

!!! note "Using Codex?"
    Codex uses a dedicated URL for the RingCentral MCP server — see the [Codex instructions](codex.md) for details.

---

!!! tip "Not sure which server to add?"
    Start with **App Connect** if you want to log calls and look up CRM contacts. Add **RingCentral MCP** if you want access to broader RingCentral platform tools. You can connect both.
