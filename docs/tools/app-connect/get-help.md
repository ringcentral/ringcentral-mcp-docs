# getHelp

Returns a quick-start guide describing what the App Connect integration can do and how to get started. Useful as an onboarding prompt when a user first connects the server to their AI client.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

A plain-text or markdown guide covering:

- What App Connect does
- How to authenticate with a CRM
- A summary of available tools and common workflows

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getHelp",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What can I do with the RingCentral App Connect integration?
    ```

---

## Notes

- This tool is safe to call before authentication is complete.
- Intended for use at session start or when a user asks "what can you do?"

---

!!! tip "Related tools"
    - [`getSessionInfo`](get-session-info.md) — check current auth status
    - [`getPublicConnectors`](get-public-connectors.md) — list connectable CRMs
