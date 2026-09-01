---
title: Servers
description: RingCentral MCP servers — tool references, integration guides, and setup instructions.
hide:
  - toc
---

# Servers

RingCentral currently publishes four active MCP servers. All implement the [Model Context Protocol](https://modelcontextprotocol.io) specification and are reachable over HTTPS using Server-Sent Events (SSE) transport.

<div class="rc-solutions-grid">

  <div class="rc-sol-card-wrap">
    <a href="ringex-phone/" class="rc-sol-card">
      <span class="rc-sol__icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.01-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.25 1.01l-2.2 2.21z"/></svg>
      </span>
      <div class="rc-sol__num">01</div>
      <div class="rc-sol__title">RingEX Phone</div>
      <p class="rc-sol__desc">Call logs, AI call notes, SMS, fax, and voicemail from the message store.</p>
      <span class="rc-sol__link">View server →</span>
    </a>
    <a href="https://chatgpt.com/plugins/plugin_asdk_app_6a5163accce48191ab3fac53d63cb197?q=ringcentral" class="rc-sol-card__badge" target="_blank" rel="noopener" title="Available as a ChatGPT plugin" aria-label="Open the RingCentral Phone ChatGPT plugin">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.7948.7948 0 0 0-.3927-.6813zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4536l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.6069 1.4997-2.602-1.4997Z"/></svg>
    </a>
  </div>

  <div class="rc-sol-card-wrap">
    <a href="ringex-chat/" class="rc-sol-card">
      <span class="rc-sol__icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>
      </span>
      <div class="rc-sol__num">02</div>
      <div class="rc-sol__title">RingEX Chat</div>
      <p class="rc-sol__desc">Team messaging (Glip): chats, direct conversations, teams, and posts.</p>
      <span class="rc-sol__link">View server →</span>
    </a>
    <a href="https://chatgpt.com/plugins/plugin_asdk_app_6a86209c4a088191bf0b16e16fd7db94" class="rc-sol-card__badge" target="_blank" rel="noopener" title="Available as a ChatGPT plugin" aria-label="Open the RingCentral Chat ChatGPT plugin">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.7948.7948 0 0 0-.3927-.6813zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4536l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.6069 1.4997-2.602-1.4997Z"/></svg>
    </a>
    <a href="https://claude.ai/directory/ringcentral-chat" class="rc-sol-card__badge rc-sol-card__badge--claude" target="_blank" rel="noopener" title="Available as a Claude connector" aria-label="Open the RingCentral Chat connector for Claude">
      <img src="../img/claude-icon.png" alt="Claude">
    </a>
  </div>

  <a href="ringex-admin/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94s-.02-.64-.07-.94l2.03-1.58a.5.5 0 0 0 .12-.64l-1.92-3.32a.5.5 0 0 0-.6-.22l-2.39.96a7.15 7.15 0 0 0-1.62-.94l-.36-2.54a.5.5 0 0 0-.5-.42h-3.84a.5.5 0 0 0-.5.42l-.36 2.54c-.59.24-1.13.56-1.62.94l-2.39-.96a.5.5 0 0 0-.6.22L2.7 8.68a.5.5 0 0 0 .12.64l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58a.5.5 0 0 0-.12.64l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32a.5.5 0 0 0-.12-.64zM12 15.6a3.6 3.6 0 1 1 0-7.2 3.6 3.6 0 0 1 0 7.2z"/></svg>
    </span>
    <div class="rc-sol__num">03</div>
    <div class="rc-sol__title">RingEX Admin</div>
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
| RingEX Phone | `https://mcp.labs.ringcentral.com/ringex/v1.1.0/phone` | 🟢 Preview | 12 |
| RingEX Chat | `https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat` | 🟢 Preview | 9 |
| RingEX Admin | `https://mcp.labs.ringcentral.com/ringex/admin` | 🟢 Preview | 26 |
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` | 🟡 Beta | 9 |

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

- **RingEX Phone / Chat / Admin** — no authentication required for tool discovery; most tools require a valid RingCentral session.
- **App Connect** — tools marked ⚠️ **REQUIRES CRM CONNECTION** require the user to have authenticated with both RingCentral and a supported CRM platform.

---

## Versioning policy

Labs servers follow a rolling-release model. Breaking changes will be announced in the [Changelog](../changelog.md) with at least 14 days notice. Stable tools are versioned via `api-version` query parameter where applicable.
