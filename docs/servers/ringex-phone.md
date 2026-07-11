# RingEx Phone

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/phone`  
**Status:** 🟡 Labs / Beta · New  
**Transport:** SSE over HTTPS

---

## About

RingEx Phone gives your AI assistant access to telephony data: call logs, AI-generated call notes, and messages (SMS, fax, voicemail, and pager) from the message store. It's one of three servers that replace the deprecated [RingCentral MCP](rc-labs-mcp.md) server — this one covers the phone and messaging side.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

!!! info "Migrating from RingCentral MCP"
    If you previously used `platform_read_user_call_log`, `platform_read_ai_notes`, `platform_list_messages`, `platform_read_message`, or `platform_read_message_content` on the deprecated RingCentral MCP server, point your client at this endpoint instead. Tool names and parameters are unchanged.

---

## Connecting

See the [RingEx Phone Setup guide](ringex-phone-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`platform_read_user_call_log`](../tools/ringcentral/platform-read-user-call-log.md) | — | List call records |
| [`platform_read_ai_notes`](../tools/ringcentral/platform-read-ai-notes.md) | — | Retrieve AI-generated call notes |
| [`platform_list_messages`](../tools/ringcentral/platform-list-messages.md) | — | List messages from the message store |
| [`platform_read_message`](../tools/ringcentral/platform-read-message.md) | — | Get one or more messages |
| [`platform_read_message_content`](../tools/ringcentral/platform-read-message-content.md) | — | Download a message attachment |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to show your recent call log to confirm the connection is active.
3. **Use** — Ask your AI assistant to look up calls, voicemails, SMS, or AI-generated call notes. See the [Tool Reference](../tools/ringcentral/index.md) for parameter-level detail (tool names and parameters carry over from the deprecated server).

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/phone \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
