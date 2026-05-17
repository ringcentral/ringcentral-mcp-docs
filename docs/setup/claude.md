---
title: Connect to Claude
description: Connect RingCentral MCP servers to Claude.ai or Claude Desktop.
---

# Connect to Claude

RingCentral MCP servers work with both Claude.ai (web and mobile) and Claude Desktop. Remote servers are added through the UI in both cases — not through configuration files.

---

## Server URLs

| Server | URL |
|--------|-----|
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` |
| RingCentral MCP | `https://mcp.labs.ringcentral.com/ringex` |

---

## Claude.ai

=== "Step 1 — Open Integrations"

    1. Sign in to [claude.ai](https://claude.ai)
    2. Click your avatar (top right) → **Settings**
    3. Navigate to **Integrations**
    4. Click **Add integration**

=== "Step 2 — Add a server"

    Enter the server details and click **Connect**:

    | Field | Value |
    |-------|-------|
    | Name | `RingCentral App Connect` |
    | URL | `https://unified-crm-extension.labs.ringcentral.com/mcp` |

    Repeat to add the RingCentral MCP server if needed:

    | Field | Value |
    |-------|-------|
    | Name | `RingCentral MCP` |
    | URL | `https://mcp.labs.ringcentral.com/ringex` |

=== "Step 3 — Authenticate"

    Complete the RingCentral OAuth flow when prompted. You will be asked to:

    1. Sign in with your RingCentral account
    2. Authorize the integration

=== "Step 4 — Verify"

    In a new conversation, ask:

    ```
    Check my RingCentral session status.
    ```

    You should see your RingCentral username and CRM connection status returned.

---

## Claude Desktop

Remote MCP servers are added through **Settings → Connectors** — not through `claude_desktop_config.json`, which only supports local stdio servers.

=== "Step 1 — Open Connectors"

    1. Open Claude Desktop
    2. Click the menu → **Settings**
    3. Navigate to **Connectors**
    4. Click **Add connector**

=== "Step 2 — Add a server"

    Enter the URL and click **Connect**:

    - `https://unified-crm-extension.labs.ringcentral.com/mcp`

    Repeat to add the second server if needed:

    - `https://mcp.labs.ringcentral.com/ringex`

=== "Step 3 — Authenticate"

    Complete the RingCentral OAuth flow in the browser window that opens.

=== "Step 4 — Verify"

    In a new conversation, look for the 🔌 **Tools** indicator in the message input bar. Click it to confirm the servers are listed.

    Then ask:

    ```
    Check my RingCentral session status.
    ```

---

## Connect your CRM

Once the server is connected, link your CRM to enable contact lookup and call logging:

1. Ask: *"What CRM platforms can I connect?"*
2. The assistant will display available connectors
3. Click through the OAuth flow to link your CRM account

Supported platforms include Salesforce, HubSpot, Zoho, and others. See [`getPublicConnectors`](../tools/app-connect/get-public-connectors.md) for the full list.

---

## Adding a local stdio server

If you need to add a **local** MCP server (one that runs as a process on your machine), you can use `claude_desktop_config.json`:

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

```json
{
  "mcpServers": {
    "my-local-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-package"]
    }
  }
}
```

Restart Claude Desktop after saving.

---

## Troubleshooting

**Tools not appearing after connecting**

- Confirm the URL has no trailing slash
- Disconnect and reconnect the server from Settings → Connectors
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`

**Authentication errors**

- Go to Settings → Connectors → disconnect and reconnect
- Ensure your RingCentral account has the necessary API permissions

**CRM tools returning errors**

- Ask: *"What is my session status?"* — if `crmConnected` is `false`, re-link your CRM
- Re-authenticate via Settings → Connectors — disconnect and reconnect the server
