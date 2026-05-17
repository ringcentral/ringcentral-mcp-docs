# platform_read_glip_conversation_new

Get details about a specific Team Messaging conversation. Maps to the RingCentral REST API `GET /team-messaging/v1/conversations/{chatId}`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.chatId` | `string` | ✅ | ID of the conversation to retrieve |

---

## Returns

Returns the conversation object including its `id`, `type`, member list with extension details, `creationTime`, and `lastModifiedTime`.

---

## Example

=== "Claude prompt"

    ```
    Get the details for conversation ID 62910238527.
    ```

---

## Notes

- Use [`platform_list_glip_conversations_new`](platform-list-glip-conversations-new.md) to discover conversation IDs before calling this tool.
- This tool retrieves metadata about the conversation, not its messages. To read messages, use [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md).
- The authenticated user must be a member of the conversation to retrieve it.

---

!!! tip "Related tools"
    Read the messages in this conversation with [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md), or post into it with [`platform_create_glip_post_new`](platform-create-glip-post-new.md).
