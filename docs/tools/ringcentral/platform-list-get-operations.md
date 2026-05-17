# platform_list_get_operations

Lists the supported read-only RingCentral Platform GET operations available through `platform_call_get_operation`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

Returns a list of all supported GET operation identifiers along with their input schemas, describing the path parameters, query parameters, and expected data types for each operation.

---

## Example

=== "Claude prompt"

    ```
    What read operations are available on the RingCentral platform?
    ```

---

## Notes

- Call this tool before using [`platform_call_get_operation`](platform-call-get-operation.md) to ensure you are passing a valid operation name and correct parameters.
- The returned schemas drive the dynamic dispatch in `platform_call_get_operation`.
- For POST operations, use [`platform_list_post_operations`](platform-list-post-operations.md) instead.

---

!!! tip "Related tools"
    Pass one of the returned operation names to [`platform_call_get_operation`](platform-call-get-operation.md) to execute it.
