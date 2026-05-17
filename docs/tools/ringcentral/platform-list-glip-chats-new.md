# platform_list_glip_chats_new

List chats the authenticated user belongs to. Maps to the RingCentral REST API `GET /team-messaging/v1/chats`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `query.type` | `Personal \| Direct \| Group \| Team \| Everyone` | — | Filter by one or more chat types |
| `query.recordCount` | `number` | — | Maximum number of chats to return |
| `query.pageToken` | `string` | — | Pagination token from a previous response to retrieve the next page |

---

## Returns

Returns a paginated list of chat objects the authenticated user is a member of. Each entry includes the chat `id`, `type`, `name` (for teams and groups), `creationTime`, and member count.

---

## Example

=== "Claude prompt"

    ```
    Show me all the team chats I'm a member of.
    ```

---

## Notes

- Multiple values can be supplied for `query.type` to filter across several chat types at once.
- Use the `pageToken` from the response to paginate through large result sets.
- To list only conversations (1:1 and group DMs), use [`platform_list_glip_conversations_new`](platform-list-glip-conversations-new.md); for teams only, use [`platform_list_glip_teams_new`](platform-list-glip-teams-new.md).

---

!!! tip "Related tools"
    Once you have a `chatId`, use [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md) to read its messages or [`platform_create_glip_post_new`](platform-create-glip-post-new.md) to post into it.
