# platform_read_extension

Get details about a RingCentral extension. Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}`.

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

Returns the extension object including the user's name, extension number, email, status, regional settings, and associated phone numbers.

---

## Example

=== "Claude prompt"

    ```
    What is my RingCentral extension number and email address?
    ```

---

## Notes

- Both `path.accountId` and `path.extensionId` default to `~`, so calling this tool with no parameters returns the authenticated user's own extension details.
- To look up a different extension, supply the target extension's ID as `path.extensionId`.
- For a higher-level view of the authenticated user (including token scope), consider [`profile_get_current_extension`](profile-get-current-extension.md).

---

!!! tip "Related tools"
    Use [`platform_read_unified_presence`](platform-read-unified-presence.md) to check the presence status of the same extension.
