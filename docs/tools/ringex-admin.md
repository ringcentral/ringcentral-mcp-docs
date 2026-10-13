# RingEX Admin — Tools Reference

Full reference for every tool available on the [RingEX Admin](../servers/ringex-admin.md) server. Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

!!! danger "Experimental — not for production accounts"
    These tools change live account configuration and some paths have not been validated end to end against a live tenant. Interfaces may change without notice. Use a test account.

Most admin tools are **action-based**: they take an `action` argument that selects a strict argument variant. Pick exactly one variant and don't mix fields between variants — the server rejects calls that do. The single-purpose tools (`delete_call_queue`, `delete_ivr_prompt`, `delete_site`, `get_admin_setup_status`, `search_admin_audit_log`) take no `action` argument; each tool's parameter table below is authoritative.

!!! warning "Write tools require a two-step confirmation"
    Tools that change configuration return `status: "confirmation_required"` with a plan and a single-use `confirmationToken` on the first call, without changing anything. Show the plan to the user, and only after explicit approval repeat the identical arguments plus the token. Tokens expire after about five minutes and are refused if the affected objects changed in the meantime.

---

## about_ringcentral_mcp_tools

Call this first when you want to know what a RingEX MCP server can do, what tools are available, or which RingCentral tasks are supported. Returns a concise overview of the available tool categories and representative tool names for the connected server.

**Available on:** [RingEX Phone](../servers/ringex-phone.md) · [RingEX Chat](../servers/ringex-chat.md) · [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

This tool takes no parameters.

---

### Returns

| Field | Type | Description |
|-------|------|-------------|
| `summary` | `string` | A short description of what the connected server can help with. |
| `categories` | `array` | A list of capability categories, each with: `category` (name), `examples` (example use cases), and `representativeTools` (a sample of tool names in that category). |
| `usageNotes` | `array` | Operational tips — e.g. that `tools/list` should be used to inspect exact tool names and input schemas, that authenticated `accountId`/`extensionId` parameters usually default to the current user, and that write tools should only be selected when the user actually asks for that side effect. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "about_ringcentral_mcp_tools",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What can this RingCentral MCP server do?
    ```

---

!!! tip "Start here"
    Run this tool right after connecting a new RingEX server to confirm which capabilities and tools are exposed, before calling `tools/list` for exact schemas.

---

## assign_phone_number

Assigns an existing account phone number — from inventory or from another assignment — to a user, IVR menu, or call queue, or makes it a company number. Can also swap one number for another. It never buys numbers; use [`read_phone_numbers`](#read_phone_numbers) to find existing numbers and their ids.

The main company number cannot be reassigned with `assign` except to a company role, and it cannot be swapped with `replace`.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required

---

### Actions

| Action | Required | Optional | What it does |
|--------|----------|----------|--------------|
| `assign` | `phoneNumberId`, `destination` | `confirmationToken` | Points the number at an extension or makes it a company number. |
| `replace` | `phoneNumberId`, `targetPhoneNumberId` | `confirmationToken` | Swaps one number for another — e.g. a temporary number for a ported-in number. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `assign` or `replace`. |
| `phoneNumberId` | ✅ | The number being assigned or replaced. |
| `destination` | ✅ (assign) | Either `{ "type": "extension", "extensionId": "..." }` — a user, IVR menu, or call queue extension that gets the number as its direct number — or `{ "type": "company_number", "usageType": "CompanyNumber" \| "MainCompanyNumber" }`. |
| `targetPhoneNumberId` | ✅ (replace) | The other number RingCentral swaps it with. |
| `confirmationToken` | — | Token from the preview call. Send identical arguments plus this token to execute. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "assign_phone_number",
        "arguments": {
          "action": "assign",
          "phoneNumberId": "14155550123",
          "destination": {
            "type": "extension",
            "extensionId": "402304004"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Assign the number +1 415 555 0123 to Dana's extension as her direct line.
    ```

---

!!! warning "Changes live call routing"
    Both actions change where inbound calls ring, so both require the two-step confirmation described at the top of this page.

!!! info "`replace` semantics are not yet validated against a live tenant"
    Exactly what RingCentral does to both numbers during a swap has not been exercised end to end. Test `replace` on a non-production account first.

---

## bulk_move_users

Moves up to 50 extensions to another site, in three steps: `preview` resolves every extension and returns a plan, `execute` starts the move, and `status` reports per-extension results. Execution is asynchronous — `execute` returns a `taskId` that you poll with `status`.

Extensions already in the target site are skipped. A task can finish with some moves failed, which is reported as `partial_failure` rather than success. Use [`read_users`](#read_users) for extension ids and [`read_sites`](#read_sites) for site ids.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required

---

### Actions

| Action | Required | What it does |
|--------|----------|--------------|
| `preview` | `extensionIds`, `targetSiteId` | Resolves each extension, shows its current site, and returns a plan plus a `confirmationToken`. Nothing changes. |
| `execute` | `extensionIds`, `targetSiteId`, `confirmationToken` | Starts the move and returns a `taskId`. |
| `status` | `taskId` | Returns per-extension `Success` / `Fail` results for the task. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `preview`, `execute`, or `status`. |
| `extensionIds` | ✅ (preview, execute) | Numeric extension ids from `read_users`. At most 50. |
| `targetSiteId` | ✅ (preview, execute) | Destination site id from `read_sites`. Use `main-site` to move users to the main site. |
| `taskId` | ✅ (status) | Task id returned by `execute`. |
| `confirmationToken` | ✅ (execute) | Token returned by `preview`. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "bulk_move_users",
        "arguments": {
          "action": "preview",
          "extensionIds": ["402304004", "402304005"],
          "targetSiteId": "88001122"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Move everyone currently in the Austin site over to the new Dallas site.
    ```

---

!!! warning "Asynchronous and partially fallible"
    Always poll `status` after `execute`. A `partial_failure` result means some extensions moved and others did not.

---

## delete_call_queue

Permanently deletes one call queue after checking what depends on it. The dependency check looks for phone numbers assigned to the queue, IVR menus that route to it, and other queues that overflow to it. If any exist — or a check could not be completed — the result is `blocked` with the list of blockers and no token is issued.

Queue members are not a blocker; they are removed along with the queue.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `callQueueId` | ✅ | Queue to delete, from [`read_call_queues`](#read_call_queues). |
| `confirmationToken` | — | Token from the preview call. Send the same `callQueueId` plus this token to execute. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "delete_call_queue",
        "arguments": {
          "callQueueId": "402304099"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the old "Tier 1 Overflow" call queue — check first what still points at it.
    ```

---

!!! danger "The check is deliberately limited"
    It does not inspect user or site call-handling rules that forward to the queue, a site operator, or call monitoring and paging groups that include it, and it reads at most 50 IVR menus and 50 other queues. Larger accounts are reported as an incomplete check and blocked. Review those places yourself before approving. Deletion cannot be undone with this tool.

---

## delete_ivr_prompt

Permanently deletes one IVR audio prompt. The call is refused while any IVR menu still plays the prompt, and also when the menu scan cannot prove that none does — the refusal lists which menus to change first with [`manage_ivr`](#manage_ivr).

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `promptId` | ✅ | Prompt to delete, from [`read_ivr_media`](#read_ivr_media). |
| `confirmationToken` | — | Token from the preview call. Send the same `promptId` plus this token to execute. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "delete_ivr_prompt",
        "arguments": {
          "promptId": "prompt-2024-holiday"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Remove last year's holiday greeting from our IVR prompt library.
    ```

---

!!! danger "Cannot be undone"
    To restore a deleted prompt you must upload the audio again with [`manage_ivr_media`](#manage_ivr_media).

---

## delete_role

Permanently deletes one custom role. Standard roles cannot be deleted. The first call finds every user who holds the role and returns the role, the affected users, and the replacement role.

You must state what happens to those users: pass `replacementRoleId` (added to each holder before deletion) or, only when nobody holds the role, `noAssignments: true`. A wrong assertion is refused. The call also refuses if the account is too large to verify every assignment, or if more than 50 users hold the role.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `delete`. |
| `roleId` | ✅ | Role id from [`read_roles`](#read_roles). |
| `replacementRoleId` | ✅ (if anyone holds the role) | Role added to every current holder before deletion. |
| `noAssignments` | — | `true` to assert nobody holds the role. Verified against current assignments and rejected if wrong. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "delete_role",
        "arguments": {
          "action": "delete",
          "roleId": "custom-support-lead",
          "replacementRoleId": "standard-user"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the "Support Lead" custom role and move everyone on it to Standard User.
    ```

---

!!! danger "Requires role-management permission"
    The role is re-read after deletion; a `partial` status means a step did not finish, and the result says which.

---

## delete_routing_rule

Deletes one custom company answering rule or one extension interaction rule. Default company rules (`BusinessHours`, `AfterHours`) and built-in extension state rules (`work-hours`, `after-hours`, `dnd`, `forward-all-calls`, `agent`) cannot be deleted — change them with [`manage_routing_rules`](#manage_routing_rules) instead.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Actions

| Action | Required | Optional | What it does |
|--------|----------|----------|--------------|
| `delete_company_rule` | `ruleId` | `confirmationToken` | Deletes a custom company answering rule. |
| `delete_extension_rule` | `extensionId`, `ruleId` | `confirmationToken` | Deletes one extension's interaction rule. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `delete_company_rule` or `delete_extension_rule`. |
| `ruleId` | ✅ | Rule to delete, from [`read_call_routing`](#read_call_routing). |
| `extensionId` | ✅ (extension rules) | Extension that owns the rule. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "delete_routing_rule",
        "arguments": {
          "action": "delete_company_rule",
          "ruleId": "rule-holiday-2025"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the leftover 2025 holiday answering rule from our company call handling.
    ```

---

!!! info "Legacy API"
    Company rules use RingCentral's legacy call-handling API because no replacement exists. The result reads the rule back to verify it is gone.

---

## delete_site

Permanently deletes one empty site. The first call checks that the site has no members and no phone numbers assigned to it. If anything depends on the site, the status is `blocked` with the list of blockers — move users with [`bulk_move_users`](#bulk_move_users) or [`manage_sites`](#manage_sites) `assign_members`, and reassign numbers, first.

The main site (`main-site`) cannot be deleted.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `siteId` | ✅ | Site id from [`read_sites`](#read_sites). `main-site` is not accepted. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "delete_site",
        "arguments": {
          "siteId": "88001122"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    We closed the Austin office — delete that site if nothing is still attached to it.
    ```

---

!!! danger "Not every dependency is detected"
    Queues, IVR menus, and routing rules that point at the site are not checked. Review those yourself before approving.

---

## disable_user

Sets one user extension's status to `Disabled`. It never deletes the extension. Only extensions of type `User` are accepted, and you cannot disable your own account.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `disable`. |
| `extensionId` | ✅ | Numeric extension id from [`read_users`](#read_users). |
| `reason` | — | `Voluntarily` or `Involuntarily`. Recorded by RingCentral. |
| `comment` | — | Short internal note recorded with the status change. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "disable_user",
        "arguments": {
          "action": "disable",
          "extensionId": "402304004",
          "reason": "Voluntarily",
          "comment": "Offboarded 2026-10-01"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Disable Dana's RingCentral account — she left the company last week.
    ```

---

!!! warning "Phone numbers, devices, and licences stay assigned"
    Disabling does not release them. Handle those separately. The status is re-read afterwards; `partial` means the change could not be verified.

---

## get_admin_setup_status

Read-only first-run checklist for a new RingEX account. Inspects whether the account has a site, a main company number, initial users, company business hours, and basic inbound routing, then returns an ordered checklist with the recommended next step.

A check that cannot be read with the administrator's permissions is reported as `unknown` rather than failing the whole checklist. Site administrators cannot be verified from account-level reads, so that check is always `unknown` — use [`read_users`](#read_users) with `action: "get_assignments"` for a specific person.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

This tool takes no parameters.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_admin_setup_status",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    We just got our RingCentral account — what still needs setting up?
    ```

---

!!! tip "Good opening move"
    Run this against a new account before anything else; it tells you which of the other admin tools to reach for next.

---

## manage_call_queues

Creates and updates call queues and manages who answers them. It never deletes a queue — use [`delete_call_queue`](#delete_call_queue).

Ringing order (round robin, simultaneous, fixed order) is part of call handling rules and is not configured here.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `create` | `name` | `extensionNumber`, `siteId`, `memberExtensionIds`, `confirmationToken` | ✅ |
| `update` | `callQueueId` | `name`, `extensionNumber`, `status`, `siteId`, `editableMemberStatus`, `alertTimerSeconds`, `serviceLevel` | — |
| `set_members` | `callQueueId` | `addedExtensionIds`, `removedExtensionIds`, `confirmationToken` | When adding more than one member, or removing anyone |
| `set_overflow` | `callQueueId` | `enabled`, `overflowQueueIds`, `confirmationToken` | ✅ |
| `set_presence` | `callQueueId`, `members` | — | — |
| `set_agent_presence` | `extensionId`, `queues` | — | — |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `callQueueId` | ✅ (most actions) | Queue id from [`read_call_queues`](#read_call_queues). |
| `name` | ✅ (create) | Queue display name, up to 100 characters. |
| `extensionNumber` | — | 2–8 digit extension number for the queue. |
| `siteId` | — | Site that owns the queue, from [`read_sites`](#read_sites). |
| `status` | — | `Enabled` or `Disabled`. |
| `memberExtensionIds` | — | Initial members on `create`. Up to 50. |
| `addedExtensionIds` / `removedExtensionIds` | — | Members to add or remove on `set_members`. Up to 50 each. |
| `editableMemberStatus` | — | Whether members may change their own queue availability. |
| `alertTimerSeconds` | — | Seconds before queue members are notified of a queued call. |
| `serviceLevel` | — | Object with `thresholdSeconds` and `abandonedThresholdSeconds` (0–86400), `goalPercent` (0–100), and `includeAbandonedCalls`. |
| `overflowQueueIds` | — | Queues that receive overflow calls. An empty list clears them. Up to 10. |
| `members` | ✅ (set_presence) | Array of up to 50 `{ extensionId, acceptCurrentQueueCalls }`. |
| `queues` | ✅ (set_agent_presence) | Array of up to 50 `{ callQueueId, acceptCalls }` for one agent. |
| `confirmationToken` | — | Token from the preview call, for the actions that need it. |

---

### Examples

=== "Create a queue"

    ```json
    {
      "action": "create",
      "name": "Tier 1 Support",
      "extensionNumber": "7100",
      "memberExtensionIds": ["402304004", "402304005"]
    }
    ```

=== "Set overflow"

    ```json
    {
      "action": "set_overflow",
      "callQueueId": "402304099",
      "enabled": true,
      "overflowQueueIds": ["402304100"]
    }
    ```

=== "Take an agent off a queue"

    ```json
    {
      "action": "set_agent_presence",
      "extensionId": "402304004",
      "queues": [
        { "callQueueId": "402304099", "acceptCalls": false }
      ]
    }
    ```

=== "Claude prompt"

    ```
    Create a "Tier 1 Support" queue at extension 7100 with Dana and Sam in it.
    ```

---

!!! warning "Overflow loops are refused"
    `set_overflow` changes live routing and refuses a configuration that would create a loop between queues. Actions that run without confirmation are verified by re-reading the queue.

!!! info "Queue creation is not yet validated against a live tenant"
    RingCentral's exact requirements for creating a queue have not been exercised end to end. Test `create` on a non-production account first.

---

## manage_ivr

Creates and changes IVR (auto-attendant) menus — their name, greeting, and key-press destinations. It never deletes a menu, prompt, or extension, and only works in your own account.

`update` replaces the **complete** key-action list, not a delta. A menu whose current settings cannot be copied exactly is refused rather than rewritten. Upload audio with [`manage_ivr_media`](#manage_ivr_media) first.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `create` | `name` | `extensionNumber`, `siteId`, `prompt`, `keyActions` | — |
| `update` | `menuId` | `name`, `prompt`, `keyActions`, `confirmationToken` | ✅ |
| `create_destination` | `type`, `name`, `contactEmail` | `extensionNumber`, `siteId` | — |
| `attach_prompt` | `menuId`, `promptId` | `confirmationToken` | ✅ |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `menuId` | ✅ (update, attach_prompt) | Menu id from [`read_call_routing`](#read_call_routing) `get_ivr`. |
| `name` | ✅ (create, create_destination) | Display name, up to 256 characters. |
| `extensionNumber` | — | 2–8 digit extension number. RingCentral assigns one if omitted. |
| `siteId` | — | Site that owns the menu, from [`read_sites`](#read_sites). |
| `prompt` | — | Either `{ "mode": "Audio", "promptId": "..." }` or `{ "mode": "TextToSpeech", "text": "..." }`, where `text` is up to 1000 characters. |
| `keyActions` | — | The complete new key-action list (up to 13 entries). Each is `{ input, action, extensionId?, phoneNumber? }`. `input` is `0`–`9`, `Star`, `Hash`, or `NoInput`. `action` is one of `Connect`, `Voicemail`, `DialByName`, `Transfer`, `Repeat`, `ReturnToRoot`, `ReturnToPrevious`, `Disconnect`, `ReturnToTopLevelMenu`, `DoNothing`, `ConnectToOperator`. `extensionId` is required for `Connect` and `Voicemail` and not allowed otherwise; `phoneNumber` is required for `Transfer` and not allowed otherwise. |
| `type` | ✅ (create_destination) | `Announcement` (plays a message) or `Voicemail` (takes a message). |
| `contactEmail` | ✅ (create_destination) | Contact email for the new extension — voicemail notifications go here. |
| `promptId` | ✅ (attach_prompt) | Audio prompt id from [`read_ivr_media`](#read_ivr_media), or the id returned by a [`manage_ivr_media`](#manage_ivr_media) upload. |
| `confirmationToken` | — | Token from the preview call. |

---

### Examples

=== "Create a menu"

    ```json
    {
      "action": "create",
      "name": "Main Auto-Attendant",
      "extensionNumber": "8000",
      "prompt": {
        "mode": "TextToSpeech",
        "text": "Thanks for calling. Press 1 for sales, 2 for support."
      },
      "keyActions": [
        { "input": "1", "action": "Connect", "extensionId": "402304099" },
        { "input": "2", "action": "Connect", "extensionId": "402304100" },
        { "input": "NoInput", "action": "ConnectToOperator" }
      ]
    }
    ```

=== "Attach an audio prompt"

    ```json
    {
      "action": "attach_prompt",
      "menuId": "ivr-main",
      "promptId": "prompt-welcome-2026"
    }
    ```

=== "Claude prompt"

    ```
    Set up a main auto-attendant on extension 8000: 1 goes to Sales, 2 to Support.
    ```

---

!!! warning "Key actions are replaced wholesale"
    On `update`, omitted keys are removed. Read the menu first with `read_call_routing` and send the full intended list.

---

## manage_ivr_media

Uploads and replaces the audio files that IVR menus play. It does not generate speech from text, and it never deletes a prompt — use [`delete_ivr_prompt`](#delete_ivr_prompt).

WAV and MP3 are recommended; files over 10 MB are refused. Attach an uploaded prompt to a menu with [`manage_ivr`](#manage_ivr).

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `upload` | — | `file`, `contentBase64`, `fileName`, `contentType`, `description` | — |
| `replace` | `promptId` | `file`, `contentBase64`, `fileName`, `contentType`, `description`, `confirmationToken` | When any menu uses the old prompt |
| `rename` | `promptId`, `filename` | — | — |

`replace` uploads a new prompt and repoints every menu that currently plays the old prompt to it, leaving the old prompt in place. Menus with settings the tool cannot copy exactly are left unchanged and reported as failed.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `upload`, `replace`, or `rename`. |
| `promptId` | ✅ (replace, rename) | Existing prompt from [`read_ivr_media`](#read_ivr_media). |
| `file` | — | ChatGPT file reference (`download_url` + `file_id`) for the audio file. |
| `contentBase64` | — | Exact standard base64 audio bytes, for clients without file-parameter transformation. Provide `fileName` with it. Not a path, URL, or data URL. |
| `fileName` | — | Audio file name with extension, e.g. `welcome.wav`. Required with `contentBase64`. |
| `filename` | ✅ (rename) | The new file name for the prompt. Renaming cannot change the audio. |
| `contentType` | — | Audio MIME type. Inferred from the file extension when omitted. |
| `description` | — | Optional description of the prompt contents. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "manage_ivr_media",
        "arguments": {
          "action": "upload",
          "contentBase64": "UklGRi...",
          "fileName": "welcome-2026.wav",
          "description": "Updated main greeting"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Upload this WAV as our new main greeting and swap it in for the old one.
    ```

---

!!! info "Two ways to supply audio"
    Use `file` when your client supports file references, or `contentBase64` plus `fileName` when it doesn't.

---

## manage_roles

Creates and updates custom roles and manages role assignments. It never deletes a role — use [`delete_role`](#delete_role). Requires an administrator with role-management permission.

`assign` and `bulk_assign` refuse your own account, and you cannot remove a role from yourself.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `create` | `name`, `permissionIds` | `description` | — |
| `update` | `roleId` | `name`, `description`, `permissionIds`, `confirmationToken` | When `permissionIds` is given |
| `assign` | `extensionId`, `roleIds` | `confirmationToken` | ✅ |
| `assign_default` | `extensionId` | `confirmationToken` | ✅ |
| `bulk_assign` | `roleId` | `addExtensionIds`, `removeExtensionIds`, `confirmationToken` | ✅ |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `roleId` | ✅ (update, bulk_assign) | Role id from [`read_roles`](#read_roles). |
| `name` | ✅ (create) | Role display name, up to 128 characters. |
| `description` | — | Role description, up to 2000 characters. |
| `permissionIds` | ✅ (create) | Permission ids from `read_roles` `list_permissions`. On `update` this is the **complete** new permission list, not a delta. Up to 300. |
| `extensionId` | ✅ (assign, assign_default) | Extension to change. |
| `roleIds` | ✅ (assign) | Roles to add to the user. Up to 10. |
| `addExtensionIds` / `removeExtensionIds` | — | Users to add to or remove from the role on `bulk_assign`. Up to 50 each. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "manage_roles",
        "arguments": {
          "action": "bulk_assign",
          "roleId": "custom-support-lead",
          "addExtensionIds": ["402304004", "402304005"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Give Dana and Sam the "Support Lead" role.
    ```

---

!!! warning "Assigning a role can take others away"
    RingCentral may change the roles a user already holds when a new role is assigned. The preview shows the user's current roles, and the result lists `previousRoles` and any `lostRoleIds` so a loss is visible. `assign_default` is not validated on a live tenant — check the result.

---

## manage_routing_rules

Creates and updates call-handling rules and business hours at both company and extension scope. It never deletes a rule — use [`delete_routing_rule`](#delete_routing_rule) — and never changes the company forward-all override, which is [`set_emergency_call_redirect`](#set_emergency_call_redirect).

Inspect current rules with [`read_call_routing`](#read_call_routing) first.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Scope | Required | Optional | Confirmation |
|--------|-------|----------|----------|:---:|
| `create_company_rule` | Company | `name` | `ruleType`, `enabled`, `schedule`, `callHandlingAction`, `destinationExtensionId`, `confirmationToken` | ✅ |
| `update_company_rule` | Company | `ruleId` | `name`, `enabled`, `schedule`, `callHandlingAction`, `destinationExtensionId`, `confirmationToken` | ✅ |
| `set_company_hours` | Company | `weeklyRanges` | `confirmationToken` | ✅ |
| `update_state_rule` | Extension | `extensionId`, `stateId`, `route` | `confirmationToken` | ✅ |
| `create_interaction_rule` | Extension | `extensionId`, `displayName`, `enabled`, `condition`, `route` | — | — |
| `update_interaction_rule` | Extension | `extensionId`, `ruleId` | `displayName`, `enabled`, `condition`, `route` | — |
| `set_user_hours` | Extension | `extensionId`, `weeklyRanges` | — | — |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `ruleId` | ✅ (update_company_rule, update_interaction_rule) | Rule id from `read_call_routing`. `update_state_rule` uses `stateId` instead. |
| `extensionId` | ✅ (extension scope) | Extension the rule belongs to. |
| `name` | ✅ (create_company_rule) | Company rule name, up to 30 characters. |
| `ruleType` | — | `BusinessHours`, `AfterHours`, or `Custom`. |
| `enabled` | ✅ (create_interaction_rule) | Whether the rule is active. Optional elsewhere; defaults to `true`. |
| `schedule` | — | `{ kind: "preset", ref: "BusinessHours" \| "AfterHours" }`, `{ kind: "weekly", weeklyRanges: {...} }`, or `{ kind: "dates", ranges: [...] }`. |
| `callHandlingAction` | — | `Operator` (play the company greeting, forward to the operator), `Disconnect`, or `Bypass` (forward to `destinationExtensionId`). |
| `destinationExtensionId` | ✅ (with `Bypass`) | Extension that receives the call. |
| `weeklyRanges` | ✅ (hours actions) | Complete weekly schedule keyed by day name, each day an array of `{ from, to }` in `HH:MM`. Omitted or empty days have no business hours. |
| `stateId` | ✅ (update_state_rule) | `work-hours`, `after-hours`, `dnd`, `forward-all-calls`, or `agent`. |
| `displayName` | ✅ (create_interaction_rule) | Rule name, up to 64 characters. |
| `condition` | ✅ (create_interaction_rule) | `{ type: "state", stateId: "work-hours" \| "after-hours" }` or `{ type: "callers", callers: [{ phoneNumber, name }] }` — up to 20 callers. |
| `route` | ✅ (state and interaction rules) | One of: `voicemail` (needs `extensionId` and `greetingPresetId`), `extension` (needs `extensionId`), `phone_number` (needs `phoneNumber` and `name`), or `ring_extensions` (needs `extensionIds` — up to 10 — and `ringMode` of `at_once` or `in_order`, plus optional `durationSeconds` between 10 and 300). |
| `confirmationToken` | — | Token from the preview call. |

---

### Examples

=== "Set company business hours"

    ```json
    {
      "action": "set_company_hours",
      "weeklyRanges": {
        "monday":    [{ "from": "09:00", "to": "17:00" }],
        "tuesday":   [{ "from": "09:00", "to": "17:00" }],
        "wednesday": [{ "from": "09:00", "to": "17:00" }],
        "thursday":  [{ "from": "09:00", "to": "17:00" }],
        "friday":    [{ "from": "09:00", "to": "15:00" }]
      }
    }
    ```

=== "Route a caller to voicemail"

    ```json
    {
      "action": "create_interaction_rule",
      "extensionId": "402304004",
      "displayName": "Known spam caller",
      "enabled": true,
      "condition": {
        "type": "callers",
        "callers": [{ "phoneNumber": "+14155550199", "name": "Spam" }]
      },
      "route": {
        "type": "voicemail",
        "extensionId": "402304004",
        "greetingPresetId": "preset-default"
      }
    }
    ```

=== "Claude prompt"

    ```
    Set our company business hours to 9–5 Monday through Thursday and 9–3 on Friday.
    ```

---

!!! warning "Voicemail is required as the terminal target"
    RingCentral rejects the `dnd` state rule and interaction rules with a plain extension route — use a voicemail route, whose `greetingPresetId` you copy from `read_call_routing` `get_extension_rules`. Company rules use the legacy call-handling API; extension rules use the newer API, which some legacy-routing accounts may not support.

!!! info "Extension-scope rules are not yet validated against a live tenant"
    The request bodies for extension-scope actions follow the OpenAPI contract but have not been exercised end to end. Test them on a non-production account first.

---

## manage_sites

Creates and updates RingEX sites and manages their members, administrators, and IVR key actions. It never deletes a site — use [`delete_site`](#delete_site).

The main site (`main-site`), site business hours, and site main-number assignment are not supported here.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `create` | `name`, `administratorExtensionId` | `extensionNumber`, `callerIdName`, `email`, `siteAccess`, `code` | — |
| `update` | `siteId` | `name`, `extensionNumber`, `callerIdName`, `email`, `siteAccess` | — |
| `assign_members` | `siteId`, `addExtensionIds`, `removeExtensionIds` | `confirmationToken` | When changing more than one member |
| `assign_admin` | `siteId`, `extensionId` | `confirmationToken` | ✅ |
| `set_ivr` | `siteId` | `topMenuId`, `keyActions`, `confirmationToken` | ✅ |

`create` creates the site and then assigns the required administrator. If that second step fails, the result has status `partial` so you can retry with `assign_admin`.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `siteId` | ✅ (most actions) | Site id from [`read_sites`](#read_sites). `main-site` is not accepted for changes. |
| `name` | ✅ (create) | Site name, up to 100 characters. |
| `administratorExtensionId` | ✅ (create) | Extension that will administer the new site. Every site needs at least one. |
| `extensionId` | ✅ (assign_admin) | Extension that becomes an administrator of the site. |
| `extensionNumber` | — | Site extension number, up to 8 digits. |
| `callerIdName` | — | Caller ID name shown to callers. RingCentral allows at most 15 characters. |
| `email` | — | Site contact email. |
| `siteAccess` | — | `Limited` or `Unlimited` — whether users of the site can reach other sites by dialing extensions. |
| `code` | — | Site code. |
| `addExtensionIds` / `removeExtensionIds` | ✅ (assign_members) | Numeric extension ids to add or remove. Up to 50 each; pass an empty array for the side you aren't changing. |
| `topMenuId` | — | Extension id of the site's top IVR menu. |
| `keyActions` | — | Replaces the site's key actions with exactly this list (up to 10). Each is `{ input, action, extensionId? }` where `input` is `0`, `Star`, `Hash`, or `NoInput` and `action` is `Repeat`, `ReturnToRoot`, `ReturnToPrevious`, `ReturnToTopLevelMenu`, `Connect`, `ConnectToIncomingCallRoutingSelection`, `ConnectToOperator`, `Disconnect`, or `DoNothing`. `extensionId` is required for `Connect` and not allowed otherwise. Note this enum is **not** the same as [`manage_ivr`](#manage_ivr)'s. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "manage_sites",
        "arguments": {
          "action": "create",
          "name": "Dallas Office",
          "administratorExtensionId": "402304004",
          "callerIdName": "RC Dallas",
          "siteAccess": "Unlimited"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a Dallas Office site with Dana as the site administrator.
    ```

---

!!! warning "set_ivr changes live call routing"
    It always returns a preview with the current and requested settings before anything changes.

---

## manage_users

Creates and updates users. It never disables or deletes users, never resets passwords, and never assigns phone numbers — those are [`disable_user`](#disable_user) and [`assign_phone_number`](#assign_phone_number).

Look up users with [`read_users`](#read_users), sites with [`read_sites`](#read_sites), and roles with [`read_roles`](#read_roles) first.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required for some actions

---

### Actions

| Action | Required | Optional | Confirmation |
|--------|----------|----------|:---:|
| `create` | `user` | `confirmationToken` | ✅ |
| `apply_template` | `templateId`, `user` | `confirmationToken` | ✅ |
| `bulk_create` | `users` | `confirmationToken` | ✅ |
| `update` | `extensionId` | `firstName`, `lastName`, `department`, `jobTitle`, `mobilePhone`, `businessPhone`, `extensionNumber`, `siteId` | — |

`create`, `apply_template`, and `bulk_create` consume licenses and change the directory, so all three preview first. `update` changes an existing extension directly.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `user` | ✅ (create, apply_template) | Object with `firstName`, `lastName`, `email` (required) plus optional `extensionNumber`, `department`, `jobTitle`, `siteId`, and — for `create` only — `roleIds` (up to 5). Under `apply_template`, `roleIds` is not accepted at all and `siteId` is only allowed when the template does not fix a site. |
| `users` | ✅ (bulk_create) | Array of up to 20 user objects, same shape as `user`. Results are returned per user. |
| `templateId` | ✅ (apply_template) | Server-owned organizational template. See the `ringex://admin/organizational-templates` resource. |
| `extensionId` | ✅ (update) | Numeric extension id of the user to change. |
| `firstName`, `lastName`, `department`, `jobTitle` | — | Contact fields, up to 64 characters each. |
| `mobilePhone`, `businessPhone` | — | Phone numbers. |
| `extensionNumber` | — | 2–10 digit extension number. RingCentral assigns one when omitted on create. |
| `siteId` | — | Site id from `read_sites`. Omit, or use `main-site`, for the main site. |
| `confirmationToken` | — | Token from the preview call. |

---

### Examples

=== "Create one user"

    ```json
    {
      "action": "create",
      "user": {
        "firstName": "Dana",
        "lastName": "Reyes",
        "email": "dana.reyes@example.com",
        "jobTitle": "Support Engineer",
        "siteId": "88001122"
      }
    }
    ```

=== "Bulk create"

    ```json
    {
      "action": "bulk_create",
      "users": [
        { "firstName": "Dana", "lastName": "Reyes", "email": "dana.reyes@example.com" },
        { "firstName": "Sam",  "lastName": "Okafor", "email": "sam.okafor@example.com" }
      ]
    }
    ```

=== "Update a user"

    ```json
    {
      "action": "update",
      "extensionId": "402304004",
      "jobTitle": "Senior Support Engineer",
      "department": "Customer Success"
    }
    ```

=== "Claude prompt"

    ```
    Add Dana Reyes (dana.reyes@example.com) as a user in the Dallas site.
    ```

---

!!! warning "Never retry an unknown outcome blindly"
    A `partial` result lists which step failed. Verify with `read_users` before retrying.

---

## read_call_queues

Read-only lookup of call queues, their members, overflow settings, and member availability. Never changes anything.

How phones ring (round robin, simultaneous, fixed order) is part of call handling rules and is not returned here.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | Optional | What it returns |
|--------|----------|----------|-----------------|
| `list` | `page`, `perPage` | `memberExtensionId` | Queues, optionally only those a given extension belongs to. |
| `get` | `callQueueId` | — | One queue with its service-level settings. |
| `list_members` | `callQueueId`, `page`, `perPage` | — | Member extension ids. Resolve names with [`read_users`](#read_users). |
| `get_overflow` | `callQueueId` | — | Overflow settings and destination queues. |
| `get_presence` | `callQueueId` | — | Each member's queue availability. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `callQueueId` | ✅ (most actions) | Numeric call queue id. |
| `memberExtensionId` | — | Only return queues this extension is a member of. |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_call_queues",
        "arguments": {
          "action": "list",
          "page": 1,
          "perPage": 50
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What call queues do we have, and who's in each one?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_call_routing

Read-only inspection of how inbound calls are routed — IVR menus, business hours, company answering rules, the forward-all override, per-extension call-handling rules, and what a given phone number actually rings.

It describes the configured routing; it does not simulate a call or evaluate business hours.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | Optional | What it returns |
|--------|----------|----------|-----------------|
| `get_ivr` | — | `menuId` | All IVR menus, or one menu with its prompt and key-press destinations. |
| `get_business_hours` | — | `extensionId` | Company weekly hours, or one extension's. |
| `get_company_rules` | `page`, `perPage` | `ruleId` | Company answering rules, or one rule. |
| `get_forward_all` | — | — | The company forward-all override. |
| `get_extension_rules` | `extensionId` | — | One extension's call-handling rules — names and enabled state only. Ring groups and conditions are not returned. |
| `get_by_number` | `phoneNumber` | — | What the number rings: an IVR menu with its key-press destinations, a call queue with overflow, a user extension, or — for a company number — the enabled company rules and forward-all state. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `menuId` | — | Omit to list all IVR menus. |
| `extensionId` | — | Omit for company business hours; set for one extension. Required for `get_extension_rules`. |
| `ruleId` | — | Omit to list company answering rules. |
| `phoneNumber` | ✅ (get_by_number) | 7–15 digits, optionally with a leading `+`. |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_call_routing",
        "arguments": {
          "action": "get_by_number",
          "phoneNumber": "+14155550123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Where does our main number actually ring? Walk me through the routing.
    ```

---

!!! info "Mixed APIs"
    Company-level reads use RingCentral's legacy call-handling API because no replacement exists. Extension-level reads use the newer API, which some legacy-routing accounts may not support.

---

## read_ivr_media

Read-only lookup of the account's IVR audio prompt metadata — id, filename, and content type. It does not return audio bytes or download links.

Use [`read_call_routing`](#read_call_routing) with `get_ivr` to see which menus use a prompt.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | What it returns |
|--------|----------|-----------------|
| `list` | — | All prompts on the account. |
| `get` | `promptId` | One prompt. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `list` or `get`. |
| `promptId` | ✅ (get) | Prompt id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_ivr_media",
        "arguments": {
          "action": "list"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What audio prompts do we have uploaded for our auto-attendant?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_phone_numbers

Read-only lookup of the account's existing phone numbers and what each is assigned to. This reads current inventory only — it cannot search for or buy new numbers.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | Optional | What it returns |
|--------|----------|----------|-----------------|
| `list` | `page`, `perPage` | `type`, `usageType`, `status`, `tollType`, `phoneNumber` | One page of numbers. |
| `get` | `phoneNumberId` | — | One number by its numeric id. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `list` or `get`. |
| `phoneNumberId` | ✅ (get) | Numeric phone number id. |
| `type` | — | Array of `VoiceFax`, `VoiceOnly`, `FaxOnly`. |
| `usageType` | — | Array of usage types, e.g. `MainCompanyNumber`, `DirectNumber`, `Inventory`, `AdditionalCompanyNumber`, `CompanyNumber`, `PhoneLine`, `CompanyFaxNumber`, `ForwardedNumber`, `ForwardedCompanyNumber`, `ContactCenterNumber`, `ConferencingNumber`, `MeetingsNumber`, `NumberStorage`, `BusinessMobileNumber`. |
| `status` | — | `Normal`, `Pending`, `PortedIn`, `Temporary`, or `Unknown`. |
| `tollType` | — | `Toll` or `TollFree`. |
| `phoneNumber` | — | Exact or partial phone number to filter by. |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_phone_numbers",
        "arguments": {
          "action": "list",
          "page": 1,
          "perPage": 50,
          "usageType": ["Inventory"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Which phone numbers do we have sitting unused in inventory?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_roles

Read-only lookup of user roles and permission definitions. Never changes anything.

To see which roles a specific user has, use [`read_users`](#read_users) with `action: "get_assignments"`.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | Optional | What it returns |
|--------|----------|----------|-----------------|
| `list_roles` | `page`, `perPage` | `customOnly` | Roles on the account. |
| `get_role` | `roleId` | — | One role with its permission ids. |
| `list_assignable` | `extensionId`, `page`, `perPage` | — | Roles the administrator may assign to one user. |
| `list_permissions` | `page`, `perPage` | `assignableOnly` | Permission definitions. |
| `get_permission` | `permissionId` | — | An explanation of one permission. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `roleId` | ✅ (get_role) | Role id. |
| `extensionId` | ✅ (list_assignable) | Numeric id of the user whose assignable roles to list. |
| `permissionId` | ✅ (get_permission) | Permission id. |
| `customOnly` | — | When true, return only custom roles defined by this account. |
| `assignableOnly` | — | When true, return only assignable permissions. |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_roles",
        "arguments": {
          "action": "list_roles",
          "page": 1,
          "perPage": 50,
          "customOnly": true
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What custom roles have we defined, and what can each one do?
    ```

---

!!! info "list_assignable needs the RoleManagement scope"
    RingCentral answers `403 BIL-103` for this lookup on some accounts — fall back to `list_roles` when that happens.

---

## read_sites

Read-only lookup of the account's sites, their members, and their IVR top menus. Never changes anything.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | What it returns |
|--------|----------|-----------------|
| `list` | — | All sites. |
| `get` | `siteId` | One site. |
| `list_members` | `siteId`, `page`, `perPage` | Extensions assigned to the site. |
| `get_ivr` | `siteId` | The site's IVR top menu and key actions. |
| `recommend_extension_prefix` | — | An unused leading extension digit for a new site, inferred from how existing sites number their extensions. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `siteId` | ✅ (get, list_members, get_ivr) | Site id from `list`. The literal id `main-site` is not accepted for these actions. |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_sites",
        "arguments": {
          "action": "list"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List our RingCentral sites and how many people are in each.
    ```

---

!!! info "recommend_extension_prefix is advisory"
    It returns its evidence alongside the suggestion, and the prefix is not reserved.

---

## read_users

Read-only lookup of users and other extensions in the authenticated administrator's own account. Never changes anything. For the authenticated user's own settings, use the [RingEX Phone](../servers/ringex-phone.md) tools instead.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Actions

| Action | Required | Optional | What it returns |
|--------|----------|----------|-----------------|
| `list` | `page`, `perPage` | `status`, `type`, `extensionNumber`, `email` | One page of extensions, with exact-match filters. |
| `search` | `text` | `status`, `type` | Extensions matching name, email, or extension number within a bounded scan. The result reports whether the scan was complete. |
| `get` | `extensionId` | — | One extension. |
| `get_assignments` | `extensionId` | — | The roles and administered sites assigned to one extension. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of the actions above. |
| `extensionId` | ✅ (get, get_assignments) | Numeric RingCentral extension id, as returned by `list` or `search`. |
| `text` | ✅ (search) | Case-insensitive text matched against name, email, and extension number. At least 2 characters. |
| `status` | — | Array of `Enabled`, `Disabled`, `Frozen`, `NotActivated`, `Unassigned`. |
| `type` | — | Array of `User`, `VirtualUser`, `DigitalUser`, `FlexibleUser`, `Limited`, `Department`, `Announcement`, `Voicemail`, `PagingOnly`, `SharedLinesGroup`, `ParkLocation`, `IvrMenu`. `Department` is the legacy API name for a call queue. |
| `extensionNumber` | — | Exact extension number (list only). |
| `email` | — | Exact email address (list only). |
| `page` | ✅ (list actions) | Page number, 1–1000. Defaults to 1. |
| `perPage` | ✅ (list actions) | Results per page, 1–100. Defaults to 50. |

---

### Examples

=== "Search by name"

    ```json
    {
      "action": "search",
      "text": "reyes",
      "type": ["User"]
    }
    ```

=== "List disabled users"

    ```json
    {
      "action": "list",
      "page": 1,
      "perPage": 50,
      "status": ["Disabled"]
    }
    ```

=== "Claude prompt"

    ```
    Find Dana Reyes in our account and tell me what roles she has.
    ```

---

!!! info "Requires an administrator"
    The caller needs permission to read extensions.

---

## release_phone_number

Removes an unused phone number from the account's inventory. Only numbers with `Inventory`, `ForwardedNumber`, or `ForwardedCompanyNumber` usage can be released. Numbers in use — direct numbers, the main company number, additional company numbers — are returned as `blocked` with the reason and must be moved off their role first.

There is no unassign action, because RingCentral offers no operation that returns an assigned number to inventory.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Destructive — confirmation required

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `release`. |
| `phoneNumberId` | ✅ | Number to release, from [`read_phone_numbers`](#read_phone_numbers). |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "release_phone_number",
        "arguments": {
          "action": "release",
          "phoneNumberId": "14155550199"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Release that spare inventory number we're not using — +1 415 555 0199.
    ```

---

!!! danger "Recovery is not guaranteed"
    Whether a released number can be recovered needs live validation. Usage is read from the v2 phone-number list; a number that list does not return is treated as in use.

---

## search_admin_audit_log

Read-only search of the account's configuration audit trail — who changed what and when. Filter by time range (at most 180 days), the administrator who acted, the affected extension, site, exact action ids, or free text.

Secrets and credential-like changed values are redacted, and client IP addresses are omitted.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `eventTimeFrom` | — | Start of the range (ISO 8601). Defaults to 7 days before `eventTimeTo`. |
| `eventTimeTo` | — | End of the range (ISO 8601). Defaults to now. |
| `actorExtensionIds` | — | Only events initiated by these extension ids — the administrator who made the change. Up to 20. |
| `targetExtensionIds` | — | Only events affecting these extension ids — the user or object that was changed. Up to 20. |
| `siteId` | — | Only events for this site. |
| `actionIds` | — | Exact audit action ids to include, e.g. `CHANGE_USER_INFO`. Up to 20. |
| `excludeActionIds` | — | Action ids to exclude. Up to 20. |
| `searchText` | — | Substring matched against initiator and target name, extension number, role, and changed values. |
| `page` | — | Page number, 1–1000. Defaults to 1. |
| `perPage` | — | Results per page, 1–100. Defaults to 25. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "search_admin_audit_log",
        "arguments": {
          "eventTimeFrom": "2026-10-01T00:00:00Z",
          "eventTimeTo": "2026-10-13T00:00:00Z",
          "actionIds": ["CHANGE_USER_INFO"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Who changed user settings in our account over the past two weeks?
    ```

---

!!! info "Narrow rather than page deeply"
    RingCentral returns at most 10,000 records per search. Tighten the range or filters instead of paging through everything.

---

## set_emergency_call_redirect

Switches the company-wide "forward all calls" override on or off, for a temporary closure or emergency. This affects every inbound company call.

RingCentral only lets this tool toggle the override — the destination and time ranges are read from the existing account configuration and cannot be changed here, so confirm the destination shown in the preview before enabling.

**Server:** [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Write — confirmation required

---

### Actions

| Action | Required | Optional | What it does |
|--------|----------|----------|--------------|
| `enable` | — | `acknowledgeDisconnect`, `confirmationToken` | Turns the forward-all override on. |
| `disable` | — | `confirmationToken` | Turns it off. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `enable` or `disable`. |
| `acknowledgeDisconnect` | — | `true`, required only when the configured forward-all action disconnects callers. Confirms that callers will be disconnected rather than forwarded. |
| `confirmationToken` | — | Token from the preview call. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "set_emergency_call_redirect",
        "arguments": {
          "action": "enable"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    The office is closed for the storm — turn on our company-wide call forwarding.
    ```

---

!!! danger "Enabling is refused without a usable destination"
    The override needs the `Bypass` action with a destination, the `Operator` action, or the `Disconnect` action with `acknowledgeDisconnect: true`. The result reads the setting back to verify it. Uses RingCentral's legacy company call-handling API because no replacement exists.

---
