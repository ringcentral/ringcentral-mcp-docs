# findContactByPhone

Searches the connected CRM for a contact matching the given phone number. Ideal for automatic caller lookup when an inbound call arrives.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `phoneNumber` | `string` | ✅ | Phone number to search for. Accepts E.164 format (`+14155550123`) or local formats — the server normalises before searching. |

---

## Returns

An array of matching contact objects (same schema as [`findContactByName`](find-contact-by-name.md)):

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID |
| `name` | `string` | Full name |
| `phone` | `string \| null` | Primary phone number |
| `email` | `string \| null` | Primary email address |
| `company` | `string \| null` | Associated company or account name |
| `crmUrl` | `string \| null` | Deep link to the CRM record |

Returns an empty array `[]` if no match is found.

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "findContactByPhone",
        "arguments": {
          "phoneNumber": "+14155550123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Who is calling from +1 415 555 0123?
    ```

=== "Sample response"

    ```json
    [
      {
        "id": "0031g00000XxYyZAAZ",
        "name": "Jane Smith",
        "phone": "+14155550123",
        "email": "jane.smith@acme.com",
        "company": "Acme Corp",
        "crmUrl": "https://acme.salesforce.com/0031g00000XxYyZAAZ"
      }
    ]
    ```

---

## Notes

- Phone number normalisation handles common formats: `(415) 555-0123`, `415-555-0123`, `+1 415 555 0123`.
- When no contact is found, consider calling [`createContact`](create-contact.md) to add them.

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.

!!! tip "Common workflow"
    Inbound call → `findContactByPhone` → display contact info → after call ends → [`createCallLog`](create-call-log.md)
