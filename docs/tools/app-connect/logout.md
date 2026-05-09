# logout

Signs the current user out of the connected CRM platform. The RingCentral session remains active; only the CRM link is severed.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

A confirmation object:

| Field | Type | Description |
|-------|------|-------------|
| `success` | `boolean` | `true` if the CRM session was successfully terminated |
| `message` | `string` | Human-readable status message |

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "logout",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Disconnect my CRM from RingCentral App Connect.
    ```

=== "Sample response"

    ```json
    {
      "success": true,
      "message": "Successfully disconnected from Salesforce."
    }
    ```

---

## Notes

- After calling `logout`, tools that require CRM authentication will return an error until the user reconnects.
- To reconnect, the user must re-authenticate via the App Connect portal or the AI client's integration settings.
- This does **not** log the user out of RingCentral itself.

---

!!! tip "Related tools"
    - [`getSessionInfo`](get-session-info.md) — confirm logout was successful
