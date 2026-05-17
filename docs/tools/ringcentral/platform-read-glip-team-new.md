# platform_read_glip_team_new

Get details about a specific Team Messaging team. Maps to the RingCentral REST API `GET /team-messaging/v1/teams/{chatId}`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.chatId` | `string` | ✅ | ID of the team to retrieve |

---

## Returns

Returns the team object including its `id`, `name`, `description`, `creationTime`, `lastModifiedTime`, privacy setting (public or private), and member count.

---

## Example

=== "Claude prompt"

    ```
    Give me the details for team ID 62910238527.
    ```

---

## Notes

- Use [`platform_list_glip_teams_new`](platform-list-glip-teams-new.md) to discover team IDs before calling this tool.
- This tool returns team metadata only, not its posts. To read messages, use [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md).
- The authenticated user must be a member of the team to retrieve it.

---

!!! tip "Related tools"
    Read team messages with [`platform_read_glip_posts_new`](platform-read-glip-posts-new.md), or post into the team with [`platform_create_glip_post_new`](platform-create-glip-post-new.md).
