# platform_call_post_operation

Executes a supported RingCentral Platform POST operation with a JSON request body.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool uses a dynamic dispatch model. The operation name and its request body schema are not fixed — they are determined by the operations returned from [`platform_list_post_operations`](platform-list-post-operations.md). Call that tool first to discover the valid operation identifiers and their expected input schemas, then pass the appropriate operation name and body to this tool.

---

## Returns

Returns the JSON response body from the underlying RingCentral Platform POST endpoint for the requested operation. The exact shape of the response depends on which operation is executed.

---

## Example

=== "Claude prompt"

    ```
    Search the company directory for everyone in the Engineering department.
    ```

---

## Notes

- Always call [`platform_list_post_operations`](platform-list-post-operations.md) first to discover valid operation names and their request body schemas.
- Path parameters such as `accountId` default to `~`, which resolves to the authenticated user's account.
- This tool handles write and search (POST) operations. For read-only operations use [`platform_call_get_operation`](platform-call-get-operation.md).

---

!!! tip "Related tools"
    Use [`platform_list_post_operations`](platform-list-post-operations.md) to browse available operations before calling this tool.
