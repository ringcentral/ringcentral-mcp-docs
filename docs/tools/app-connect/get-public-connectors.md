# getPublicConnectors

Returns the list of CRM connectors publicly available through App Connect. Use this to show users which CRM platforms they can link to their RingCentral account.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

An array of connector objects:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique connector identifier |
| `name` | `string` | Human-readable CRM platform name |
| `logoUrl` | `string` | URL to the connector's logo image |
| `authType` | `string` | Authentication method (`"oauth2"`, `"apikey"`, etc.) |
| `status` | `string` | Availability status (`"available"`, `"beta"`, `"deprecated"`) |

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "getPublicConnectors",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me which CRM platforms I can connect to with RingCentral App Connect.
    ```

=== "Sample response"

    ```json
    [
      { "id": "salesforce", "name": "Salesforce", "authType": "oauth2", "status": "available" },
      { "id": "hubspot",    "name": "HubSpot",    "authType": "oauth2", "status": "available" },
      { "id": "zoho",       "name": "Zoho CRM",   "authType": "oauth2", "status": "available" },
      { "id": "dynamics",   "name": "MS Dynamics","authType": "oauth2", "status": "beta"      }
    ]
    ```

---

!!! tip "Related tools"
    - [`getSessionInfo`](get-session-info.md) — check if a connector is already linked
