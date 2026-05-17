# platform_list_post_operations

Lists the supported RingCentral Platform POST operations available through `platform_call_post_operation`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

Returns a list of all supported POST operation identifiers along with their request body schemas, describing the required and optional fields for each operation.

---

## Example

=== "Claude prompt"

    ```
    What write operations are supported on the RingCentral platform?
    ```

---

## Notes

- Call this tool before using [`platform_call_post_operation`](platform-call-post-operation.md) to ensure you are passing a valid operation name and correct request body.
- The returned schemas drive the dynamic dispatch in `platform_call_post_operation`.
- For read-only GET operations, use [`platform_list_get_operations`](platform-list-get-operations.md) instead.

---

!!! tip "Related tools"
    Pass one of the returned operation names to [`platform_call_post_operation`](platform-call-post-operation.md) to execute it.
