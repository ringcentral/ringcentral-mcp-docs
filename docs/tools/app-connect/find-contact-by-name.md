# findContactByName

Searches the connected CRM for contacts whose name matches the provided string. Returns contact details including phone numbers, email, and CRM record IDs.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `name` | `string` | ✅ | Full or partial name to search for (e.g. `"Jane"`, `"Jane Smith"`) |

---

## Returns

An array of matching contact objects:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID |
| `name` | `string` | Full name |
| `phone` | `string \| null` | Primary phone number |
| `email` | `string \| null` | Primary email address |
| `company` | `string \| null` | Associated company or account name |
| `crmUrl` | `string \| null` | Deep link to the record in the CRM UI |

Returns an empty array `[]` if no matches are found.

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "findContactByName",
        "arguments": {
          "name": "Jane Smith"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Look up the contact "Jane Smith" in my CRM.
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

- Search is case-insensitive and supports partial matches.
- If multiple contacts match, all are returned. The AI client is responsible for disambiguation.
- Use the returned `id` as the `contactId` parameter when calling [`createCallLog`](create-call-log.md).

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected. Call [`getSessionInfo`](get-session-info.md) first to verify.

!!! tip "Related tools"
    - [`findContactByPhone`](find-contact-by-phone.md) — search by phone number instead
    - [`createContact`](create-contact.md) — create a contact if none is found
    - [`createCallLog`](create-call-log.md) — log a call against the found contact
