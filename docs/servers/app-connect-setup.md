---
title: App Connect Setup
description: Connect the App Connect MCP server to Claude, ChatGPT, or Codex, and link your CRM.
---

# App Connect Setup

**Server URL:** `https://unified-crm-extension.labs.ringcentral.com/mcp`

---

## How authentication works

App Connect sits between your AI client and your CRM, so it has **two independent layers of auth**. Setting both up correctly — in the right order — is the main thing to get right.

1. **RingCentral identity** — established when you add the App Connect MCP server to your AI client (Claude, ChatGPT, Codex, etc.). This is a standard RingCentral OAuth/SSO flow and happens automatically as part of the steps below.
2. **CRM connection** — established separately, through the **[App Connect Chrome extension](https://github.com/ringcentral/rc-unified-crm-extension)** ("RingCentral App Connect"). Install the extension, sign in with the same RingCentral account, and connect your CRM from there — not from inside your AI client.

The App Connect server remembers the CRM session tied to your RingCentral identity. Once the extension has connected a CRM, any AI client with the MCP server enabled auto-detects that session — there's no separate CRM login step to repeat in Claude, ChatGPT, or Codex. If a tool call fails with a CRM auth error, the fix is almost always to (re)connect the CRM in the extension, not in the AI client.

**Recommended order:**

1. Add the MCP server to your AI client (below) — this handles RingCentral auth.
2. Install the App Connect Chrome extension and connect your CRM through it.
3. Return to your AI client and verify: ask "Check my RingCentral session status."

!!! warning "One CRM at a time"
    App Connect intermediates the connection to your CRM, and it supports **one connected CRM per RingCentral account at a time**. If you need to switch CRMs, disconnect the current one in the extension (or call [`logout`](../tools/app-connect.md#logout)) before connecting a new one — you can't have two CRMs linked simultaneously.

!!! tip "Does your CRM have its own MCP server?"
    Some CRMs (e.g. Salesforce) publish their own dedicated MCP servers, which can expose more CRM-specific functionality than App Connect's generic tool set. If your CRM has one, it's worth evaluating alongside App Connect. App Connect is most valuable when your CRM **doesn't** yet support MCP directly — it gives you contact lookup, contact creation, and call logging without waiting on the CRM vendor.

---

## Connect to your AI client

=== "Claude"

    Custom connectors live under **Customize > Connectors** (Claude.ai) or **Settings → Connectors** (Claude Desktop) — not through `claude_desktop_config.json`, which only supports local stdio servers.

    1. Sign in to [claude.ai](https://claude.ai), or open Claude Desktop.
    2. **Pro/Max:** go to **Customize > Connectors** → click **+** → **Add custom connector**. **Team/Enterprise:** an Owner first adds it under **Organization settings > Connectors** → **Add** → hover **Custom** → select **Web**; members then connect individually via **Customize > Connectors**.
    3. Enter a name (e.g. `RingCentral App Connect`) and the URL above, then click **Add**.
    4. Complete the RingCentral OAuth flow. This only establishes your RingCentral identity — see [Connect your CRM](#connect-your-crm-via-the-chrome-extension) below to link a CRM.
    5. In a new conversation, click the **+** button (lower left of the chat box) → **Connectors**, and toggle App Connect on.
    6. Verify: ask "Check my RingCentral session status."

=== "ChatGPT"

    ChatGPT calls this an **App** (renamed from "Connector" in December 2025). Connecting a server that can call tools — not just read/fetch — requires Developer Mode.

    1. **Business/Enterprise/Edu workspaces:** a workspace admin enables Developer Mode via **Workspace Settings → Permissions & Roles → Connected Data**. **Individual Enterprise/Edu accounts, or Pro (read/fetch-only):** go to **Settings → Apps → Advanced Settings** and toggle **Developer mode** on.
    2. In **Settings → Apps**, click **Create**, enter the URL above as the MCP Server URL, name it (e.g. `RingCentral App Connect`), click **Scan Tools**, then **Save**.
    3. Complete the RingCentral OAuth flow. This only establishes your RingCentral identity — see [Connect your CRM](#connect-your-crm-via-the-chrome-extension) below to link a CRM.
    4. Open a new chat, click the **+** icon or tools menu, and select App Connect — or mention it by name in your prompt.
    5. Verify: ask "Check my RingCentral session status."

    !!! note "Pro users"
        With read/fetch-only Developer Mode, you can look up CRM contacts and call logs, but can't create contacts or log calls.

=== "Codex"

    1. Open the Codex app → click the **Settings** gear (bottom left) → **MCP Servers** → **Add server**.
    2. Enter a name (e.g. `RingCentral App Connect`), set Type to **Streamable HTTP**, and enter the URL above.
    3. Click **Save**, then select **Restart** so Codex picks up the new server.
    4. Authenticate with your RingCentral account in the browser window that opens. This only establishes your RingCentral identity — see [Connect your CRM](#connect-your-crm-via-the-chrome-extension) below to link a CRM.
    5. Codex has no connector picker — mention "RingCentral" explicitly in your prompt, e.g. "Using RingCentral, check my session status."

---

## Connect your CRM (via the Chrome extension)

CRM auth happens outside your AI client, through the App Connect Chrome extension:

1. Install the [App Connect Chrome extension](https://github.com/ringcentral/rc-unified-crm-extension) and sign in with your RingCentral account (the same one you used above).
2. In the extension, choose your CRM platform and click through its OAuth flow to link your account. Supported platforms include Salesforce, HubSpot, Zoho, and others — see [`getPublicConnectors`](../tools/app-connect.md#getpublicconnectors) for the full list.
3. Once connected, the extension keeps that CRM session alive server-side. You don't need to keep the extension open or repeat this step per AI client — App Connect auto-detects the session the next time your AI client calls a CRM-dependent tool.

You can also check or trigger this from within a conversation once the MCP server is connected: ask *"What CRM platforms can I connect?"* to see available connectors, and *"What is my session status?"* to confirm `crmConnected` is `true`.

Remember: only **one CRM can be connected at a time** per RingCentral account. To switch, disconnect the current CRM first (in the extension, or by asking your assistant to log out).

---

## Troubleshooting

**Tools not appearing after connecting**

- Confirm the URL has no trailing slash.
- Disconnect and reconnect the server from your client's connector/app settings.
- Check that your network allows outbound HTTPS to `*.ringcentral.com` and `*.labs.ringcentral.com`.

**Authentication errors**

- Remove the connector/app and re-add it to restart the RingCentral OAuth flow.
- Ensure your RingCentral account has the necessary API permissions.

**CRM tools returning errors**

- Ask: *"What is my session status?"* — if `crmConnected` is `false`, the CRM layer isn't linked (or was disconnected). Open the App Connect Chrome extension and reconnect your CRM there — reconnecting inside the AI client won't fix this, since CRM auth isn't handled by the client.
- If you recently switched CRMs, confirm the old one was disconnected first — only one CRM can be linked at a time.

---

[← Back to App Connect](app-connect.md)
