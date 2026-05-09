# rcGetCallLogs

Fetches call log records from the RingCentral platform for the authenticated user within a specified time range. Records can be passed directly to [`createCallLog`](create-call-log.md) without field mapping.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `timeFrom` | `string` | ✅ | Start of the time range in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, e.g. `2025-05-01T00:00:00Z` |
| `timeTo` | `string` | ✅ | End of the time range in ISO 8601 format, e.g. `2025-05-06T23:59:59Z` |

---

## Returns

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

## Example

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

## Passing records to createCallLog

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

## Notes

- Maximum date range is 7 days per request. For longer ranges, make multiple calls with sequential windows.
- Results are ordered by `startTime` descending (most recent first).
- Calls from all devices and extensions under the authenticated account are included.

---

!!! warning "CRM connection required"
    This tool requires an active RingCentral session. The user must be authenticated via RingCentral OAuth.

!!! tip "Related tools"
    - [`createCallLog`](create-call-log.md) — write fetched records to your CRM
    - [`findContactByPhone`](find-contact-by-phone.md) — resolve caller identity from `from.phoneNumber`
