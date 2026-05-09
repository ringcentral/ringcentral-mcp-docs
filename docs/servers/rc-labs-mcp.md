# RingCentral Labs MCP

**Endpoint:** `https://mcp.labs.ringcentral.com`  
**Status:** 🟡 Labs / Beta  
**Transport:** SSE over HTTPS

---

## About

The RingCentral Labs MCP server is the experimental home for new platform capabilities built by the RingCentral Labs engineering team. Tools published here are under active development and subject to change.

!!! warning "Labs status"
    Tools on this server are not covered by RingCentral's standard SLA. They may be renamed, modified, or removed without prior notice. Use in production with caution.

---

## Connecting

=== "Claude Desktop (claude_desktop_config.json)"

    ```json
    {
      "mcpServers": {
        "rc-labs": {
          "url": "https://mcp.labs.ringcentral.com",
          "transport": "sse"
        }
      }
    }
    ```

=== "Claude.ai (Settings → Integrations)"

    1. Open **Settings → Integrations → Add MCP Server**
    2. Enter URL: `https://mcp.labs.ringcentral.com`
    3. Click **Connect**

=== "Cursor"

    Add to `.cursor/mcp.json` in your project root:

    ```json
    {
      "mcpServers": {
        "rc-labs": {
          "url": "https://mcp.labs.ringcentral.com"
        }
      }
    }
    ```

---

## Tool discovery

```bash
curl -X POST https://mcp.labs.ringcentral.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

---

## Roadmap

The Labs MCP server roadmap includes upcoming tools for:

- **RingCentral AI Noise Cancellation** — expose transcription and noise-cancel status
- **Analytics & Reporting** — pull QoS and usage metrics for a RingCentral account
- **Video Meetings** — create, list, and summarize RingCentral Video meetings
- **SMS & Messaging** — send and receive SMS programmatically

Follow the [Changelog](../changelog.md) for release announcements.
