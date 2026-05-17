# platform_read_unified_presence

Get the unified presence status for a RingCentral extension. Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/unified-presence`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `path.extensionId` | `string` | — | Extension ID; defaults to `~` (authenticated user's extension) |

---

## Returns

Returns the unified presence object for the specified extension, including the aggregated presence status (e.g. `Available`, `Busy`, `DoNotDisturb`), telephony session presence, meeting presence, and glip (Team Messaging) presence.

---

## Example

=== "Claude prompt"

    ```
    What is my current presence status on RingCentral?
    ```

---

## Notes

- Both `path.accountId` and `path.extensionId` default to `~`, so calling this tool with no parameters returns the authenticated user's own presence.
- The unified presence aggregates status across telephony, meetings, and Team Messaging into a single top-level status.
- To look up the extension profile rather than its presence, use [`platform_read_extension`](platform-read-extension.md).

---

!!! tip "Related tools"
    Use [`platform_read_extension`](platform-read-extension.md) to retrieve the full extension profile alongside presence information.
