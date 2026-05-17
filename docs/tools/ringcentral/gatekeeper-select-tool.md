# gatekeeper_select_tool

First stop for translating a natural-language RingCentral request into MCP tool calls. Selects one RingCentral MCP tool using endpoint input schemas.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `userRequest` | `string` | ✅ | The natural-language request describing what the user wants to accomplish |
| `conversationContext` | `string` | — | Additional context from the ongoing conversation to improve tool selection |
| `intentHints` | `string[]` | — | Optional array of hint strings to help disambiguate the user's intent |

---

## Returns

Returns the name of the single most appropriate RingCentral MCP tool to call for the given request, along with any relevant metadata to guide the follow-up tool invocation.

---

## Example

=== "Claude prompt"

    ```
    I want to see my recent missed calls.
    ```

---

## Notes

- Use this tool as the entry point when a user's request is ambiguous and you are unsure which RingCentral MCP tool to invoke.
- The tool examines all available endpoint input schemas to make its selection, so passing rich `conversationContext` improves accuracy.
- After receiving the selected tool name, call that tool directly with the appropriate parameters.

---

!!! tip "Related tools"
    Follow up `gatekeeper_select_tool` with [`platform_get_capabilities`](platform-get-capabilities.md) if you need a broader overview of what operations are available before deciding.
