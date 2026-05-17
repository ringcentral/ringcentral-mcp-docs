# platform_create_glip_conversation_new

Create or open a direct conversation (1:1 or group). Maps to the RingCentral REST API `POST /team-messaging/v1/conversations`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `body.members[].email` | `string` | — | Email address of a member to include in the conversation |
| `body.members[].id` | `string` | — | Extension ID of a member to include in the conversation |

---

## Returns

Returns the conversation object for the newly created or already-existing conversation, including its `id`, type, creation time, and member list.

---

## Example

=== "Claude prompt"

    ```
    Start a direct message conversation with alice@example.com.
    ```

---

## Notes

- If a conversation with the exact same set of members already exists, the API returns the existing conversation rather than creating a duplicate.
- Each member can be identified by either `email` or `id`; at least one of the two should be provided per member entry.
- The authenticated user is automatically added as a member.

---

!!! tip "Related tools"
    After creating a conversation, use [`platform_create_glip_post_new`](platform-create-glip-post-new.md) to send the first message into it.
