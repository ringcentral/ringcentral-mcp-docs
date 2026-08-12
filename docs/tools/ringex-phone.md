# RingEX Phone — Tools Reference

Full reference for every tool available on the [RingEX Phone](../servers/ringex-phone.md) server. As of **v1.1.0**, the 24 fine-grained `platform_*`/`read_*`/`list_*` tools have been replaced with 12 workflow-oriented tools. Every tool is scoped to the authenticated user's own data — account, extension, and pagination selectors are not exposed as parameters.

Tools are listed alphabetically within each capability area — use the on-page navigation ("On this page") to jump to a specific tool.

!!! tip "Exact schemas live in `tools/list`"
    The tables below document parameters, types, and constraints as of this writing, but the authoritative schema for a given tool — including any new enum values or fields — is always visible by calling `tools/list` on the server.

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

## get_my_phone

Returns a bounded, read-only view of the authenticated RingCentral user's extension number, personal direct or business-mobile numbers, minimal Phone presence, business-hours schedule, and Business Hours/After Hours call-handling rules. There is no account, extension, rule, presence, or paging selector — this tool always describes the caller's own profile. It never changes presence, Do Not Disturb, forwarding, hours, or answering rules; it only reads them.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

This tool takes no parameters.

---

### Returns

The authenticated user's extension number, personal/business-mobile numbers, a minimal presence projection, business-hours schedule, and Business Hours/After Hours call-handling (answering) rules.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_phone",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What's my extension number and current call-handling setup?
    ```

---

## resolve_directory_person

Resolves a person in the company directory by name, department, or job title. "Role" means job title, not an administrative permission — this tool does not search the caller's personal address book (use `search_my_contacts` for that) and does not perform directory administration. Presence is only included when the selector produces a single, unique, exact match.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

!!! note "Company directory management moved"
    `platform_list_directory_entries`, `platform_read_directory_entry`, and `search_directory_entries` are replaced by this tool. It is scoped to finding a person to call or text — not to directory administration. For Team Chat person resolution, use [RingEX Chat](../servers/ringex-chat.md)'s `find_person` instead of the retired `team_messaging_get_person`.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `selector` | ✅ | One of `{ "kind": "name", "value": "…" }`, `{ "kind": "department", "value": "…" }`, or `{ "kind": "role", "value": "…" }` (`value` max 128 characters). `role` matches job title, not an admin permission. |
| `includePresence` | — | Boolean, defaults to `true`. Presence is only populated when the selector resolves to a single, unique, exact match. |

---

### Returns

The resolved directory person (or candidate list if ambiguous), optionally including presence when there is a single exact match.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "resolve_directory_person",
        "arguments": {
          "selector": { "kind": "name", "value": "Ada Lovelace" }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up Ada Lovelace in the company directory.
    ```

---

## search_my_contacts

Searches the authenticated user's personal address book by name or phone number. This is the caller's own contacts only — not the company directory — and excludes fields like email, notes, birthdays, and addresses.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `selector` | ✅ | One of `{ "kind": "name", "value": "…" }` or `{ "kind": "phone_number", "value": "+1…" }` (E.164 format). |

---

### Returns

Matching personal address-book contacts (name and phone number fields only).

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "search_my_contacts",
        "arguments": {
          "selector": { "kind": "phone_number", "value": "+14155551234" }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Do I have a personal contact saved for +1 415 555 1234?
    ```

---

## get_my_call_activity

Gets the authenticated user's complete personal voice-call activity for a bounded time window: recent and missed calls, returned calls, total connected-call time, longest call, repeated unsuccessful callers, and outstanding callbacks. The server reads every page in the window before calculating results; account, extension, and pagination selectors are intentionally not exposed.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `dateFrom` | ✅ | Inclusive lower bound, ISO-8601 date-time with offset (e.g. `2026-08-01T00:00:00.000Z`). |
| `dateTo` | ✅ | Inclusive upper bound, ISO-8601 date-time with offset. |
| `phoneNumber` | — | Filters activity to one phone number (max 64 characters). |

---

### Returns

Aggregated call activity for the window: recent/missed/returned calls, total connected-call time, longest call, repeated unsuccessful callers, and outstanding callbacks.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_call_activity",
        "arguments": {
          "dateFrom": "2026-08-05T00:00:00.000Z",
          "dateTo": "2026-08-12T00:00:00.000Z"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Summarize my call activity for the past week, including any missed calls I still owe a callback.
    ```

---

## get_my_call_insight

Gets AI notes and transcript text for one call in the authenticated user's personal call history. Pass the call id returned by `get_my_call_activity` or `search_my_call_insights`. This tool does not return recording audio — use `get_my_call_recording_metadata` to check for recording metadata.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `callId` | ✅ | Id of a call from the caller's own history (max 256 characters). |

---

### Returns

AI-generated notes and transcript text for the call, when available. No recording audio is returned.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_call_insight",
        "arguments": { "callId": "1234567890123" }
      }
    }
    ```

=== "Claude prompt"

    ```
    What were the AI notes from my call with Priya this morning?
    ```

---

## get_my_call_recording_metadata

Checks whether one call in the authenticated user's personal call history has embedded recording metadata. Returns a safe call projection plus a deduplicated count and the recording modes present — never call or recording ids, URIs, content locations, or audio.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `callId` | ✅ | Id of a call from the caller's own history. |

---

### Returns

A safe call projection, a deduplicated recording count, and the recording mode(s) present (e.g. automatic/on-demand) — no ids, URIs, content locations, or audio.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_call_recording_metadata",
        "arguments": { "callId": "1234567890123" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Was my last call with the support team recorded?
    ```

---

## search_my_call_insights

Searches the authenticated user's personal calls by person, topic, and date window. `topic` is a literal, Unicode-normalized lexical substring match against searchable AI content — not semantic search. Setting `semanticCandidateMode: "all_calls"` explicitly returns searchable AI content for every bounded candidate in the window, capped at 25 calls or 1,000,000 shared characters, whichever comes first.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `dateFrom` | ✅ | Inclusive lower bound, ISO-8601 date-time with offset. |
| `dateTo` | ✅ | Inclusive upper bound, ISO-8601 date-time with offset. |
| `person` | — | One of `{ "kind": "phone_number", "value": "…" }` (max 64 characters) or `{ "kind": "extension_number", "value": "…" }` (digits only, max 20 characters). |
| `topic` | — | Literal substring to match against searchable AI content, Unicode-normalized (2–256 characters). Not a semantic query. |
| `semanticCandidateMode` | — | Only supported value is `"all_calls"` — returns searchable AI content for every bounded candidate call (capped at 25 calls / 1,000,000 shared characters). |

---

### Returns

Matching calls with a safe projection plus, depending on the request, topic-matched excerpts or full searchable AI content per candidate.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "search_my_call_insights",
        "arguments": {
          "dateFrom": "2026-07-01T00:00:00.000Z",
          "dateTo": "2026-08-12T00:00:00.000Z",
          "topic": "renewal"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Find any calls from the last month where renewal pricing came up.
    ```

---

## get_my_communication_inbox

Gets the authenticated user's SMS, voicemail, and fax records for a bounded date window, newest first. Excludes shared mailboxes, Pager, internal Text, and Team Chat. Returns a strict minimal projection — no owner/account/extension ids or raw media.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `dateFrom` | ✅ | Inclusive lower bound, ISO-8601 date-time with offset. |
| `dateTo` | ✅ | Inclusive upper bound, ISO-8601 date-time with offset. |
| `messageTypes` | — | Array of `SMS`, `VoiceMail`, `Fax` (max 3 items). Defaults to all three. |
| `direction` | — | `Inbound` or `Outbound`. |
| `keyword` | — | SMS subject text or fax cover-page text only (2–128 characters). Requires exactly one `messageTypes` value. Does not search voicemail transcription or fax PDF/OCR content. |
| `participantPhoneNumber` | — | E.164 phone number of a participant on either side of the conversation. |
| `senderPhoneNumber` | — | E.164 phone number of the sender. |
| `readStatus` | — | `Read` or `Unread`. |

---

### Returns

Matching SMS/voicemail/fax records, newest first, with a minimal projection (no owner/account/extension ids or raw media).

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_communication_inbox",
        "arguments": {
          "dateFrom": "2026-08-05T00:00:00.000Z",
          "dateTo": "2026-08-12T00:00:00.000Z",
          "messageTypes": ["VoiceMail"],
          "readStatus": "Unread"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my unread voicemails from this week.
    ```

---

## get_my_message_detail

Reads one SMS, voicemail, or fax record from the authenticated user's own message store, identified by `messageId`. May retrieve a verified voicemail transcription. Never exposes attachment ids, URIs, audio, binary, or base64 content.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `messageId` | ✅ | Id of the message record (numeric string, up to 16 digits). |

---

### Returns

The message record's metadata and, for voicemail, a verified transcription when available. No attachment ids, URIs, or binary/audio content are returned.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_message_detail",
        "arguments": { "messageId": "1234567890" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Read me that voicemail from earlier today.
    ```

---

## get_my_sms_thread

Gets a bounded window of one SMS conversation for the authenticated user, oldest first. Returns a minimal projection — no conversation/owner/account/extension ids or MMS binary content.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `messageId` | ✅ | Id of one message in the target SMS conversation. |
| `dateFrom` | ✅ | Inclusive lower bound, ISO-8601 date-time with offset. |
| `dateTo` | ✅ | Inclusive upper bound, ISO-8601 date-time with offset. |

---

### Returns

Messages in the conversation window, oldest first, with a minimal projection (no conversation/owner/account/extension ids or MMS binary content).

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_my_sms_thread",
        "arguments": {
          "messageId": "1234567890",
          "dateFrom": "2026-08-01T00:00:00.000Z",
          "dateTo": "2026-08-12T00:00:00.000Z"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my text thread with that number from the last week and a half.
    ```

---

## send_sms

Sends one SMS from a phone number the authenticated user owns. Requires the sender to be an SMS-capable personal number owned by the authenticated extension, and the recipient to differ from the sender. Before this tool is invoked, a compatible host must show the final sender, recipient, and exact text and obtain the user's explicit approval — never send silently. Retries must use a fresh `requestId`; never retry an unknown result with the same or a new UUID against the same intended send.

**Server:** [RingEX Phone](../servers/ringex-phone.md)  
**Access:** Write

!!! warning "Confirm before sending"
    This tool is customer-facing and irreversible once delivered. Always restate the sender, recipient, and exact text back to the user and get an explicit yes before calling it.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `senderPhoneNumber` | ✅ | E.164 number (`+` followed by 7–15 digits) that is SMS-capable and owned by the authenticated extension. |
| `recipientPhoneNumber` | ✅ | E.164 number, must differ from `senderPhoneNumber`. |
| `text` | ✅ | Message body (max 1,000 characters). |
| `requestId` | ✅ | A UUID unique to this send attempt. Never reuse a `requestId` to retry after an unknown/ambiguous result. |

---

### Returns

Delivery status for the sent SMS.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "send_sms",
        "arguments": {
          "senderPhoneNumber": "+14155551234",
          "recipientPhoneNumber": "+14155556789",
          "text": "Running 10 minutes late, see you soon.",
          "requestId": "8f14e45f-ceea-4e79-9d68-2a5e8e5c9a3f"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Text +1 415 555 6789 from my number: "Running 10 minutes late, see you soon."
    ```

---

!!! note "Directory administration and Team Chat person lookup live elsewhere"
    Bulk directory administration is not exposed on this server. For Team Chat person resolution, use [RingEX Chat](../servers/ringex-chat.md)'s `find_person`.
