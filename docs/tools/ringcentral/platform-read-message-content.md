# platform_read_message_content

Get the binary content of a message attachment. Maps to the RingCentral REST API `GET /restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}/content/{attachmentId}`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `path.extensionId` | `string` | — | Extension ID; defaults to `~` (authenticated user's extension) |
| `path.messageId` | `string` | ✅ | ID of the message containing the attachment |
| `path.attachmentId` | `string` | ✅ | ID of the specific attachment to download |
| `query.contentDisposition` | `Inline \| Attachment` | — | Controls whether the content is rendered inline or downloaded as a file |
| `query.contentDispositionFilename` | `string` | — | Filename hint to use when the content is served as a download |

---

## Returns

Returns the raw binary content of the specified attachment (e.g. a fax image, voicemail audio file, or MMS media file) along with the appropriate `Content-Type` header.

---

## Example

=== "Claude prompt"

    ```
    Download the fax attachment with ID 111222333 from message 9876543210.
    ```

---

## Notes

- `path.accountId` and `path.extensionId` both default to `~`, which resolves to the authenticated user's account and extension.
- Attachment IDs can be found in the `attachments` array of a message object returned by [`platform_read_message`](platform-read-message.md).
- Use `query.contentDisposition: Attachment` combined with `query.contentDispositionFilename` to prompt a file download in browser-based contexts.

---

!!! tip "Related tools"
    First retrieve the message and its attachment IDs with [`platform_read_message`](platform-read-message.md).
