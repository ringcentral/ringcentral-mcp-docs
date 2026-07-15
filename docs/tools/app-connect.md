# App Connect - Tools Reference

Full reference for every tool available on the [App Connect](../servers/app-connect.md) server. Tools are listed in the order shown on the overview page - use the on-page navigation to jump to a specific tool.

---

## getSessionInfo

Returns the current user's RingCentral identity and their CRM connection status. Use this tool to verify a session is active before calling tools that require CRM authentication.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** No

---

### Parameters

This tool takes no parameters.

---

### Returns

A session object containing:

| Field | Type | Description |
|-------|------|-------------|
| `rcUserId` | `string` | RingCentral user ID |
| `rcUserName` | `string` | Display name of the authenticated RC user |
| `rcExtension` | `string` | RC extension number |
| `crmConnected` | `boolean` | Whether a CRM platform is linked |
| `crmPlatform` | `string \| null` | Name of the connected CRM (e.g. `"Salesforce"`) |
| `crmUserId` | `string \| null` | User ID in the CRM system |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getSessionInfo",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Check my RingCentral session status and tell me which CRM I'm connected to.
    ```

=== "Sample response"

    ```json
    {
      "rcUserId": "12345678",
      "rcUserName": "Jane Smith",
      "rcExtension": "1042",
      "crmConnected": true,
      "crmPlatform": "Salesforce",
      "crmUserId": "0051g00000AbCdEAAZ"
    }
    ```

---

### Notes

- If `crmConnected` is `false`, calls to CRM-dependent tools will return an authentication error.
- Use this as a health-check at the start of automated workflows.

---

!!! tip "Related tools"
    - [`getPublicConnectors`](#getpublicconnectors) — see which CRM platforms are available to connect
    - [`logout`](#logout) — end the CRM session

---

## getPublicConnectors

Returns the list of CRM connectors publicly available through App Connect. Use this to show users which CRM platforms they can link to their RingCentral account.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** No

---

### Parameters

This tool takes no parameters.

---

### Returns

An array of connector objects:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique connector identifier |
| `name` | `string` | Human-readable CRM platform name |
| `logoUrl` | `string` | URL to the connector's logo image |
| `authType` | `string` | Authentication method (`"oauth2"`, `"apikey"`, etc.) |
| `status` | `string` | Availability status (`"available"`, `"beta"`, `"deprecated"`) |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getPublicConnectors",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me which CRM platforms I can connect to with RingCentral App Connect.
    ```

=== "Sample response"

    ```json
    [
      { "id": "salesforce", "name": "Salesforce", "authType": "oauth2", "status": "available" },
      { "id": "hubspot",    "name": "HubSpot",    "authType": "oauth2", "status": "available" },
      { "id": "zoho",       "name": "Zoho CRM",   "authType": "oauth2", "status": "available" },
      { "id": "dynamics",   "name": "MS Dynamics","authType": "oauth2", "status": "beta"      }
    ]
    ```

---

!!! tip "Related tools"
    - [`getSessionInfo`](#getsessioninfo) — check if a connector is already linked

---

## getHelp

Returns a quick-start guide describing what the App Connect integration can do and how to get started. Useful as an onboarding prompt when a user first connects the server to their AI client.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** No

---

### Parameters

This tool takes no parameters.

---

### Returns

A plain-text or markdown guide covering:

- What App Connect does
- How to authenticate with a CRM
- A summary of available tools and common workflows

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getHelp",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What can I do with the RingCentral App Connect integration?
    ```

---

### Notes

- This tool is safe to call before authentication is complete.
- Intended for use at session start or when a user asks "what can you do?"

---

!!! tip "Related tools"
    - [`getSessionInfo`](#getsessioninfo) — check current auth status
    - [`getPublicConnectors`](#getpublicconnectors) — list connectable CRMs

---

## findContactByName

Searches the connected CRM for contacts whose name matches the provided string. Returns contact details including phone numbers, email, and CRM record IDs.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `name` | `string` | ✅ | Full or partial name to search for (e.g. `"Jane"`, `"Jane Smith"`) |

---

### Returns

An array of matching contact objects:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID |
| `name` | `string` | Full name |
| `phone` | `string \| null` | Primary phone number |
| `email` | `string \| null` | Primary email address |
| `company` | `string \| null` | Associated company or account name |
| `crmUrl` | `string \| null` | Deep link to the record in the CRM UI |

Returns an empty array `[]` if no matches are found.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "findContactByName",
        "arguments": {
          "name": "Jane Smith"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up the contact "Jane Smith" in my CRM.
    ```

=== "Sample response"

    ```json
    [
      {
        "id": "0031g00000XxYyZAAZ",
        "name": "Jane Smith",
        "phone": "+14155550123",
        "email": "jane.smith@acme.com",
        "company": "Acme Corp",
        "crmUrl": "https://acme.salesforce.com/0031g00000XxYyZAAZ"
      }
    ]
    ```

---

### Notes

- Search is case-insensitive and supports partial matches.
- If multiple contacts match, all are returned. The AI client is responsible for disambiguation.
- Use the returned `id` as the `contactId` parameter when calling [`createCallLog`](#createcalllog).

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected. Call [`getSessionInfo`](#getsessioninfo) first to verify.

!!! tip "Related tools"
    - [`findContactByPhone`](#findcontactbyphone) — search by phone number instead
    - [`createContact`](#createcontact) — create a contact if none is found
    - [`createCallLog`](#createcalllog) — log a call against the found contact

---

## findContactByPhone

Searches the connected CRM for a contact matching the given phone number. Ideal for automatic caller lookup when an inbound call arrives.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `phoneNumber` | `string` | ✅ | Phone number to search for. Accepts E.164 format (`+14155550123`) or local formats — the server normalises before searching. |

---

### Returns

An array of matching contact objects (same schema as [`findContactByName`](#findcontactbyname)):

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID |
| `name` | `string` | Full name |
| `phone` | `string \| null` | Primary phone number |
| `email` | `string \| null` | Primary email address |
| `company` | `string \| null` | Associated company or account name |
| `crmUrl` | `string \| null` | Deep link to the CRM record |

Returns an empty array `[]` if no match is found.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "findContactByPhone",
        "arguments": {
          "phoneNumber": "+14155550123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Who is calling from +1 415 555 0123?
    ```

=== "Sample response"

    ```json
    [
      {
        "id": "0031g00000XxYyZAAZ",
        "name": "Jane Smith",
        "phone": "+14155550123",
        "email": "jane.smith@acme.com",
        "company": "Acme Corp",
        "crmUrl": "https://acme.salesforce.com/0031g00000XxYyZAAZ"
      }
    ]
    ```

---

### Notes

- Phone number normalisation handles common formats: `(415) 555-0123`, `415-555-0123`, `+1 415 555 0123`.
- When no contact is found, consider calling [`createContact`](#createcontact) to add them.

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.

!!! tip "Common workflow"
    Inbound call → `findContactByPhone` → display contact info → after call ends → [`createCallLog`](#createcalllog)

---

## createContact

Creates a new contact record in the connected CRM platform. Returns the newly created contact's CRM ID and details.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `phoneNumber` | `string` | ✅ | Phone number in E.164 format, e.g. `+14155551234` |
| `newContactName` | `string` | — | Full name of the new contact. If omitted, the contact is created with only a phone number. |

---

### Returns

The created contact object:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID of the new contact |
| `name` | `string \| null` | Name as stored in the CRM |
| `phone` | `string` | Phone number as stored |
| `crmUrl` | `string` | Deep link to the new record in the CRM UI |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createContact",
        "arguments": {
          "phoneNumber": "+14155551234",
          "newContactName": "Alex Johnson"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a new contact for Alex Johnson with phone number +1 415 555 1234.
    ```

=== "Sample response"

    ```json
    {
      "id": "0031g00000NewIdAAA",
      "name": "Alex Johnson",
      "phone": "+14155551234",
      "crmUrl": "https://acme.salesforce.com/0031g00000NewIdAAA"
    }
    ```

---

### Notes

- The `phoneNumber` field must be in [E.164 format](https://en.wikipedia.org/wiki/E.164). Use `+` followed by country code and number, no spaces or dashes.
- Duplicate detection is handled by the CRM platform. If a contact with that phone number already exists, the CRM may return an error or the existing record depending on your CRM's settings.
- After creating a contact, the returned `id` can be passed directly to [`createCallLog`](#createcalllog).

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.

!!! tip "Related tools"
    - [`findContactByPhone`](#findcontactbyphone) — check for existing contacts before creating
    - [`createCallLog`](#createcalllog) — immediately log a call against the new contact

---

## createCallLog

Creates a single call activity log in the connected CRM platform. Can accept a raw RingCentral call log record (from [`rcGetCallLogs`](#rcgetcalllogs)) or manually supplied fields.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `incomingData` | `object` | — | A complete RingCentral call log record. Pass items from `rcGetCallLogs` directly here — no field mapping needed. |
| `contactId` | `string` | — | CRM contact ID to associate the log with. |
| `contactType` | `string` | — | Type of the CRM contact object (e.g. `"Contact"`, `"Lead"`). Required by some CRMs when `contactId` is set. |
| `note` | `string` | — | Free-text note or call summary to attach to the log entry. |

!!! info "At least one parameter recommended"
    All parameters are technically optional, but a useful log entry typically needs at least `incomingData` or `contactId` + `note`.

---

### Returns

| Field | Type | Description |
|-------|------|-------------|
| `logId` | `string` | ID of the created CRM activity record |
| `crmUrl` | `string \| null` | Deep link to the log entry in the CRM UI |

---

### Example

=== "Passing rcGetCallLogs data directly"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createCallLog",
        "arguments": {
          "incomingData": {
            "logInfo": { /* single record from rcGetCallLogs.records[] */ }
          },
          "contactId": "0031g00000XxYyZAAZ",
          "contactType": "Contact",
          "note": "Customer called to discuss renewal. Interested in Enterprise plan."
        }
      }
    }
    ```

=== "Manual log with note only"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createCallLog",
        "arguments": {
          "contactId": "0031g00000XxYyZAAZ",
          "contactType": "Contact",
          "note": "Left voicemail. Will follow up next Tuesday."
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Log today's call with Jane Smith to Salesforce. Note: discussed Q3 renewal, she's interested in upgrading to Enterprise.
    ```

=== "Sample response"

    ```json
    {
      "logId": "00T1g00000AbCdEAAZ",
      "crmUrl": "https://acme.salesforce.com/00T1g00000AbCdEAAZ"
    }
    ```

---

### Recommended workflow

The most complete log entry combines data from `rcGetCallLogs` with a contact lookup and a human-written note:

```
1. rcGetCallLogs       → get raw call record
2. findContactByPhone  → resolve CRM contact ID
3. createCallLog       → post log with incomingData + contactId + note
```


---

!!! warning "One log per call"
    This tool creates **one** log entry per invocation. To log multiple calls, call it once per record from `rcGetCallLogs`.

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.

---

## rcGetCallLogs

Fetches call log records from the RingCentral platform for the authenticated user within a specified time range. Records can be passed directly to [`createCallLog`](#createcalllog) without field mapping.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `timeFrom` | `string` | ✅ | Start of the time range in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, e.g. `2025-05-01T00:00:00Z` |
| `timeTo` | `string` | ✅ | End of the time range in ISO 8601 format, e.g. `2025-05-06T23:59:59Z` |

---

### Returns

An object containing a `records` array. Each record is a complete RingCentral call log object:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique call log ID |
| `sessionId` | `string` | Session ID (groups legs of the same call) |
| `startTime` | `string` | ISO 8601 timestamp when the call started |
| `duration` | `number` | Call duration in seconds |
| `type` | `string` | `"Voice"`, `"Fax"`, etc. |
| `direction` | `string` | `"Inbound"` or `"Outbound"` |
| `result` | `string` | `"Accepted"`, `"Missed"`, `"Voicemail"`, etc. |
| `from` | `object` | Caller info: `{ phoneNumber, name, extensionNumber }` |
| `to` | `object` | Callee info: `{ phoneNumber, name, extensionNumber }` |
| `recording` | `object \| null` | Recording metadata if available |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "rcGetCallLogs",
        "arguments": {
          "timeFrom": "2025-05-01T00:00:00Z",
          "timeTo":   "2025-05-06T23:59:59Z"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me all my RingCentral calls from this week.
    ```

=== "Sample response"

    ```json
    {
      "records": [
        {
          "id": "RCLogABC123",
          "sessionId": "sess_001",
          "startTime": "2025-05-06T14:32:00Z",
          "duration": 312,
          "type": "Voice",
          "direction": "Inbound",
          "result": "Accepted",
          "from": { "phoneNumber": "+14155550123", "name": "Jane Smith" },
          "to":   { "phoneNumber": "+16505551000", "extensionNumber": "1042" },
          "recording": null
        }
      ]
    }
    ```

---

### Passing records to createCallLog

Each item in `records[]` can be passed **directly** as `incomingData.logInfo` to `createCallLog` — no field renaming required:

```json
// Use records[0] directly
{
  "name": "createCallLog",
  "arguments": {
    "incomingData": { "logInfo": <records[0]> },
    "contactId": "0031g00000XxYyZAAZ",
    "note": "Call summary here"
  }
}
```

---

### Notes

- Maximum date range is 7 days per request. For longer ranges, make multiple calls with sequential windows.
- Results are ordered by `startTime` descending (most recent first).
- Calls from all devices and extensions under the authenticated account are included.

---

!!! warning "CRM connection required"
    This tool requires an active RingCentral session. The user must be authenticated via RingCentral OAuth.

!!! tip "Related tools"
    - [`createCallLog`](#createcalllog) — write fetched records to your CRM
    - [`findContactByPhone`](#findcontactbyphone) — resolve caller identity from `from.phoneNumber`

---

## logout

Signs the current user out of the connected CRM platform. The RingCentral session remains active; only the CRM link is severed.

**Server:** [App Connect](../servers/app-connect.md)  
**CRM required:** No

---

### Parameters

This tool takes no parameters.

---

### Returns

A confirmation object:

| Field | Type | Description |
|-------|------|-------------|
| `success` | `boolean` | `true` if the CRM session was successfully terminated |
| `message` | `string` | Human-readable status message |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "logout",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Disconnect my CRM from RingCentral App Connect.
    ```

=== "Sample response"

    ```json
    {
      "success": true,
      "message": "Successfully disconnected from Salesforce."
    }
    ```

---

### Notes

- After calling `logout`, tools that require CRM authentication will return an error until the user reconnects.
- To reconnect, the user must re-authenticate via the App Connect portal or the AI client's integration settings.
- This does **not** log the user out of RingCentral itself.

---

!!! tip "Related tools"
    - [`getSessionInfo`](#getsessioninfo) — confirm logout was successful

---

