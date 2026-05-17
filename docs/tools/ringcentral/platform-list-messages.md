# platform_list_messages

List messages in a user's message store (SMS, fax, voicemail, pager). Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `path.extensionId` | `string` | — | Extension ID; defaults to `~` (authenticated user's extension) |
| `query.messageType` | `Fax \| SMS \| VoiceMail \| Pager` | — | Filter by one or more message types |
| `query.direction` | `Inbound \| Outbound` | — | Filter by message direction |
| `query.readStatus` | `Read \| Unread` | — | Filter by read status |
| `query.dateFrom` | `string` | — | Start of date range in ISO 8601 format |
| `query.dateTo` | `string` | — | End of date range in ISO 8601 format |
| `query.conversationId` | `string` | — | Filter to a specific conversation thread |
| `query.phoneNumber` | `string` | — | Filter messages to or from a specific phone number |
| `query.distinctConversations` | `boolean` | — | Return only the most recent message per conversation |
| `query.page` | `number` | — | Page number for pagination |
| `query.perPage` | `number` | — | Number of records per page |
| `query.availability` | `Alive \| Deleted \| Purged` | — | Filter by message availability status |
| `query.owner` | `Any \| Personal \| Shared` or `string[]` | — | Filter by message ownership |
| `query.voicemailOwner` | `string[]` | — | Filter voicemails by owner extension ID(s) |
| `query.ownerExtensionType` | `string` | — | Filter by the extension type of the message owner |

---

## Returns

Returns a paginated list of message records from the user's message store. Each record includes message `id`, `type`, `direction`, `readStatus`, `subject`, sender and recipient details, and `creationTime`.

---

## Example

=== "Claude prompt"

    ```
    Show me all unread SMS messages from the past week.
    ```

---

## Notes

- `path.accountId` and `path.extensionId` both default to `~`, which resolves to the authenticated user's account and extension.
- Multiple enum values can be supplied for `messageType`, `direction`, `readStatus`, and `availability` to broaden the filter.
- To retrieve the content of a specific message, follow up with [`platform_read_message`](platform-read-message.md) or [`platform_read_message_content`](platform-read-message-content.md).

---

!!! tip "Related tools"
    Retrieve a specific message by ID with [`platform_read_message`](platform-read-message.md), or download an attachment with [`platform_read_message_content`](platform-read-message-content.md).
