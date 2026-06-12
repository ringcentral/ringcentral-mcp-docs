---
title: Connect to Codex
description: Connect RingCentral MCP servers to the Codex app.
---

# Connect to Codex

The Codex app supports remote MCP servers through its **MCP Servers** settings. Once connected and authenticated, RingCentral tools are available in your Codex sessions.

---

## Server URLs

| Server | URL |
|--------|-----|
| RingCentral MCP | `https://mcp.labs.ringcentral.com/ringex` |

---

## Setup

=== "Step 1 — Open MCP Servers"

    1. Open the Codex app
    2. Click **Settings** (bottom left) → **Settings**
    3. Navigate to **MCP Servers**
    4. Click **Add server**

=== "Step 2 — Add the server"

    Fill in the server details and click **Save**:

    | Field | Value |
    |-------|-------|
    | Name | `RingCentral MCP` (any name works) |
    | Type | **Streamable HTTP** |
    | URL | `https://mcp.labs.ringcentral.com/ringex` |

    After saving, Codex returns you to the MCP server list automatically.

=== "Step 3 — Authenticate"

    1. Click **Authenticate** on the server you just added
    2. Sign in with your RingCentral account in the browser window that opens
    3. Authorize the integration

=== "Step 4 — Verify"

    In a new session, ask:

    ```
    Using RingCentral, show my extension profile.
    ```

    You should see your RingCentral extension details returned.

---

## Telling Codex to use RingCentral tools

Unlike ChatGPT or Claude, Codex has no picker to nominate a specific MCP tool for a conversation. Codex infers which of its enabled MCP servers to use from your prompt alone.

Mention RingCentral explicitly so Codex picks the right tools:

```
Using RingCentral, show me my call logs from today.
```

```
This is a RingCentral task — list my team messaging chats.
```

If Codex keeps reaching for other tools, add more context (e.g. *"use the RingCentral MCP server"*) or temporarily disable other MCP servers in **Settings → MCP Servers**.

---

## Troubleshooting

**Server changes not taking effect**

- Codex can get stuck and fail to refresh its MCP configuration after you add or edit a server. Close and re-open the Codex app to force a refresh.

**Codex not using RingCentral tools**

- Mention RingCentral explicitly in your prompt — Codex selects tools by inference, not by attachment
- Temporarily disable other MCP servers to reduce ambiguity

**Authentication errors**

- Re-run **Authenticate** from the MCP server list
- Remove the server, re-add it, and authenticate again to restart the OAuth flow
- Ensure your RingCentral account has the necessary API permissions
