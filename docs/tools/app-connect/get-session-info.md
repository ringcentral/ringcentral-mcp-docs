# getSessionInfo

Returns the current user's RingCentral identity and their CRM connection status. Use this tool to verify a session is active before calling tools that require CRM authentication.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

A session object containing:

| Field | Type | Description |
|-------|------|-------------|
| `rcUserId` | `string` | RingCentral user ID |
| `rcUserName` | `string` | Display name of the authenticated RC user |
| `rcExtension` | `string` | RC extension number |
| `crmConnected` | `boolean` | Whether a CRM platform is linked |
| `crmPlatform` | `string \| null` | Name of the connected CRM (e.g. `"Salesforce"`) |
| `crmUserId` | `string \| null` | User ID in the CRM system |

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getSessionInfo",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Check my RingCentral session status and tell me which CRM I'm connected to.
    ```

=== "Sample response"

    ```json
    {
      "rcUserId": "12345678",
      "rcUserName": "Jane Smith",
      "rcExtension": "1042",
      "crmConnected": true,
      "crmPlatform": "Salesforce",
      "crmUserId": "0051g00000AbCdEAAZ"
    }
    ```

---

## Notes

- If `crmConnected` is `false`, calls to CRM-dependent tools will return an authentication error.
- Use this as a health-check at the start of automated workflows.

---

!!! tip "Related tools"
    - [`getPublicConnectors`](get-public-connectors.md) — see which CRM platforms are available to connect
    - [`logout`](logout.md) — end the CRM session
