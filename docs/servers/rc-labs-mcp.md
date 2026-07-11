# RingCentral MCP (Deprecated)

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex`  
**Status:** 🔴 Deprecated  
**Transport:** SSE over HTTPS

---

!!! danger "Deprecated — migrate to RingEx Phone, Chat, and Admin"
    This monolithic server has been replaced by three focused servers. It remains reachable for now to support in-flight migrations, but it will not receive new tools and may be shut off in a future release. Point new integrations at the replacements below.

    | Tool group on this server | Migrate to |
    |---|---|
    | Call log & AI call notes, SMS/fax/voicemail messages | [RingEx Phone](ringex-phone.md) |
    | Team messaging (Glip) chats, conversations, teams, posts | [RingEx Chat](ringex-chat.md) |
    | Meta/discovery, generic operations, extension, presence, directory | [RingEx Admin](ringex-admin.md) |

    Tool names and parameters are unchanged — only the endpoint URL differs. See each replacement server's page for its connecting instructions.

## About

The RingCentral MCP server gives your AI assistant direct access to the RingCentral platform. Read call logs, search the company directory, send and read team messages, retrieve voicemails and SMS, and pull AI-generated call notes — all through natural language.

Run [`platform_get_capabilities`](../tools/ringcentral/platform-get-capabilities.md) to see a full summary of supported API endpoints and tools.

!!! warning "Labs status"
    This server was part of RingCentral Labs and was never covered by RingCentral's standard SLA. It is now deprecated in favor of RingEx Phone, Chat, and Admin — see the migration notice above.

---

## Connecting

This server is deprecated — new connections should go to its replacements instead. If you're not yet able to migrate, add it to your MCP client the same way as the replacement servers, using this server's endpoint above: see the [RingEx Phone](ringex-phone-setup.md), [RingEx Chat](ringex-chat-setup.md), or [RingEx Admin](ringex-admin-setup.md) setup guides for the general steps for Claude, ChatGPT, and Codex.

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
