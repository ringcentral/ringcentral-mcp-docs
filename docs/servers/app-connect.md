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

=== "Claude Desktop (Settings → Connectors)"

    Remote MCP servers cannot be added to `claude_desktop_config.json`. Use the Connectors UI instead:

    1. Open Claude Desktop → **Settings → Connectors**
    2. Click **Add connector**
    3. Enter URL: `https://unified-crm-extension.labs.ringcentral.com/mcp`
    4. Click **Connect**
    5. Authenticate with RingCentral when prompted
    6. Authenticate with your CRM when prompted

=== "Claude.ai (Settings → Integrations)"

    1. Open **Settings → Integrations → Add MCP Server**
    2. Enter URL: `https://unified-crm-extension.labs.ringcentral.com/mcp`
    3. Click **Connect**
    4. Authenticate with RingCentral when prompted
    5. Authenticate with your CRM when prompted

=== "Cursor"

    ```json
    {
      "mcpServers": {
        "appconnect": {
          "url": "https://unified-crm-extension.labs.ringcentral.com/mcp",
          "type": "http"
        }
      }
    }
    ```

---

## Authentication

This server uses a **two-layer auth** model:

1. **RingCentral identity** — required for all tools. Uses OAuth 2.0 / SSO via your RingCentral account.
2. **CRM connection** — required for tools marked ⚠️ **REQUIRES CRM CONNECTION**. Users must link their CRM account via the App Connect portal.

See the [Setup guide](../setup/claude.md) for step-by-step connection instructions.

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
