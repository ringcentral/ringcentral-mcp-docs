# platform_call_get_operation

Executes a supported read-only RingCentral Platform GET operation. Missing `accountId`, `extensionId`, and `ownerExtensionId` path parameters default to `~`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool uses a dynamic dispatch model. The operation name and its parameters are not fixed — they are determined by the operations returned from [`platform_list_get_operations`](platform-list-get-operations.md). Call that tool first to discover the valid operation identifiers and their expected input schemas, then pass the appropriate operation name and arguments to this tool.

---

## Returns

Returns the JSON response body from the underlying RingCentral Platform GET endpoint for the requested operation. The exact shape of the response depends on which operation is executed.

---

## Example

=== "Claude prompt"

    ```
    Show me the details for my RingCentral extension.
    ```

---

## Notes

- Always call [`platform_list_get_operations`](platform-list-get-operations.md) first to discover valid operation names and their schemas.
- Path parameters `accountId`, `extensionId`, and `ownerExtensionId` default to `~`, which resolves to the authenticated user's account and extension.
- This tool covers read-only (GET) operations only. For write operations use [`platform_call_post_operation`](platform-call-post-operation.md).

---

!!! tip "Related tools"
    Use [`platform_list_get_operations`](platform-list-get-operations.md) to browse available operations before calling this tool.
