---
title: Servers
description: RingCentral MCP servers — tool references, integration guides, and setup instructions.
hide:
  - toc
---

# Servers

RingCentral currently publishes four active MCP servers. All implement the [Model Context Protocol](https://modelcontextprotocol.io) specification and are reachable over HTTPS using Server-Sent Events (SSE) transport.

<div class="rc-solutions-grid">

  <a href="ringex-phone/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.01-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.25 1.01l-2.2 2.21z"/></svg>
    </span>
    <div class="rc-sol__num">01</div>
    <div class="rc-sol__title">RingEx Phone</div>
    <p class="rc-sol__desc">Call logs, AI call notes, SMS, fax, and voicemail from the message store.</p>
    <span class="rc-sol__link">View server →</span>
  </a>

  <a href="ringex-chat/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>
    </span>
    <div class="rc-sol__num">02</div>
    <div class="rc-sol__title">RingEx Chat</div>
    <p class="rc-sol__desc">Team messaging (Glip): chats, direct conversations, teams, and posts.</p>
    <span class="rc-sol__link">View server →</span>
  </a>

  <a href="ringex-admin/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94s-.02-.64-.07-.94l2.03-1.58a.5.5 0 0 0 .12-.64l-1.92-3.32a.5.5 0 0 0-.6-.22l-2.39.96a7.15 7.15 0 0 0-1.62-.94l-.36-2.54a.5.5 0 0 0-.5-.42h-3.84a.5.5 0 0 0-.5.42l-.36 2.54c-.59.24-1.13.56-1.62.94l-2.39-.96a.5.5 0 0 0-.6.22L2.7 8.68a.5.5 0 0 0 .12.64l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58a.5.5 0 0 0-.12.64l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32a.5.5 0 0 0-.12-.64zM12 15.6a3.6 3.6 0 1 1 0-7.2 3.6 3.6 0 0 1 0 7.2z"/></svg>
    </span>
    <div class="rc-sol__num">03</div>
    <div class="rc-sol__title">RingEx Admin</div>
    <p class="rc-sol__desc">Tool discovery, generic API dispatch, extension, presence, and directory search.</p>
    <span class="rc-sol__link">View server →</span>
  </a>

  <a href="app-connect/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>
    </span>
    <div class="rc-sol__num">04</div>
    <div class="rc-sol__title">App Connect</div>
    <p class="rc-sol__desc">Bridges RingCentral telephony with your connected CRM — contacts, call logging, and more.</p>
    <span class="rc-sol__link">View server →</span>
  </a>

</div>

---

## Server registry

| Server | URL | Status | Tools |
|--------|-----|--------|-------|
| RingEx Phone | `https://mcp.labs.ringcentral.com/ringex/phone` | 🟡 Labs / Beta · New | 24 |
| RingEx Chat | `https://mcp.labs.ringcentral.com/ringex/team-chat` | 🟡 Labs / Beta · New | 65 |
| RingEx Admin | `https://mcp.labs.ringcentral.com/ringex/admin` | 🟡 Labs / Beta · New | 26 |
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` | 🟢 Available | 9 |

---

## Transport & protocol

Both servers use **SSE (Server-Sent Events)** transport over HTTPS, which is the recommended transport for remote MCP servers. Clients connect by sending an HTTP `POST` to the server URL with a JSON-RPC 2.0 body.

```bash
# Discover tools on any server
curl -X POST https://<server-url> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

---

## Authentication model

- **RingEx Phone / Chat / Admin** — no authentication required for tool discovery; most tools require a valid RingCentral session.
- **App Connect** — tools marked ⚠️ **REQUIRES CRM CONNECTION** require the user to have authenticated with both RingCentral and a supported CRM platform.

---

## Versioning policy

Labs servers follow a rolling-release model. Breaking changes will be announced in the [Changelog](../changelog.md) with at least 14 days notice. Stable tools are versioned via `api-version` query parameter where applicable.
