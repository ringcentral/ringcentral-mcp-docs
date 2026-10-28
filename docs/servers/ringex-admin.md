# RingEX Admin

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://mcp.labs.ringcentral.com/ringex/admin</code><button class="rc-copy" data-copy="https://mcp.labs.ringcentral.com/ringex/admin" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--experimental">Experimental</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

---

## About

--8<-- "experimental.md"

RingEX Admin gives your AI assistant the ability to administer a RingEX account: users and extensions, roles and permissions, sites, phone numbers, call queues, IVR menus and prompts, call routing and business hours, emergency call redirect, and the admin audit log. It joins [RingEX Phone](ringex-phone.md), [RingEX Chat](ringex-chat.md), and [RingEX Meetings](ringex-meetings.md) in the RingEX family, which replaced the original monolithic RingCentral MCP server — this one covers account- and admin-level tools.

Most tools are **action-based**: they take an `action` argument that selects a strict argument variant. Read tools return configuration; write tools change it.

!!! warning "Write tools require a two-step confirmation"
    Tools that change configuration return `status: "confirmation_required"` with a plan and a single-use `confirmationToken` on the first call, without changing anything. The assistant must show you the plan and only repeat the call — identical arguments plus the token — after you approve. Tokens expire after about five minutes.

---

## Connecting

See the [RingEX Admin Setup guide](ringex-admin-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

31 tools are available on this server, grouped by the area of the account they administer. See the [Tools reference](../tools/ringex-admin.md) for the full action and parameter breakdown per tool.

**Account**

| Tool | Access | Description |
|------|:---:|-------------|
| [`get_admin_setup_status`](../tools/ringex-admin.md#get_admin_setup_status) | Read | First-run checklist for a new account — site, main number, users, business hours, inbound routing |
| [`search_admin_audit_log`](../tools/ringex-admin.md#search_admin_audit_log) | Read | Search the account's admin change history by actor, date range, and category |

**Users and roles**

| Tool | Access | Description |
|------|:---:|-------------|
| [`read_users`](../tools/ringex-admin.md#read_users) | Read | List, search, or get users and extensions, and read a user's role and group assignments |
| [`manage_users`](../tools/ringex-admin.md#manage_users) | Write | Create, bulk-create, template-provision, or update users |
| [`disable_user`](../tools/ringex-admin.md#disable_user) | Destructive | Disable a user extension, recording the reason |
| [`bulk_move_users`](../tools/ringex-admin.md#bulk_move_users) | Write | Preview, execute, or check the status of a bulk move of users between sites |
| [`read_roles`](../tools/ringex-admin.md#read_roles) | Read | List roles and permissions, get a role, or list assignable roles |
| [`manage_roles`](../tools/ringex-admin.md#manage_roles) | Write | Create or update a role, assign it to users, or set the account default |
| [`delete_role`](../tools/ringex-admin.md#delete_role) | Destructive | Delete a custom role, reassigning or clearing its holders |

**Sites and phone numbers**

| Tool | Access | Description |
|------|:---:|-------------|
| [`read_sites`](../tools/ringex-admin.md#read_sites) | Read | List or get sites, list members, read a site IVR, or recommend an extension prefix |
| [`manage_sites`](../tools/ringex-admin.md#manage_sites) | Write | Create or update a site, assign members or an admin, or set the site IVR |
| [`delete_site`](../tools/ringex-admin.md#delete_site) | Destructive | Delete a site |
| [`read_phone_numbers`](../tools/ringex-admin.md#read_phone_numbers) | Read | List or get account phone numbers by usage type and status |
| [`assign_phone_number`](../tools/ringex-admin.md#assign_phone_number) | Write | Assign a number to an extension or as a company number, or replace an assignment |
| [`release_phone_number`](../tools/ringex-admin.md#release_phone_number) | Destructive | Release an unassigned number back to RingCentral |

**Company calls and recording**

| Tool | Access | Description |
|------|:---:|-------------|
| [`read_company_call_log`](../tools/ringex-admin.md#read_company_call_log) | Read | List, get, or sync the company's call history |
| [`read_company_active_calls`](../tools/ringex-admin.md#read_company_active_calls) | Read | Snapshot of the calls in progress across the company right now |
| [`read_company_call_analytics`](../tools/ringex-admin.md#read_company_call_analytics) | Read | Aggregate or timeline call counts, durations, and queue service levels |
| [`read_company_call_recordings`](../tools/ringex-admin.md#read_company_call_recordings) | Read | Get a recording's metadata or download its audio |
| [`read_call_recording_settings`](../tools/ringex-admin.md#read_call_recording_settings) | Read | Read recording settings, auto-recorded extensions, and recording greetings |

**Call queues**

| Tool | Access | Description |
|------|:---:|-------------|
| [`read_call_queues`](../tools/ringex-admin.md#read_call_queues) | Read | List or get call queues, members, overflow settings, and agent presence |
| [`manage_call_queues`](../tools/ringex-admin.md#manage_call_queues) | Write | Create or update a queue, set its members, overflow, or agent presence |
| [`delete_call_queue`](../tools/ringex-admin.md#delete_call_queue) | Destructive | Delete a call queue |

**IVR and call routing**

| Tool | Access | Description |
|------|:---:|-------------|
| [`read_call_routing`](../tools/ringex-admin.md#read_call_routing) | Read | Read IVR menus, business hours, company and extension rules, forward-all, or routing for a number |
| [`manage_routing_rules`](../tools/ringex-admin.md#manage_routing_rules) | Write | Create or update company, interaction, and state routing rules, and set business hours |
| [`delete_routing_rule`](../tools/ringex-admin.md#delete_routing_rule) | Destructive | Delete a company or extension routing rule |
| [`manage_ivr`](../tools/ringex-admin.md#manage_ivr) | Write | Create or update an IVR menu, add a destination, or attach a prompt |
| [`read_ivr_media`](../tools/ringex-admin.md#read_ivr_media) | Read | List or get IVR greeting prompts |
| [`manage_ivr_media`](../tools/ringex-admin.md#manage_ivr_media) | Write | Upload, replace, or rename an IVR prompt |
| [`delete_ivr_prompt`](../tools/ringex-admin.md#delete_ivr_prompt) | Destructive | Delete an IVR prompt |
| [`set_emergency_call_redirect`](../tools/ringex-admin.md#set_emergency_call_redirect) | Write | Enable or disable the account-wide emergency call redirect |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Run `read_users` with `action: "list"` to confirm your RingCentral identity resolves and that you hold the admin permissions these tools require. On a brand-new account, run `get_admin_setup_status` for a first-run checklist of what still needs configuring.
3. **Use** — Ask your AI assistant to look up a user, audit who changed what last week, add a member to a call queue, or walk an IVR menu's key actions.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/admin \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
