# RingEX Admin

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://mcp.labs.ringcentral.com/ringex/admin</code><button class="rc-copy" data-copy="https://mcp.labs.ringcentral.com/ringex/admin" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--preview">Preview</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

---

## About

RingEX Admin gives your AI assistant access to account and extension administration: account info, extensions, roles and permissions, call analytics, directory/contacts, and presence. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers account- and admin-level tools.

Run `about_ringcentral_mcp_tools` to see a full summary of supported tools and permissions.

---

## Connecting

See the [RingEX Admin Setup guide](ringex-admin-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

26 tools are available on this server.

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-admin.md#about_ringcentral_mcp_tools) | — | List all available tools and permissions for this server |
| [`platform_analytics_calls_aggregation_fetch`](../tools/ringex-admin.md#platform_analytics_calls_aggregation_fetch) | — | Get calls aggregation data |
| [`platform_get_account_info_v2`](../tools/ringex-admin.md#platform_get_account_info_v2) | — | Get account info |
| [`platform_list_account_phone_numbers_v2`](../tools/ringex-admin.md#platform_list_account_phone_numbers_v2) | — | List account phone numbers |
| [`platform_list_account_switches`](../tools/ringex-admin.md#platform_list_account_switches) | — | List account switches |
| [`platform_list_administered_sites`](../tools/ringex-admin.md#platform_list_administered_sites) | — | List user administered sites |
| [`platform_list_answering_rules`](../tools/ringex-admin.md#platform_list_answering_rules) | — | List call handling rules |
| [`platform_list_contacts`](../tools/ringex-admin.md#platform_list_contacts) | — | List contacts |
| [`platform_list_directory_entries`](../tools/ringex-admin.md#platform_list_directory_entries) | — | Get company directory entries |
| [`platform_list_extensions`](../tools/ringex-admin.md#platform_list_extensions) | — | List extensions |
| [`platform_list_favorite_contacts`](../tools/ringex-admin.md#platform_list_favorite_contacts) | — | List favorite contacts |
| [`platform_read_account_phone_number`](../tools/ringex-admin.md#platform_read_account_phone_number) | — | Get a phone number |
| [`platform_read_account_presence`](../tools/ringex-admin.md#platform_read_account_presence) | — | Get user presence status list |
| [`platform_read_call_recording`](../tools/ringex-admin.md#platform_read_call_recording) | — | Get call recording |
| [`platform_read_call_recording_content`](../tools/ringex-admin.md#platform_read_call_recording_content) | — | Get call recording content |
| [`platform_read_company_call_log`](../tools/ringex-admin.md#platform_read_company_call_log) | — | List company call records |
| [`platform_read_company_call_record`](../tools/ringex-admin.md#platform_read_company_call_record) | — | Get company call record(s) |
| [`platform_read_contact`](../tools/ringex-admin.md#platform_read_contact) | — | Get user contact(s) |
| [`platform_read_country`](../tools/ringex-admin.md#platform_read_country) | — | Get country |
| [`platform_read_directory_entry`](../tools/ringex-admin.md#platform_read_directory_entry) | — | Get corporate directory entry |
| [`platform_read_directory_federation`](../tools/ringex-admin.md#platform_read_directory_federation) | — | Get account federation |
| [`platform_read_permission`](../tools/ringex-admin.md#platform_read_permission) | — | Get permission |
| [`platform_read_permission_category`](../tools/ringex-admin.md#platform_read_permission_category) | — | Get permission category |
| [`platform_read_user_role`](../tools/ringex-admin.md#platform_read_user_role) | — | Get user role |
| [`platform_read_user_presence_status`](../tools/ringex-admin.md#platform_read_user_presence_status) | — | Get user presence status |
| [`read_call_ai_notes`](../tools/ringex-admin.md#read_call_ai_notes) | — | Read call AI notes |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Run `platform_get_account_info_v2` to confirm your RingCentral identity is resolved.
3. **Use** — Ask your AI assistant to look up a colleague in the directory, check presence, review call analytics, or inspect account/extension settings.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/admin \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
