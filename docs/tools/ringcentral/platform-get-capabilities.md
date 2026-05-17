# platform_get_capabilities

Returns a help-style summary of the RingCentral API endpoints and MCP tools implemented by this service.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

Returns a human-readable summary describing all RingCentral API endpoints and MCP tools available through this server, including brief descriptions of what each tool does and how to use it.

---

## Example

=== "Claude prompt"

    ```
    What can you do with the RingCentral MCP server?
    ```

---

## Notes

- This is the best starting point for discovering what is available on the server without calling individual list tools.
- The response is intended to be read by an AI agent or surfaced directly to an end user as onboarding help.
- For a machine-readable list of GET operations, use [`platform_list_get_operations`](platform-list-get-operations.md); for POST operations use [`platform_list_post_operations`](platform-list-post-operations.md).

---

!!! tip "Related tools"
    Use [`gatekeeper_select_tool`](gatekeeper-select-tool.md) after reviewing capabilities to route a specific user request to the right tool.
