---
title: RingEX Admin Setup
description: Connect the RingEX Admin MCP server to ChatGPT, Claude, or Codex.
---

# RingEX Admin Setup

**Server URL:** `https://mcp.labs.ringcentral.com/ringex/admin`

---

=== "ChatGPT"

    ChatGPT calls this an **App** (renamed from "Connector" in December 2025). Connecting a server that can call tools — not just read/fetch — requires Developer Mode.

    1. **Business/Enterprise/Edu workspaces:** a workspace admin enables Developer Mode via **Workspace Settings → Permissions & Roles → Connected Data**. **Individual Enterprise/Edu accounts, or Pro (read/fetch-only):** go to **Settings → Apps → Advanced Settings** and toggle **Developer mode** on.
    2. In **Settings → Apps**, click **Create**, enter the URL above as the MCP Server URL, name it (e.g. `RingEX Admin`), click **Scan Tools**, then **Save**.
    3. Complete the RingCentral OAuth flow when prompted.
    4. Open a new chat, click the **+** icon or tools menu, and select RingEX Admin — or mention it by name in your prompt.
    5. Verify: ask "What's my RingCentral extension and presence status?"

    !!! note "Pro users"
        With read/fetch-only Developer Mode, most Admin tools already work since this server is largely read-oriented (extension, presence, directory, discovery).

=== "Claude"

    Custom connectors live under **Customize > Connectors** (Claude.ai) or **Settings → Connectors** (Claude Desktop) — not through `claude_desktop_config.json`, which only supports local stdio servers.

    1. Sign in to [claude.ai](https://claude.ai), or open Claude Desktop.
    2. **Pro/Max:** go to **Customize > Connectors** → click **+** → **Add custom connector**. **Team/Enterprise:** an Owner first adds it under **Organization settings > Connectors** → **Add** → hover **Custom** → select **Web**; members then connect individually via **Customize > Connectors**.
    3. Enter a name (e.g. `RingEX Admin`) and the URL above, then click **Add**.
    4. Complete the RingCentral OAuth flow: sign in with your RingCentral account and authorize the integration.
    5. In a new conversation, click the **+** button (lower left of the chat box) → **Connectors**, and toggle RingEX Admin on.
    6. Verify: ask "What's my RingCentral extension and presence status?"

=== "Codex"

    1. Open the Codex app → click the **Settings** gear (bottom left) → **MCP Servers** → **Add server**.
    2. Enter a name (e.g. `RingEX Admin`), set Type to **Streamable HTTP**, and enter the URL above.
    3. Click **Save**, then select **Restart** so Codex picks up the new server.
    4. Authenticate with your RingCentral account in the browser window that opens.
    5. Codex has no connector picker — mention "RingCentral" explicitly in your prompt, e.g. "Using RingCentral, what's my extension and presence status?"

---

## Troubleshooting

**Tools not appearing after connecting**

- Confirm the URL has no trailing slash.
- Disconnect and reconnect the server from your client's connector/app settings.
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`.

**Authentication errors**

- Remove the connector/app and re-add it to restart the OAuth flow.
- Ensure your RingCentral account has the necessary API permissions.

---

[← Back to RingEX Admin](ringex-admin.md)
