---
title: App Connect Setup
description: Connect the App Connect MCP server to Claude, ChatGPT, or Codex, and link your CRM.
---

# App Connect Setup

**Server URL:** `https://unified-crm-extension.labs.ringcentral.com/mcp`

---

=== "Claude"

    Custom connectors live under **Customize > Connectors** (Claude.ai) or **Settings → Connectors** (Claude Desktop) — not through `claude_desktop_config.json`, which only supports local stdio servers.

    1. Sign in to [claude.ai](https://claude.ai), or open Claude Desktop.
    2. **Pro/Max:** go to **Customize > Connectors** → click **+** → **Add custom connector**. **Team/Enterprise:** an Owner first adds it under **Organization settings > Connectors** → **Add** → hover **Custom** → select **Web**; members then connect individually via **Customize > Connectors**.
    3. Enter a name (e.g. `RingCentral App Connect`) and the URL above, then click **Add**.
    4. Complete the RingCentral OAuth flow, then authenticate with your CRM when prompted.
    5. In a new conversation, click the **+** button (lower left of the chat box) → **Connectors**, and toggle App Connect on.
    6. Verify: ask "Check my RingCentral session status."

=== "ChatGPT"

    ChatGPT calls this an **App** (renamed from "Connector" in December 2025). Connecting a server that can call tools — not just read/fetch — requires Developer Mode.

    1. **Business/Enterprise/Edu workspaces:** a workspace admin enables Developer Mode via **Workspace Settings → Permissions & Roles → Connected Data**. **Individual Enterprise/Edu accounts, or Pro (read/fetch-only):** go to **Settings → Apps → Advanced Settings** and toggle **Developer mode** on.
    2. In **Settings → Apps**, click **Create**, enter the URL above as the MCP Server URL, name it (e.g. `RingCentral App Connect`), click **Scan Tools**, then **Save**.
    3. Complete the RingCentral OAuth flow, then authenticate with your CRM when prompted.
    4. Open a new chat, click the **+** icon or tools menu, and select App Connect — or mention it by name in your prompt.
    5. Verify: ask "Check my RingCentral session status."

    !!! note "Pro users"
        With read/fetch-only Developer Mode, you can look up CRM contacts and call logs, but can't create contacts or log calls.

=== "Codex"

    1. Open the Codex app → click the **Settings** gear (bottom left) → **MCP Servers** → **Add server**.
    2. Enter a name (e.g. `RingCentral App Connect`), set Type to **Streamable HTTP**, and enter the URL above.
    3. Click **Save**, then select **Restart** so Codex picks up the new server.
    4. Authenticate with your RingCentral account, then your CRM, in the browser windows that open.
    5. Codex has no connector picker — mention "RingCentral" explicitly in your prompt, e.g. "Using RingCentral, check my session status."

---

## Connect your CRM

Once App Connect is active in a conversation:

1. Ask: *"What CRM platforms can I connect?"*
2. Your assistant will display the available connectors
3. Click through the OAuth flow to link your CRM account

Supported platforms include Salesforce, HubSpot, Zoho, and others. See [`getPublicConnectors`](../tools/app-connect/get-public-connectors.md) for the full list.

---

## Troubleshooting

**Tools not appearing after connecting**

- Confirm the URL has no trailing slash.
- Disconnect and reconnect the server from your client's connector/app settings.
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`.

**Authentication errors**

- Remove the connector/app and re-add it to restart the OAuth flow.
- Ensure your RingCentral account has the necessary API permissions.

**CRM tools returning errors**

- Ask: *"What is my session status?"* — if `crmConnected` is `false`, re-link your CRM by asking *"What CRM platforms can I connect?"*

---

[← Back to App Connect](app-connect.md)
