# Quickstart

Get connected to a RingCentral MCP server in under 5 minutes.

---

## Prerequisites

- A [RingCentral account](https://www.ringcentral.com) (free developer accounts available at [developers.ringcentral.com](https://developers.ringcentral.com))
- An MCP-compatible AI client: Claude Desktop, Claude.ai, Cursor, or Windsurf

---

## Step 1 — Choose a server

| Goal | Server |
|------|--------|
| Log calls to a CRM, look up contacts | [App Connect](../servers/app-connect.md) |
| Explore experimental RingCentral tools | [RC Labs MCP](../servers/rc-labs-mcp.md) |

---

## Step 2 — Add the server to your AI client

=== "Claude.ai"

    1. Go to **Settings → Integrations**
    2. Click **Add MCP Server**
    3. Paste the server URL:
       - App Connect: `https://unified-crm-extension.labs.ringcentral.com/mcp`
       - RC Labs: `https://mcp.labs.ringcentral.com`
    4. Click **Connect**
    5. Authenticate with RingCentral when prompted

=== "Claude Desktop"

    Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

    ```json
    {
      "mcpServers": {
        "app-connect": {
          "url": "https://unified-crm-extension.labs.ringcentral.com/mcp",
          "transport": "sse"
        },
        "rc-labs": {
          "url": "https://mcp.labs.ringcentral.com",
          "transport": "sse"
        }
      }
    }
    ```

    Restart Claude Desktop to apply changes.

=== "Cursor"

    Create or edit `.cursor/mcp.json` in your project root:

    ```json
    {
      "mcpServers": {
        "app-connect": {
          "url": "https://unified-crm-extension.labs.ringcentral.com/mcp"
        }
      }
    }
    ```

=== "Windsurf"

    Add to `~/.codeium/windsurf/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "app-connect": {
          "url": "https://unified-crm-extension.labs.ringcentral.com/mcp"
        }
      }
    }
    ```

---

## Step 3 — Verify the connection

Once connected, ask your AI assistant:

```
Check my RingCentral session status.
```

You should see your RingCentral username and CRM connection status returned.

---

## Step 4 — Connect your CRM (App Connect only)

If you're using App Connect and want to sync call logs or look up contacts:

1. Ask: *"What CRM platforms can I connect?"*
2. The assistant will list available connectors
3. Follow the OAuth flow to link your CRM account

Or see the full [Authentication guide](authentication.md).

---

## Step 5 — Try your first tool

```
Show me my RingCentral call logs from today.
```

```
Look up the contact "Jane Smith" in my CRM.
```

```
Log my last call with Jane Smith to Salesforce with the note: discussed renewal.
```

---

!!! success "You're set up!"
    Explore the [Tool Reference](../tools/app-connect/get-session-info.md) for all available tools, or follow the [CRM Integration Workflow](crm-workflow.md) guide for a real-world automation example.
