---
title: Connect to ChatGPT
description: Connect RingCentral MCP servers to ChatGPT using Connectors.
---

# Connect to ChatGPT

ChatGPT supports remote MCP servers through its **Connectors** feature. Once connected, you can invoke RingCentral tools directly in your conversations.

!!! info "Subscription required"
    ChatGPT Connectors require a **Pro, Team, Enterprise, or Edu** subscription. The feature is not available on the free tier.

---

## Server URLs

| Server | URL |
|--------|-----|
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` |
| RingCentral MCP | `https://mcp.labs.ringcentral.com/ringex` |

---

## Setup

=== "Step 1 — Enable Developer Mode"

    ChatGPT Connectors require Developer Mode to be enabled:

    1. Sign in to [chatgpt.com](https://chatgpt.com)
    2. Click your profile picture (top right) → **Settings**
    3. Navigate to **Connectors**
    4. Click **Advanced** at the bottom of the page
    5. Toggle **Developer mode** on

=== "Step 2 — Create a connector"

    1. In **Settings → Connectors**, click **Create connector**
    2. Enter the server URL in the **Base URL** field:

        ```
        https://unified-crm-extension.labs.ringcentral.com/mcp
        ```

    3. Give it a name, e.g. `RingCentral App Connect`
    4. Click **Save**

    Repeat to add the RingCentral MCP server if needed:

    ```
    https://mcp.labs.ringcentral.com/ringex
    ```

=== "Step 3 — Authenticate"

    After saving, ChatGPT will initiate the RingCentral OAuth flow:

    1. A browser window will open asking you to sign in to RingCentral
    2. Authorize the integration
    3. You will be redirected back to ChatGPT

=== "Step 4 — Enable for a conversation"

    Connectors must be explicitly enabled for each conversation:

    1. Open a new chat
    2. Click the **+** icon in the message compose area
    3. Select **More** → find your RingCentral connector
    4. Toggle it **on**

    The connector is now active for that conversation.

---

## Connect your CRM

Once the App Connect server is active in a conversation, link your CRM:

1. Ask: *"What CRM platforms can I connect?"*
2. ChatGPT will display available connectors
3. Follow the OAuth flow to link your CRM account

---

## Using tools in a conversation

With the connector enabled, invoke tools through natural language:

```
Check my RingCentral session status.
```

```
Look up the contact for +1 415 555 0123 in my CRM.
```

```
Show me my call logs from today and log the most recent one to Salesforce.
```

---

## Troubleshooting

**Connector not appearing in the + menu**

- Confirm Developer Mode is enabled in Settings → Connectors → Advanced
- Verify the connector was saved successfully in Settings → Connectors

**Authentication errors**

- Delete the connector and re-create it to restart the OAuth flow
- Ensure your RingCentral account has the necessary API permissions

**Tools returning CRM errors**

- Ask: *"What is my session status?"* — if `crmConnected` is `false`, re-link your CRM by asking *"What CRM platforms can I connect?"*

!!! warning "Connector scope per conversation"
    Connectors are enabled per-conversation, not globally. You need to activate the connector each time you start a new chat where you want to use RingCentral tools.
