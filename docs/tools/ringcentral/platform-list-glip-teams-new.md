# platform_list_glip_teams_new

List Team Messaging teams the authenticated user belongs to. Maps to the RingCentral REST API `GET /team-messaging/v1/teams`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `query.recordCount` | `number` | — | Maximum number of teams to return |
| `query.pageToken` | `string` | — | Pagination token from a previous response to retrieve the next page |

---

## Returns

Returns a paginated list of team objects the authenticated user is a member of. Each entry includes the team `id`, `name`, `description`, `creationTime`, and whether the team is public or private.

---

## Example

=== "Claude prompt"

    ```
    What RingCentral teams am I a member of?
    ```

---

## Notes

- Only teams (`type: Team`) are returned; for direct and group conversations use [`platform_list_glip_conversations_new`](platform-list-glip-conversations-new.md).
- Use the `pageToken` from the response to paginate through large result sets.
- To get details for a specific team by ID, use [`platform_read_glip_team_new`](platform-read-glip-team-new.md).

---

!!! tip "Related tools"
    Once you have a team's `chatId`, post into it with [`platform_create_glip_post_new`](platform-create-glip-post-new.md) or read its posts with [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md).
