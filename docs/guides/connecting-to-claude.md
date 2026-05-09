# Connecting to Claude

This guide covers how to connect RingCentral MCP servers specifically to Anthropic's Claude products: Claude.ai and Claude Desktop.

---

## Claude.ai (web & mobile)

Claude.ai supports MCP servers through the **Integrations** settings panel.

### Adding a server

1. Open [claude.ai](https://claude.ai) and sign in
2. Click your avatar → **Settings**
3. Navigate to **Integrations**
4. Click **Add integration** or **Connect more tools**
5. Enter the server URL and a display name:

    | Field | Value |
    |-------|-------|
    | Name | `RingCentral App Connect` |
    | URL | `https://unified-crm-extension.labs.ringcentral.com/mcp` |

6. Click **Connect**
7. Complete the RingCentral OAuth flow if prompted

### Using tools in a conversation

Once connected, Claude will automatically have access to the server's tools. You can invoke them naturally:

> *"Look up Jane Smith in my CRM and log a call saying we discussed the Q3 renewal."*

To see which tools are available, ask:

> *"What RingCentral tools do you have access to?"*

---

## Claude Desktop

Claude Desktop uses a local JSON config file to register MCP servers.

### Config file location

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

### Configuration

```json
{
  "mcpServers": {
    "rc-app-connect": {
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

After saving, **restart Claude Desktop** for the changes to take effect.

### Verifying the connection

In a new Claude Desktop conversation, look for the 🔌 **Tools** indicator in the input bar. Click it to see connected servers and available tools.

---

## Troubleshooting

### Tools not appearing

- Confirm the server URL is correct (no trailing slash)
- Restart the client after config changes
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`

### Authentication errors

- Re-authenticate: go to Settings → Integrations → disconnect and reconnect the server
- Ensure your RingCentral account has the necessary permissions (see [Authentication](authentication.md))

### CRM tools returning errors

- Call `getSessionInfo` to check CRM connection status
- If `crmConnected: false`, re-link your CRM from the App Connect portal

---

!!! tip
    If you're evaluating MCP for your team, the [Quickstart guide](quickstart.md) has the fastest path to a working demo.
