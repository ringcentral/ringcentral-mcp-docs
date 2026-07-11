# RingEx Admin

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/admin`  
**Status:** 🟡 Labs / Beta · New  
**Transport:** SSE over HTTPS

---

## About

RingEx Admin gives your AI assistant access to account and extension administration: tool discovery, generic API dispatch, extension details, presence, and directory search. It's one of three servers that replace the deprecated [RingCentral MCP](rc-labs-mcp.md) server — this one covers meta/discovery and account-level tools.

Run [`platform_get_capabilities`](../tools/ringcentral/platform-get-capabilities.md) to see a full summary of supported API endpoints and tools.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

!!! info "Migrating from RingCentral MCP"
    If you previously used `gatekeeper_select_tool`, `platform_get_capabilities`, `platform_list_get_operations`, `platform_list_post_operations`, `profile_get_current_extension`, `platform_call_get_operation`, `platform_call_post_operation`, `platform_read_extension`, `platform_read_unified_presence`, or `platform_search_directory_entries` on the deprecated RingCentral MCP server, point your client at this endpoint instead. Tool names and parameters are unchanged.

---

## Connecting

See the [RingEx Admin Setup guide](ringex-admin-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

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
| [`platform_search_directory_entries`](../tools/ringcentral/platform-search-directory-entries.md) | — | Search the company directory |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Run `profile_get_current_extension` to confirm your RingCentral identity is resolved.
3. **Use** — Ask your AI assistant to look up a colleague in the directory, check presence, or inspect your extension. See the [Tool Reference](../tools/ringcentral/index.md) for parameter-level detail (tool names and parameters carry over from the deprecated server).

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/admin \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
