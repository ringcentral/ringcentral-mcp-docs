# createContact

Creates a new contact record in the connected CRM platform. Returns the newly created contact's CRM ID and details.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `phoneNumber` | `string` | ✅ | Phone number in E.164 format, e.g. `+14155551234` |
| `newContactName` | `string` | — | Full name of the new contact. If omitted, the contact is created with only a phone number. |

---

## Returns

The created contact object:

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | CRM record ID of the new contact |
| `name` | `string \| null` | Name as stored in the CRM |
| `phone` | `string` | Phone number as stored |
| `crmUrl` | `string` | Deep link to the new record in the CRM UI |

---

## Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createContact",
        "arguments": {
          "phoneNumber": "+14155551234",
          "newContactName": "Alex Johnson"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a new contact for Alex Johnson with phone number +1 415 555 1234.
    ```

=== "Sample response"

    ```json
    {
      "id": "0031g00000NewIdAAA",
      "name": "Alex Johnson",
      "phone": "+14155551234",
      "crmUrl": "https://acme.salesforce.com/0031g00000NewIdAAA"
    }
    ```

---

## Notes

- The `phoneNumber` field must be in [E.164 format](https://en.wikipedia.org/wiki/E.164). Use `+` followed by country code and number, no spaces or dashes.
- Duplicate detection is handled by the CRM platform. If a contact with that phone number already exists, the CRM may return an error or the existing record depending on your CRM's settings.
- After creating a contact, the returned `id` can be passed directly to [`createCallLog`](create-call-log.md).

---

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.

!!! tip "Related tools"
    - [`findContactByPhone`](find-contact-by-phone.md) — check for existing contacts before creating
    - [`createCallLog`](create-call-log.md) — immediately log a call against the new contact
