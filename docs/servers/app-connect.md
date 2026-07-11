# App Connect

**Endpoint:** `https://unified-crm-extension.labs.ringcentral.com/mcp`  
**Status:** 🟢 Available  
**Transport:** SSE over HTTPS  
**Tools:** 9

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

1. **RingCentral identity** — required for all tools. Uses OAuth 2.0 / SSO via your RingCentral account.
2. **CRM connection** — required for tools marked ⚠️ **REQUIRES CRM CONNECTION**. Users must link their CRM account via the App Connect portal.

See the [Setup guide](app-connect-setup.md) for step-by-step connection instructions.

---

## Tool summary

| Tool | CRM Required | Description |
|------|:---:|-------------|
| [`getSessionInfo`](../tools/app-connect/get-session-info.md) | — | Current user identity and CRM connection status |
| [`getPublicConnectors`](../tools/app-connect/get-public-connectors.md) | — | List available CRM connectors |
| [`getHelp`](../tools/app-connect/get-help.md) | — | Quick integration guide |
| [`findContactByName`](../tools/app-connect/find-contact-by-name.md) | ⚠️ | Search CRM contacts by name |
| [`findContactByPhone`](../tools/app-connect/find-contact-by-phone.md) | ⚠️ | Search CRM contacts by phone number |
| [`createContact`](../tools/app-connect/create-contact.md) | ⚠️ | Create a new CRM contact |
| [`createCallLog`](../tools/app-connect/create-call-log.md) | ⚠️ | Log a call activity to the CRM |
| [`rcGetCallLogs`](../tools/app-connect/rc-get-call-logs.md) | ⚠️ | Retrieve call logs from RingCentral |
| [`logout`](../tools/app-connect/logout.md) | — | Sign out from the CRM session |
