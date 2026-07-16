# RingEx Admin — Tools Reference

Full reference for every tool available on the [RingEx Admin](../servers/ringex-admin.md) server. Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

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

## platform_analytics_calls_aggregation_fetch

Runs an aggregation query against RingCentral's Call Analytics API, returning grouped or summarized call metrics (such as call volume or duration) for the account, sliced by whatever dimensions and filters you specify in the request body.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to query. Omit or use `"~"` for the authenticated RingCentral context. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |
| `body` | ✅ | JSON request body describing the aggregation — grouping dimensions, filters, and time range for the calls aggregation query. |

---

### Returns

Returns the raw RingCentral response for the calls aggregation query.

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
        "name": "platform_analytics_calls_aggregation_fetch",
        "arguments": {
          "body": {
            "grouping": {
              "groupBy": "Extension"
            },
            "timeSettings": {
              "timeRange": "Last7Days"
            }
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me call volume broken down by extension for the last 7 days.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_get_account_info_v2

Retrieves core account information for a RingCentral account — status, service plan, operator, and related account-level settings. Defaults to the authenticated user's own account when no `accountId` is given.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral account info response.

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
    What's the status of our RingCentral account?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_account_phone_numbers_v2

Lists phone numbers provisioned on the RingCentral account. Results can be filtered by number type, usage type, status, toll type, extension status, BYOC (Bring Your Own Carrier) numbers, or a specific phone number, and pagination is supported via `page` and `perPage`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |
| `type` | — | Filter by phone number type. |
| `usageType` | — | Filter by usage type (e.g. main company number, direct number, fax). |
| `status` | — | Filter by phone number status. |
| `tollType` | — | Filter by toll type (e.g. toll-free vs. local). |
| `extensionStatus` | — | Filter by the status of the extension the number is assigned to. |
| `byocNumber` | — | Filter to include or exclude BYOC numbers. |
| `phoneNumber` | — | Filter to a specific phone number. |

---

### Returns

Returns the raw RingCentral response listing account phone numbers.

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
        "name": "platform_list_account_phone_numbers_v2",
        "arguments": {
          "usageType": "MainCompanyNumber",
          "perPage": 50
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List all the toll-free numbers on our RingCentral account.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_account_switches

Lists the network switches registered for automatic emergency address updates on the account. Results can be filtered by site or a search string, sorted, and paginated.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `siteId` | — | Filter switches by site. |
| `searchString` | — | Filter switches by a search string. |
| `orderBy` | — | Field to sort results by. |
| `perPage` | — | Number of results to return per page. |
| `page` | — | Page number for paginated results. |

---

### Returns

Returns the raw RingCentral response listing account switches.

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
        "name": "platform_list_account_switches",
        "arguments": {
          "siteId": "12345"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List the network switches registered for emergency address auto-update at our main site.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_administered_sites

Lists the RingCentral sites that a given extension (typically an admin) is permitted to administer. Defaults to the current user's own extension when no `extensionId` is provided.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension to look up. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral response listing administered sites.

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
    Which sites am I allowed to administer on our RingCentral account?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_answering_rules

Lists the call handling (answering) rules configured for an extension — for example custom rules that route calls differently based on caller, time of day, or other conditions. Results can be filtered by rule type, view, or enabled status, and support pagination.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `type` | — | Filter by answering rule type. |
| `view` | — | Controls the level of detail returned. |
| `enabledOnly` | — | When true, only returns rules that are currently enabled. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |

---

### Returns

Returns the raw RingCentral response listing call handling rules.

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
        "name": "platform_list_answering_rules",
        "arguments": {
          "enabledOnly": true
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What call handling rules are currently active on my extension?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_contacts

Lists personal address book contacts for an extension. Supports filtering by name prefix or phone number, sorting, and pagination.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension whose address book to list. Omit or use `"~"` for the authenticated RingCentral context. |
| `startsWith` | — | Filter contacts whose name starts with this string. |
| `sortBy` | — | Field to sort results by. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |
| `phoneNumber` | — | Filter contacts by phone number. |

---

### Returns

Returns the raw RingCentral response listing address book contacts.

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
        "name": "platform_list_contacts",
        "arguments": {
          "startsWith": "Jan"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up my personal contacts whose name starts with "Jan".
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_directory_entries

Lists entries in the company directory (users, departments, and similar directory objects) for the account. Supports filtering by site accessibility, federation status, entry type or type group, and site, plus pagination.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `accessibleSitesOnly` | — | When true, only returns entries from sites the caller can access. |
| `showFederated` | — | When true, includes entries from federated accounts. |
| `type` | — | Filter by directory entry type. |
| `typeGroup` | — | Filter by directory entry type group. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |
| `siteId` | — | Filter entries by site. |

---

### Returns

Returns the raw RingCentral response listing company directory entries.

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
        "name": "platform_list_directory_entries",
        "arguments": {
          "typeGroup": "Employees"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me everyone in the company directory.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_extensions

Lists extensions (users, departments, IVR menus, and other extension types) on the account. Can be filtered by extension number, email address, status, or extension type, with pagination support.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionNumber` | — | Filter by extension number. |
| `email` | — | Filter by email address. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |
| `status` | — | Filter by extension status (e.g. Enabled, Disabled). |
| `type` | — | Filter by extension type (e.g. User, Department, IvrMenu). |

---

### Returns

Returns the raw RingCentral response listing extensions.

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
        "name": "platform_list_extensions",
        "arguments": {
          "status": "Enabled",
          "type": "User"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List all active user extensions on our RingCentral account.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_list_favorite_contacts

Lists the contacts an extension has marked as favorites.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension whose favorites to list. Omit or use `"~"` for the authenticated RingCentral context. |

---

### Returns

Returns the raw RingCentral response listing favorite contacts.

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

## platform_read_account_phone_number

Retrieves details for a single phone number on the account, identified by its `phoneNumberId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account the number belongs to. Omit or use `"~"` for the authenticated RingCentral context. |
| `phoneNumberId` | ✅ | ID of the phone number to retrieve. |

---

### Returns

Returns the raw RingCentral response for the phone number.

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
        "name": "platform_read_account_phone_number",
        "arguments": {
          "phoneNumberId": "402304004"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the details for phone number ID 402304004.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_account_presence

Retrieves the presence status (available, busy, on a call, etc.) for all extensions on the account. Optionally includes detailed telephony state or SIP data, with pagination support.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `detailedTelephonyState` | — | When true, includes detailed telephony state in the response. |
| `sipData` | — | When true, includes SIP registration data in the response. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |

---

### Returns

Returns the raw RingCentral response listing presence status for all extensions on the account.

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
        "name": "platform_read_account_presence",
        "arguments": {
          "perPage": 100
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the presence status of everyone on our RingCentral account.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_call_recording_content

Downloads the actual audio content of a call recording, identified by its `recordingId`. Optional parameters control how the content is delivered — inline versus as an attachment, and the filename used.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account the recording belongs to. Omit or use `"~"` for the authenticated RingCentral context. |
| `recordingId` | ✅ | ID of the call recording whose content to download. |
| `contentDisposition` | — | Controls whether the content is returned inline or as an attachment. |
| `contentDispositionFilename` | — | Filename to use when the content is returned as an attachment. |

---

### Returns

Returns the raw audio content of the call recording from RingCentral.

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
          "recordingId": "8302935008",
          "contentDisposition": "Attachment",
          "contentDispositionFilename": "call-recording.mp3"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Download the audio for recording ID 8302935008.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_call_recording

Retrieves metadata for a single call recording, identified by its `recordingId`. This returns information about the recording (such as duration and content type), not the audio itself — use [`platform_read_call_recording_content`](#platform_read_call_recording_content) to fetch the actual audio.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account the recording belongs to. Omit or use `"~"` for the authenticated RingCentral context. |
| `recordingId` | ✅ | ID of the call recording to retrieve. |

---

### Returns

Returns the raw RingCentral response describing the call recording.

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
          "recordingId": "8302935008"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the details of the recording with ID 8302935008.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_company_call_log

Lists call log records for the entire company (account-wide), not just a single extension. Supports extensive filtering — by extension number, phone number, call direction, call type, recording presence/type, date range, and session identifiers — plus pagination.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionNumber` | — | Filter by extension number. |
| `phoneNumber` | — | Filter by phone number involved in the call. |
| `direction` | — | Filter by call direction (e.g. Inbound, Outbound). |
| `type` | — | Filter by call type (e.g. Voice, Fax). |
| `view` | — | Controls the level of detail returned (e.g. Simple vs. Detailed). |
| `withRecording` | — | When true, only returns calls that have a recording. |
| `recordingType` | — | Filter by recording type (e.g. Automatic, OnDemand). |
| `dateFrom` | — | Start of the date range to filter by (ISO 8601). |
| `dateTo` | — | End of the date range to filter by (ISO 8601). |
| `sessionId` | — | Filter by call session ID. |
| `telephonySessionId` | — | Filter by telephony session ID. |
| `metadataCategory` | — | Filter by metadata category. |
| `page` | — | Page number for paginated results. |
| `perPage` | — | Number of results to return per page. |

---

### Returns

Returns the raw RingCentral response listing company-wide call log records.

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
        "name": "platform_read_company_call_log",
        "arguments": {
          "dateFrom": "2026-07-08T00:00:00.000Z",
          "dateTo": "2026-07-15T00:00:00.000Z",
          "direction": "Inbound"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me all inbound calls across the company from the past week.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_company_call_record

Retrieves one or more specific company call log records, identified by `callRecordId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `callRecordId` | ✅ | ID of the call record to retrieve. Multiple IDs may be comma-separated depending on the RingCentral API. |
| `view` | — | Controls the level of detail returned (e.g. Simple vs. Detailed). |

---

### Returns

Returns the raw RingCentral response for the requested company call record(s).

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
        "name": "platform_read_company_call_record",
        "arguments": {
          "callRecordId": "42342342342"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up the details of company call record 42342342342.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_contact

Retrieves a single personal address book contact by its `contactId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension whose address book contains the contact. Omit or use `"~"` for the authenticated RingCentral context. |
| `contactId` | ✅ | ID of the contact to retrieve. |

---

### Returns

Returns the raw RingCentral response for the requested contact.

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
          "contactId": "5837201"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the details for contact ID 5837201 in my address book.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_country

Retrieves reference data for a single country from RingCentral's country dictionary, identified by `countryId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `countryId` | ✅ | ID of the country to retrieve from RingCentral's country dictionary. |

---

### Returns

Returns the raw RingCentral response for the requested country.

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
        "name": "platform_read_country",
        "arguments": {
          "countryId": "1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up country dictionary entry 1 in RingCentral.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_directory_entry

Retrieves a single company directory entry by its `entryId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `accessibleSitesOnly` | — | When true, only returns the entry if it belongs to a site the caller can access. |
| `entryId` | ✅ | ID of the directory entry to retrieve. |

---

### Returns

Returns the raw RingCentral response for the requested directory entry.

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
          "entryId": "998877"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up directory entry 998877 in the company directory.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_directory_federation

Retrieves the federated account/directory relationships configured for multi-account or multi-brand setups on the account. Can be filtered by federation type.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `types` | — | Filter by federation type. |
| `RCExtensionId` | — | Extension ID to pass as a request header, if the API requires it for this call. |

---

### Returns

Returns the raw RingCentral response describing account directory federation.

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
        "name": "platform_read_directory_federation",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Is our RingCentral account federated with any other accounts?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_permission_category

Retrieves details for a single permission category from RingCentral's permission dictionary, identified by `permissionCategoryId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `permissionCategoryId` | ✅ | ID of the permission category to retrieve from RingCentral's permission dictionary. |

---

### Returns

Returns the raw RingCentral response for the requested permission category.

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
        "name": "platform_read_permission_category",
        "arguments": {
          "permissionCategoryId": "Administration"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What permissions fall under the Administration category in RingCentral?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_permission

Retrieves details for a single permission from RingCentral's permission dictionary, identified by `permissionId`.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `permissionId` | ✅ | ID of the permission to retrieve from RingCentral's permission dictionary. |

---

### Returns

Returns the raw RingCentral response for the requested permission.

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
        "name": "platform_read_permission",
        "arguments": {
          "permissionId": "EditUserInfo"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What does the EditUserInfo permission allow in RingCentral?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_user_presence_status

Retrieves the presence status for a single extension — available, busy, on a call, and similar states. Optionally includes detailed telephony state or SIP data. Defaults to the current user's own extension when omitted.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `accountId` | — | Account to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `extensionId` | — | Extension to look up. Omit or use `"~"` for the authenticated RingCentral context. |
| `detailedTelephonyState` | — | When true, includes detailed telephony state in the response. |
| `sipData` | — | When true, includes SIP registration data in the response. |

---

### Returns

Returns the raw RingCentral response with the extension's presence status.

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
        "name": "platform_read_user_presence_status",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What's my current presence status in RingCentral?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## platform_read_user_role

Retrieves details for a single user role — including the permissions it grants — identified by `roleId`. Optionally includes advanced permission details.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `roleId` | ✅ | ID of the user role to retrieve. |
| `accountId` | — | Account the role belongs to. Omit or use `"~"` for the authenticated RingCentral context. |
| `advancedPermissions` | — | When true, includes advanced permission details in the response. |

---

### Returns

Returns the raw RingCentral response for the requested user role.

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
        "name": "platform_read_user_role",
        "arguments": {
          "roleId": "48291"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    What permissions does the "Team Manager" role have? Its role ID is 48291.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## read_call_ai_notes

Retrieves AI-generated notes and transcript details for a specific call, identified by its telephony session ID. Use this when you already know the telephony session ID for a call (typically from a call-log record) and want the AI summary or transcript for it — a phone number or a broad call-history request alone isn't enough to use this tool.

**Server:** [RingEx Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `ownerExtensionId` | — | Extension that owns the call AI notes. Omit or use `"~"` for the authenticated extension; use the owner extension from the call-log context when known. |
| `telephonySessionId` | ✅ | Telephony session ID from a RingCentral call-log record. Do not use message IDs or Team Messaging post IDs here. |

---

### Returns

Returns raw RingCentral AI notes and transcript data for a call when available.

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
    Get the AI notes for the call with telephony session ID telephony-123.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

