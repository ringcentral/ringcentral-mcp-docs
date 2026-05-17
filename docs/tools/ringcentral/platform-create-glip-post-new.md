# platform_create_glip_post_new

Create a post in a RingCentral Team Messaging chat. Maps to the RingCentral REST API `POST /team-messaging/v1/chats/{chatId}/posts`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.chatId` | `string` | ✅ | ID of the chat to post into |
| `body.text` | `string` | — | Text content of the post |
| `body.attachments[].id` | `string` | — | ID of an attachment to include |
| `body.attachments[].type` | `File \| Note \| Event \| Card` | — | Type of the attachment |

---

## Returns

Returns the newly created post object, including its `id`, `creationTime`, `lastModifiedTime`, `text`, and any attachments.

---

## Example

=== "Claude prompt"

    ```
    Post "The weekly report is ready for review" to chat ID 62910238527.
    ```

---

## Notes

- Either `body.text` or at least one attachment must be supplied; a post cannot be empty.
- Use [`platform_list_glip_chats_new`](platform-list-glip-chats-new.md) or [`platform_list_glip_conversations_new`](platform-list-glip-conversations-new.md) to find a valid `chatId` before posting.
- Attachment types `File`, `Note`, `Event`, and `Card` refer to RingCentral Team Messaging attachment objects, not local files.

---

!!! tip "Related tools"
    To read existing posts in a chat, use [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md).
