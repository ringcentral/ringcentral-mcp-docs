---
title: RingEX Meetings Setup
description: Connect the RingEX Meetings MCP server to ChatGPT, Claude, or Codex.
---

# RingEX Meetings Setup

**Server URL:** `https://mcp.labs.ringcentral.com/ringex/video`

!!! warning "Experimental server"
    RingEX Meetings is experimental, and there is no official plugin or connector for it yet — add it manually using the steps below. The endpoint and tool surface may change without notice.

!!! note "Endpoint path still says `video`"
    The server is named RingEX Meetings, but it is deployed at `…/ringex/video`. Enter the URL exactly as shown above — `…/ringex/meetings` will not resolve.

---

=== "ChatGPT"

    ChatGPT calls this an **App** (renamed from "Connector" in December 2025). Connecting a server that can call tools — not just read/fetch — requires Developer Mode.

    1. **Business/Enterprise/Edu workspaces:** a workspace admin enables Developer Mode via **Workspace Settings → Permissions & Roles → Connected Data**. **Individual Enterprise/Edu accounts, or Pro (read/fetch-only):** go to **Settings → Apps → Advanced Settings** and toggle **Developer mode** on.
    2. In **Settings → Apps**, click **Create**, enter the URL above as the MCP Server URL, name it (e.g. `RingEX Meetings`), click **Scan Tools**, then **Save**.
    3. Complete the RingCentral OAuth flow when prompted.
    4. Open a new chat, click the **+** icon or tools menu, and select RingEX Meetings — or mention it by name in your prompt.
    5. Verify: ask "List my RingCentral meetings from the last week."

    !!! note "Pro users"
        With read/fetch-only Developer Mode, the six read tools work — meeting history, summaries, transcripts, chat, and recordings. You won't be able to create or delete meeting spaces.

=== "Claude"

    Custom connectors live under **Customize > Connectors** (Claude.ai) or **Settings → Connectors** (Claude Desktop) — not through `claude_desktop_config.json`, which only supports local stdio servers.

    1. Sign in to [claude.ai](https://claude.ai), or open Claude Desktop.
    2. **Pro/Max:** go to **Customize > Connectors** → click **+** → **Add custom connector**. **Team/Enterprise:** an Owner first adds it under **Organization settings > Connectors** → **Add** → hover **Custom** → select **Web**; members then connect individually via **Customize > Connectors**.
    3. Enter a name (e.g. `RingEX Meetings`) and the URL above, then click **Add**.
    4. Complete the RingCentral OAuth flow: sign in with your RingCentral account and authorize the integration.
    5. In a new conversation, click the **+** button (lower left of the chat box) → **Connectors**, and toggle RingEX Meetings on.
    6. Verify: ask "List my RingCentral meetings from the last week."

=== "Codex"

    1. Open the Codex app → click the **Settings** gear (bottom left) → **MCP Servers** → **Add server**.
    2. Enter a name (e.g. `RingEX Meetings`), set Type to **Streamable HTTP**, and enter the URL above.
    3. Click **Save**, then select **Restart** so Codex picks up the new server.
    4. Authenticate with your RingCentral account in the browser window that opens.
    5. Codex has no connector picker — mention "RingCentral" explicitly in your prompt, e.g. "Using RingCentral, list my meetings from the last week."

---

## Verifying the connection

A good first prompt exercises the entry-point tool without pulling any meeting content:

```
List my RingCentral meetings from the last week.
```

Your assistant should call `search_meeting_history` with a date range and return compact meeting metadata. If it returns an empty list, widen the date range before assuming the connection is broken — this server only sees meetings you have access to, and `search_meeting_history` requires both `dateFrom` and `dateTo`.

---

## Troubleshooting

**Tools not appearing after connecting**

- Confirm the URL has no trailing slash, and that the path is `/ringex/video` — not `/ringex/meetings`.
- Disconnect and reconnect the server from your client's connector/app settings.
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`.

**Authentication errors**

- Remove the connector/app and re-add it to restart the OAuth flow.
- Ensure your RingCentral account has the necessary API permissions.

**No meetings returned**

- Widen the date range. Both `dateFrom` and `dateTo` are required, so an overly narrow default window will return nothing.
- This server is scoped to the authenticated user — meetings you weren't a participant in won't appear.

**A transcript, chat, or recording comes back empty**

- The artifact may not exist. Transcript, chat, and recording content is only produced when those features were enabled for the meeting. Ask for the meeting summary first — it reports which artifacts are actually available.

**Transcript or chat looks cut off**

- Both cap output, defaulting to 20,000 characters. Ask for up to 50,000 for a long meeting.

---

[← Back to RingEX Meetings](ringex-meetings.md)
