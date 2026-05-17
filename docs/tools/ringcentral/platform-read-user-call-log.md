# platform_read_user_call_log

List call log records for a user's extension. Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `path.extensionId` | `string` | — | Extension ID; defaults to `~` (authenticated user's extension) |
| `query.direction` | `Inbound \| Outbound` | — | Filter by call direction |
| `query.type` | `Voice \| Fax` | — | Filter by call type |
| `query.dateFrom` | `string` | — | Start of date range in ISO 8601 format |
| `query.dateTo` | `string` | — | End of date range in ISO 8601 format |
| `query.view` | `Simple \| Detailed` | — | Level of detail in the response (`Detailed` includes per-leg data) |
| `query.withRecording` | `boolean` | — | Return only calls that have a recording |
| `query.recordingType` | `Automatic \| OnDemand \| All` | — | Filter by recording type |
| `query.phoneNumber` | `string` | — | Filter calls to or from a specific phone number |
| `query.extensionNumber` | `string` | — | Filter calls to or from a specific extension number |
| `query.sessionId` | `string` | — | Filter to a specific call session |
| `query.telephonySessionId` | `string` | — | Filter to a specific telephony session |
| `query.transport` | `PSTN \| VoIP` | — | Filter by call transport type |
| `query.showBlocked` | `boolean` | — | Include calls from blocked numbers |
| `query.showDeleted` | `boolean` | — | Include deleted call log records |
| `query.metadataCategory` | `string[]` | — | Filter by metadata category |
| `query.page` | `number` | — | Page number for pagination |
| `query.perPage` | `number` | — | Number of records per page |

---

## Returns

Returns a paginated list of call log records for the specified extension. Each record includes call `id`, `direction`, `type`, `startTime`, `duration`, caller/callee details, telephony session IDs, and recording references if applicable.

---

## Example

=== "Claude prompt"

    ```
    Show me all inbound calls I received in the last 7 days that were recorded.
    ```

---

## Notes

- `path.accountId` and `path.extensionId` both default to `~`, so calling this tool with no path parameters returns the authenticated user's own call log.
- Use `query.view: Detailed` to retrieve per-leg data for multi-party or transferred calls.
- The `telephonySessionId` in each record can be used with [`platform_read_ai_notes`](platform-read-ai-notes.md) to retrieve AI-generated call notes.

---

!!! tip "Related tools"
    Use `telephonySessionId` values from call log records to fetch AI notes with [`platform_read_ai_notes`](platform-read-ai-notes.md).
