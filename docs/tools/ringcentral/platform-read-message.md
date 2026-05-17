# platform_read_message

Get one or more messages from a user's message store. Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `path.extensionId` | `string` | — | Extension ID; defaults to `~` (authenticated user's extension) |
| `path.messageId` | `string[]` | ✅ | One or more message IDs to retrieve |

---

## Returns

Returns the message object(s) for the specified ID(s), including message `type`, `direction`, `readStatus`, subject, sender and recipient details, `creationTime`, and a list of attachment references.

---

## Example

=== "Claude prompt"

    ```
    Get the details for message IDs 1234567890 and 9876543210.
    ```

---

## Notes

- `path.accountId` and `path.extensionId` both default to `~`, which resolves to the authenticated user's account and extension.
- Multiple message IDs can be passed in a single call by providing an array of strings to `path.messageId`.
- To download the binary content of an attachment referenced in a message, use [`platform_read_message_content`](platform-read-message-content.md).

---

!!! tip "Related tools"
    Find message IDs first with [`platform_list_messages`](platform-list-messages.md), then download attachments with [`platform_read_message_content`](platform-read-message-content.md).
