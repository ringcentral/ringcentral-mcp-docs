# platform_list_glip_conversations_new

List direct and group conversations for the authenticated user. Maps to the RingCentral REST API `GET /team-messaging/v1/conversations`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `query.recordCount` | `number` | — | Maximum number of conversations to return |
| `query.pageToken` | `string` | — | Pagination token from a previous response to retrieve the next page |

---

## Returns

Returns a paginated list of conversation objects (1:1 and group DMs) that the authenticated user participates in. Each entry includes the conversation `id`, `type`, member list, and `creationTime`.

---

## Example

=== "Claude prompt"

    ```
    List my recent direct message conversations.
    ```

---

## Notes

- This endpoint returns only `Direct` and `Group` chat types. To include Teams and other types use [`platform_list_glip_chats_new`](platform-list-glip-chats-new.md).
- Use the `pageToken` from the response to retrieve subsequent pages.
- To open or create a new conversation, use [`platform_create_glip_conversation_new`](platform-create-glip-conversation-new.md).

---

!!! tip "Related tools"
    Retrieve a specific conversation by ID with [`platform_read_glip_conversation_new`](platform-read-glip-conversation-new.md).
