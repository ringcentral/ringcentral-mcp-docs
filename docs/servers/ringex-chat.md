# RingEx Chat

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/team-chat`  
**Status:** 🟡 Labs / Beta · New  
**Transport:** SSE over HTTPS

---

## About

RingEx Chat gives your AI assistant access to RingCentral Team Messaging (Glip): chats, direct and group conversations, teams, and posts. It's one of three servers that replace the deprecated [RingCentral MCP](rc-labs-mcp.md) server — this one covers team collaboration.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

!!! info "Migrating from RingCentral MCP"
    If you previously used any `platform_*_glip_*` tool on the deprecated RingCentral MCP server, point your client at this endpoint instead. Tool names and parameters are unchanged.

---

## Connecting

See the [RingEx Chat Setup guide](ringex-chat-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`platform_list_glip_chats_new`](../tools/ringcentral/platform-list-glip-chats-new.md) | — | List team messaging chats |
| [`platform_list_glip_conversations_new`](../tools/ringcentral/platform-list-glip-conversations-new.md) | — | List direct conversations |
| [`platform_list_glip_teams_new`](../tools/ringcentral/platform-list-glip-teams-new.md) | — | List teams |
| [`platform_read_glip_conversation_new`](../tools/ringcentral/platform-read-glip-conversation-new.md) | — | Get a conversation |
| [`platform_read_glip_team_new`](../tools/ringcentral/platform-read-glip-team-new.md) | — | Get a team |
| [`platform_read_glip_posts_new`](../tools/ringcentral/platform-read-glip-posts-new.md) | — | List posts in a chat |
| [`platform_create_glip_conversation_new`](../tools/ringcentral/platform-create-glip-conversation-new.md) | — | Create or open a conversation |
| [`platform_create_glip_post_new`](../tools/ringcentral/platform-create-glip-post-new.md) | — | Post a message to a chat |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to list your team messaging chats to confirm the connection is active.
3. **Use** — Ask your AI assistant to catch you up on a chat, post an update, or open a conversation. See the [Tool Reference](../tools/ringcentral/index.md) for parameter-level detail (tool names and parameters carry over from the deprecated server).

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/team-chat \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
