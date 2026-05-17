# platform_read_glip_posts_new

List posts in a Team Messaging chat. Maps to the RingCentral REST API `GET /team-messaging/v1/chats/{chatId}/posts`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.chatId` | `string` | ✅ | ID of the chat whose posts to retrieve |
| `query.recordCount` | `number` | — | Maximum number of posts to return |
| `query.pageToken` | `string` | — | Pagination token from a previous response to retrieve the next page |

---

## Returns

Returns a paginated list of post objects for the specified chat, ordered from most recent to oldest. Each post includes its `id`, `text`, `creationTime`, `lastModifiedTime`, creator information, and any attachments.

---

## Example

=== "Claude prompt"

    ```
    Show me the last 20 messages in chat 62910238527.
    ```

---

## Notes

- Use [`platform_list_glip_chats_new`](platform-list-glip-chats-new.md) or [`platform_list_glip_conversations_new`](platform-list-glip-conversations-new.md) to find a valid `chatId`.
- Posts are returned in reverse-chronological order by default; use `pageToken` to paginate backwards through history.
- To send a new post to the chat, use [`platform_create_glip_post_new`](platform-create-glip-post-new.md).

---

!!! tip "Related tools"
    Post a reply into this chat with [`platform_create_glip_post_new`](platform-create-glip-post-new.md).
