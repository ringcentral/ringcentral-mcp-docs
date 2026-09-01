# App Connect

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://unified-crm-extension.labs.ringcentral.com/mcp</code><button class="rc-copy" data-copy="https://unified-crm-extension.labs.ringcentral.com/mcp" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--beta">Beta</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

---

## About

The App Connect MCP server bridges **RingCentral telephony** with your connected **CRM platform**. It enables AI assistants to look up contacts, create CRM records, and sync call activity — all through natural language.

Supported CRM platforms include Salesforce, HubSpot, Zoho, and others supported by the RingCentral App Connect product.

---

## Connecting

See the [App Connect Setup guide](app-connect-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex — including how to link your CRM.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Authentication

This server uses a **two-layer auth** model:

1. **RingCentral identity** — required for all tools. Uses OAuth 2.0 / SSO via your RingCentral account, established when you add the server to your AI client.
2. **CRM connection** — required for tools marked ⚠️ **REQUIRES CRM CONNECTION**. Linked separately via the **App Connect Chrome extension**, not inside the AI client. Once linked, App Connect remembers the session and any connected AI client auto-detects it.

Only **one CRM can be connected at a time** per RingCentral account — App Connect intermediates that connection, so switching CRMs requires disconnecting the current one first.

See the [Setup guide](app-connect-setup.md) for step-by-step connection instructions, including the recommended order of operations.

!!! tip "Already have a CRM-specific MCP server?"
    Some CRMs publish their own dedicated MCP servers with deeper, CRM-specific functionality. App Connect is most valuable when your CRM doesn't yet support MCP natively — evaluate both if your CRM has a dedicated option.

---

## Available tools

9 tools are available on this server.

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`getSessionInfo`](../tools/app-connect.md#getsessioninfo) | — | Current user identity and CRM connection status |
| [`getPublicConnectors`](../tools/app-connect.md#getpublicconnectors) | — | List available CRM connectors |
| [`getHelp`](../tools/app-connect.md#gethelp) | — | Quick integration guide |
| [`findContactByName`](../tools/app-connect.md#findcontactbyname) | ⚠️ | Search CRM contacts by name |
| [`findContactByPhone`](../tools/app-connect.md#findcontactbyphone) | ⚠️ | Search CRM contacts by phone number |
| [`createContact`](../tools/app-connect.md#createcontact) | ⚠️ | Create a new CRM contact |
| [`createCallLog`](../tools/app-connect.md#createcalllog) | ⚠️ | Log a call activity to the CRM |
| [`rcGetCallLogs`](../tools/app-connect.md#rcgetcalllogs) | ⚠️ | Retrieve call logs from RingCentral |
| [`logout`](../tools/app-connect.md#logout) | — | Sign out from the CRM session |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client, following the [Setup guide](app-connect-setup.md).
2. **Verify** — Ask your assistant to check your RingCentral session status to confirm the connection is active.
3. **Use** — Link your CRM, then ask your AI assistant to look up contacts, create records, or log call activity. Tools marked ⚠️ require an active CRM connection.

---

## Tool discovery

```bash
curl -X POST https://unified-crm-extension.labs.ringcentral.com/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
