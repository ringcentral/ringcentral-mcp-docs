# RingCentral MCP

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex`  
**Status:** 🟡 Labs / Beta  
**Transport:** SSE over HTTPS

---

## About

The RingCentral MCP server gives your AI assistant direct access to the RingCentral platform. Read call logs, search the company directory, send and read team messages, retrieve voicemails and SMS, and pull AI-generated call notes — all through natural language.

Run [`platform_get_capabilities`](../tools/ringcentral/platform-get-capabilities.md) to see a full summary of supported API endpoints and tools.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

---

## Connecting

=== "Claude Desktop (Settings → Connectors)"

    Remote MCP servers cannot be added to `claude_desktop_config.json`. Use the Connectors UI instead:

    1. Open Claude Desktop → **Settings → Connectors**
    2. Click **Add connector**
    3. Enter URL: `https://mcp.labs.ringcentral.com/ringex`
    4. Click **Connect**

=== "Claude.ai (Settings → Integrations)"

    1. Open **Settings → Integrations → Add MCP Server**
    2. Enter URL: `https://mcp.labs.ringcentral.com/ringex`
    3. Click **Connect**

=== "Cursor"

    Add to `.cursor/mcp.json` in your project root:

    ```json
    {
      "mcpServers": {
        "ringcentral": {
          "url": "https://mcp.labs.ringcentral.com/ringex",
          "type": "http"
        }
      }
    }
    ```

---

## Available tools

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`gatekeeper_select_tool`](../tools/ringcentral/gatekeeper-select-tool.md) | — | Route a natural-language request to the right tool |
| [`platform_get_capabilities`](../tools/ringcentral/platform-get-capabilities.md) | — | List all supported API endpoints and tools |
| [`platform_list_get_operations`](../tools/ringcentral/platform-list-get-operations.md) | — | List available GET operations |
| [`platform_list_post_operations`](../tools/ringcentral/platform-list-post-operations.md) | — | List available POST operations |
| [`platform_call_get_operation`](../tools/ringcentral/platform-call-get-operation.md) | — | Execute any supported GET operation |
| [`platform_call_post_operation`](../tools/ringcentral/platform-call-post-operation.md) | — | Execute any supported POST operation |
| [`profile_get_current_extension`](../tools/ringcentral/profile-get-current-extension.md) | — | Get the authenticated user's extension |
| [`platform_read_extension`](../tools/ringcentral/platform-read-extension.md) | — | Get extension details |
| [`platform_read_unified_presence`](../tools/ringcentral/platform-read-unified-presence.md) | — | Get presence status |
| [`platform_read_user_call_log`](../tools/ringcentral/platform-read-user-call-log.md) | — | List call records |
| [`platform_read_ai_notes`](../tools/ringcentral/platform-read-ai-notes.md) | — | Retrieve AI-generated call notes |
| [`platform_list_glip_chats_new`](../tools/ringcentral/platform-list-glip-chats-new.md) | — | List team messaging chats |
| [`platform_list_glip_conversations_new`](../tools/ringcentral/platform-list-glip-conversations-new.md) | — | List direct conversations |
| [`platform_list_glip_teams_new`](../tools/ringcentral/platform-list-glip-teams-new.md) | — | List teams |
| [`platform_read_glip_conversation_new`](../tools/ringcentral/platform-read-glip-conversation-new.md) | — | Get a conversation |
| [`platform_read_glip_team_new`](../tools/ringcentral/platform-read-glip-team-new.md) | — | Get a team |
| [`platform_read_glip_posts_new`](../tools/ringcentral/platform-read-glip-posts-new.md) | — | List posts in a chat |
| [`platform_create_glip_conversation_new`](../tools/ringcentral/platform-create-glip-conversation-new.md) | — | Create or open a conversation |
| [`platform_create_glip_post_new`](../tools/ringcentral/platform-create-glip-post-new.md) | — | Post a message to a chat |
| [`platform_list_messages`](../tools/ringcentral/platform-list-messages.md) | — | List messages from the message store |
| [`platform_read_message`](../tools/ringcentral/platform-read-message.md) | — | Get one or more messages |
| [`platform_read_message_content`](../tools/ringcentral/platform-read-message-content.md) | — | Download a message attachment |
| [`platform_search_directory_entries`](../tools/ringcentral/platform-search-directory-entries.md) | — | Search the company directory |

---

## Getting started

1. **Connect** — After adding the server, run `getPublicConnectors` and follow the on-screen steps to authenticate with your CRM.
2. **Verify** — Run `getSessionInfo` to confirm your RingCentral identity and CRM connection are active.
3. **Use** — Ask your AI assistant to look up contacts, retrieve call logs, read messages, or search the directory. See the [Tool Reference](../tools/ringcentral/index.md) for a full list of available tools.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
