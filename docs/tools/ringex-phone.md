# RingEx Phone — Tools Reference

Full reference for every tool available on the [RingEx Phone](../servers/ringex-phone.md) server. Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

---

## about_ringcentral_mcp_tools

Call this first when you want to know what a RingEx MCP server can do, what tools are available, or which RingCentral tasks are supported. Returns a concise overview of the available tool categories and representative tool names for the connected server.

**Available on:** [RingEx Phone](../servers/ringex-phone.md) · [RingEx Chat](../servers/ringex-chat.md) · [RingEx Admin](../servers/ringex-admin.md)  
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
    Run this tool right after connecting a new RingEx server to confirm which capabilities and tools are exposed, before calling `tools/list` for exact schemas.

---

## list_message_store_records

Lists RingCentral message-store records — SMS, voicemail, fax, and pager messages. Use `messageType` to scope results to one message category, and filter by conversation, direction, read status, or date range. Message-store conversation ids are specific to SMS/message-store threads and are not the same as Team Messaging (Glip) chat ids.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `messageType` | — | Message category to return: `Fax`, `SMS`, `VoiceMail`, or `Pager`. Do not use this for Team Messaging or Glip posts. |
| `conversationId` | — | Message-store conversation id used to filter records in one SMS or message-store thread. Not a Team Messaging chat id. |
| `direction` | — | Message direction filter: `Inbound` or `Outbound`. Leave empty to include both. |
| `readStatus` | — | Read status filter: `Read` or `Unread`. Useful for finding unread voicemail or SMS. |
| `dateFrom` | — | Inclusive lower bound for message creation time, as an ISO-8601 date/time (e.g. `2026-05-01T00:00:00.000Z`). |
| `dateTo` | — | Upper bound for message creation time, as an ISO-8601 date/time. Pair with `dateFrom` for a bounded range. |
| `phoneNumber` | — | Phone number used to filter SMS or fax message-store records. |
| `distinctConversations` | — | When set, groups results to one record per conversation instead of every message. |

Account and extension context default to the current authenticated user and are not user-supplied parameters.

---

### Returns

Returns the raw RingCentral message-store list response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "list_message_store_records",
        "arguments": {
          "messageType": "VoiceMail",
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

!!! info "Permission"
    This tool requires **read** access.

---

## list_user_call_log

Lists RingCentral call-log records for the authenticated extension, or another extension when its id is known. Use this for recent calls, missed calls, inbound/outbound history, or call history filtered by date range or phone number. It does not return SMS, voicemail, or Team Messaging posts.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `extensionId` | — | RingCentral extension id whose call log should be listed; defaults to `"~"` (the authenticated extension). Use directory search first if only a name is known. |
| `dateFrom` | — | Inclusive lower bound for call start time, as an ISO-8601 date/time (e.g. `2026-05-01T00:00:00.000Z`). |
| `dateTo` | — | Upper bound for call start time, as an ISO-8601 date/time. Pair with `dateFrom` for a bounded range. |
| `direction` | — | Call direction filter: `Inbound` or `Outbound`. Leave empty to include both. |
| `phoneNumber` | — | Phone number used to filter call-log records. |
| `page` | — | Result page number. Defaults to `1`. |
| `perPage` | — | Maximum number of call-log records to return in one page. Defaults to `100`. |

---

### Returns

Returns the raw RingCentral call-log response.

| Field | Description |
|-------|-------------|
| `records[].telephonySessionId` | Telephony session id that can be used to read AI notes when available (see [`read_call_ai_notes`](#read_call_ai_notes)). |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "list_user_call_log",
        "arguments": {
          "direction": "Inbound",
          "dateFrom": "2026-07-08T00:00:00.000Z",
          "dateTo": "2026-07-15T00:00:00.000Z"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my missed calls from the last week.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## message_store_create_smsmessage

Sends an SMS text message through the RingCentral message store. Use it when the recipient phone number and message text are both known. This does not send Team Messaging/Glip posts, and it should not be used to list or search existing SMS records.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `senderPhoneNumber` | — | SMS sender phone number. Omit to use the authenticated user's default SMS sender — do not ask the user for a sender solely because it was omitted. |
| `recipientPhoneNumbers` | ✅ | One or more SMS recipient phone numbers (e.g. `"+15555550101"`). |
| `text` | ✅ | SMS message text. Preserve the user's requested wording exactly. |

Account and extension context default to the current authenticated user and are not user-supplied parameters.

---

### Returns

Returns the raw RingCentral SMS send response.

| Field | Description |
|-------|-------------|
| `id` | Message-store id for the sent SMS. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "message_store_create_smsmessage",
        "arguments": {
          "recipientPhoneNumbers": ["+15555550101"],
          "text": "I am running five minutes late."
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Text +1 555-555-0101 and let them know I'm running five minutes late.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## platform_get_account_info_v2

Retrieves account information for a RingCentral account. Use it when the account id is known (or defaults to the current authenticated account) and no narrower, more specific tool applies.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral response for `getAccountInfoV2`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_get_account_info_v2",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What's the status of my RingCentral account?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_administered_sites

Lists the RingCentral sites that a given extension administers. Use it when the account/extension ids are known (or default to the current authenticated context) and you need the list of sites the current user manages.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral response for `listAdministeredSites`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_administered_sites",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What sites do I administer in RingCentral?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_answering_rules

Lists the call handling (answering) rules configured for a RingCentral extension. Use it when the account/extension ids are known (or default to the current authenticated context) and you need to inspect how incoming calls are routed.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `type` | — | Filter by answering rule type. Use only when the user asks for this filter. |
| `view` | — | View option controlling the level of detail returned. Use only when the user asks for this filter. |

---

### Returns

Returns the raw RingCentral response for call handling (answering) rules.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_answering_rules",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my call handling rules.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_contacts

Lists entries in a RingCentral extension's personal address book. Use it when the account/extension ids are known (or default to the current authenticated context) and you need the user's saved contacts.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `startsWith` | — | Filter contacts whose name starts with this string. |
| `sortBy` | — | Field to sort results by. |
| `page` | — | Result page number. |
| `perPage` | — | Maximum number of contacts to return per page. |
| `phoneNumber` | — | Filter contacts by phone number. |

---

### Returns

Returns the raw RingCentral personal address-book response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_contacts",
        "arguments": {
          "startsWith": "J"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List my saved contacts whose name starts with J.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_directory_entries

Retrieves the full company directory entries for a RingCentral account. Use it when you need a bulk listing of directory entries rather than a search — for searching by name, email, or extension, use [`search_directory_entries`](#search_directory_entries) instead.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `accessibleSitesOnly` | — | When set, limits results to sites the caller can access. |
| `showFederated` | — | When set, includes federated directory entries from linked accounts. |
| `type` | — | Filter by directory entry type. |
| `typeGroup` | — | Filter by directory entry type group. |
| `page` | — | Result page number. |
| `perPage` | — | Maximum number of directory entries to return per page. |
| `siteId` | — | Filter directory entries by site id. |
| `If-None-Match` | — | Optional HTTP conditional-request header for caching. |

---

### Returns

Returns the raw RingCentral company directory entries response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_directory_entries",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the full company directory listing.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_extension_phone_numbers

Lists the phone numbers assigned to a RingCentral extension. Use it when the account/extension ids are known (or default to the current authenticated context) and you need to see which numbers are associated with the extension.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `status` | — | Filter by phone number status. |
| `usageType` | — | Filter by phone number usage type. |
| `page` | — | Result page number. |
| `perPage` | — | Maximum number of phone numbers to return per page. |

---

### Returns

Returns the raw RingCentral response for `listExtensionPhoneNumbers`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_extension_phone_numbers",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What phone numbers are assigned to my extension?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_favorite_contacts

Lists the contacts a RingCentral extension has marked as favorites. Use it when the account/extension ids are known (or default to the current authenticated context) and you need the user's favorited contacts.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral response for `listFavoriteContacts`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_list_favorite_contacts",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my favorite contacts.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_call_recording_content

Fetches the actual audio content of a RingCentral call recording by its recording id. Use [`platform_read_call_recording`](#platform_read_call_recording) first if you only have call metadata and need to find the recording id.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `recordingId` | ✅ | Recording id identifying the exact call recording whose content should be fetched. |
| `contentDisposition` | — | Content disposition to request from RingCentral (e.g. `Inline` or `Attachment`). |

---

### Returns

Returns raw call recording audio content. Binary content is returned as base64 with content-type metadata.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_call_recording_content",
        "arguments": {
          "recordingId": "8579513004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Play back the recording of my last call.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_call_recording

Retrieves metadata for a specific RingCentral call recording by its recording id. To retrieve the actual recorded audio, use [`platform_read_call_recording_content`](#platform_read_call_recording_content).

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `recordingId` | ✅ | Recording id identifying the exact call recording to read. |

---

### Returns

Returns the raw RingCentral response for `readCallRecording`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_call_recording",
        "arguments": {
          "recordingId": "8579513004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the details for call recording 8579513004.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_contact

Retrieves one entry from a RingCentral extension's personal address book by contact id. Use [`platform_list_contacts`](#platform_list_contacts) first if you only have a name and need to find the contact id.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `contactId` | ✅ | Contact id identifying the exact personal address-book entry to read. |

---

### Returns

Returns the raw RingCentral response for `readContact`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_contact",
        "arguments": {
          "contactId": "225451004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the details for contact 225451004 in my address book.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_directory_entry

Retrieves one entry from the RingCentral company directory by its entry id. Use [`search_directory_entries`](#search_directory_entries) first if you only have a name or other free-form selector and need to find the entry id.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `accessibleSitesOnly` | — | When set, limits the lookup to sites the caller can access. |
| `entryId` | ✅ | Directory entry id identifying the exact corporate directory record to read. |

---

### Returns

Returns the raw RingCentral response for `readDirectoryEntry`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_directory_entry",
        "arguments": {
          "entryId": "225451004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up directory entry 225451004.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_user_call_record

Retrieves a single RingCentral call-log record for an extension by its call record id. Use [`list_user_call_log`](#list_user_call_log) first to find the id of the specific call you want details for.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `callRecordId` | ✅ | Call record id identifying the exact call-log entry to read. |
| `view` | — | View option controlling the level of detail returned. |

---

### Returns

Returns the raw RingCentral response for `readUserCallRecord`.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_user_call_record",
        "arguments": {
          "callRecordId": "8579513004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the full details of that last call record.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_user_presence_status

Retrieves the presence status for a RingCentral extension — available, busy, on a call, do-not-disturb, and related telephony state. Account and extension context default to the current authenticated user when not specified.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | RingCentral account id. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | RingCentral extension id. Omit or use `"~"` for the authenticated RingCentral context. |
| `detailedTelephonyState` | — | When set, includes detailed telephony state information in the response. |
| `sipData` | — | When set, includes SIP session data in the response. |

---

### Returns

Returns the raw RingCentral presence status response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "platform_read_user_presence_status",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What's my current presence status?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_call_ai_notes

Reads RingCentral AI-generated notes and transcript details for a specific call, identified by its telephony session id. Requires the telephony session id from a call-log record — if you only have a phone number or a broad call-history request, use [`list_user_call_log`](#list_user_call_log) first to find it.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `ownerExtensionId` | — | Extension id that owns the call AI notes; defaults to `"~"` (the authenticated extension). Use the owner extension from call-log context when known. |
| `telephonySessionId` | ✅ | Telephony session id from a RingCentral call-log record. Do not use message ids or Team Messaging post ids here. |

---

### Returns

Returns raw AI notes and transcript data for the call, when available.

| Field | Description |
|-------|-------------|
| `callNote.summary` | AI-generated call summary. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_call_ai_notes",
        "arguments": {
          "telephonySessionId": "telephony-123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Summarize the AI notes for my call with Jane this morning.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_extension_profile

Reads RingCentral extension profile details for the authenticated extension, or another extension when its id is known. If you only have a free-form name, run a directory search first to resolve the extension id.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `extensionId` | — | RingCentral extension id to read; defaults to `"~"` (the authenticated extension). |

Account context defaults to the current authenticated user and is not a user-supplied parameter.

---

### Returns

Returns the raw RingCentral extension profile response.

| Field | Description |
|-------|-------------|
| `id` | Extension id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_extension_profile",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What's my RingCentral extension profile look like?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_message_store_content

Fetches attachment content from a RingCentral message-store record — voicemail audio, transcripts, fax content, or other attachments. Requires both a message id and an attachment id; if you only have a message id (for example, a voicemail id), read the message-store record first with [`read_message_store_record`](#read_message_store_record) to find the attachment id. This does not fetch Team Messaging file content.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `messageId` | ✅ | Message-store message id that owns the attachment. Do not use Team Messaging post ids. |
| `attachmentId` | ✅ | Message attachment id from message-store metadata. Usually comes from `attachments[].id` on the output of [`read_message_store_record`](#read_message_store_record). |
| `contentDisposition` | — | Optional content disposition requested from RingCentral (e.g. `Inline`). |
| `contentDispositionFilename` | — | Optional filename to use with `contentDisposition`. |

Account and extension context default to the current authenticated user and are not user-supplied parameters.

---

### Returns

Returns raw message-store attachment content. Binary content is returned as base64 with content-type metadata.

| Field | Description |
|-------|-------------|
| `content` | Base64 content when the RingCentral response is binary. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_message_store_content",
        "arguments": {
          "messageId": "555",
          "attachmentId": "1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Play back that voicemail I just got.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_message_store_record

Reads one RingCentral message-store record by message id, returning its metadata. Use it when you have an SMS, voicemail, fax, or pager message-store id and need its details — for example, before fetching voicemail attachment content when only the voicemail id is known. The message id must come from RingCentral message-store APIs, not from a Team Messaging chat or post id; if a user just says "message 123" without other context, clarify whether they mean a message-store message or a Team Messaging post.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `messageId` | ✅ | RingCentral message-store message id. Use ids from message-store list results or user-provided voicemail/message ids. Do not use Team Messaging chat ids here. |

Account and extension context default to the current authenticated user and are not user-supplied parameters.

---

### Returns

Returns raw metadata for one message-store record.

| Field | Description |
|-------|-------------|
| `attachments[].id` | Attachment id to use with [`read_message_store_content`](#read_message_store_content). |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_message_store_record",
        "arguments": {
          "messageId": "555"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the details of voicemail message 555.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_user_presence

Reads RingCentral unified presence for the authenticated extension, or another extension when its id is known — whether the user is available, busy, on a call, or in do-not-disturb. If you only have a free-form name or email, run a directory search first to resolve the extension id.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `extensionId` | — | RingCentral extension id whose presence should be read; defaults to `"~"` (the authenticated extension). |

Account context defaults to the current authenticated user and is not a user-supplied parameter.

---

### Returns

Returns the raw RingCentral unified presence response.

| Field | Description |
|-------|-------------|
| `presenceStatus` | Overall user presence status. |
| `telephonyStatus` | Telephony availability or call state. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "read_user_presence",
        "arguments": {
          "extensionId": "101"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Is Jane available right now?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## search_directory_entries

Searches RingCentral company directory entries by name, extension number, email, or other selector. Use this to resolve a RingCentral user or extension id from a free-form selector — if the exact extension id needed by another tool is already known, this lookup is unnecessary. The search may return multiple candidates; do not guess when more than one person matches a request.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `searchString` | — | Text to search in RingCentral directory entries — names, emails, or extension numbers. |
| `page` | — | Result page number. |
| `perPage` | — | Maximum number of directory entries to return. Defaults to `20`. Keep small when disambiguating between similarly named people. |

Account context defaults to the current authenticated user and is not a user-supplied parameter.

---

### Returns

Returns raw directory search results.

| Field | Description |
|-------|-------------|
| `records[].id` | Extension id that can be used by extension and presence endpoints. |
| `records[].email` | User email, useful for disambiguation. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "search_directory_entries",
        "arguments": {
          "searchString": "Alex"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up Alex in the company directory.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_person

Retrieves a known RingCentral Team Messaging person by their Team Messaging person id. Use this when the request specifically references a Team Messaging person id (for example, "Get Team Messaging person 1021461048") — not for reading a RingCentral extension profile (use [`read_extension_profile`](#read_extension_profile) instead), and not when only a free-form name is given (run a directory search first). The `personId` is a Team Messaging person id, and it should not be treated as an extension id even if the numeric value looks similar.

**Server:** [RingEx Phone](../servers/ringex-phone.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `personId` | ✅ | Team Messaging person id to read (e.g. `"1021461048"`). |

---

### Returns

Returns the raw Team Messaging person response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging person id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_person",
        "arguments": {
          "personId": "1021461048"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get Team Messaging person 1021461048.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

