# platform_search_directory_entries

Search the company directory for extensions, users, and contacts. Maps to the RingCentral REST API `POST /restapi/v1.0/account/{accountId}/directory/entries/search`.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `path.accountId` | `string` | — | Account ID; defaults to `~` (authenticated user's account) |
| `body.searchString` | `string` | — | Free-text search string to match against directory entries |
| `body.searchFields` | `firstName \| lastName \| extensionNumber \| phoneNumber \| email \| jobTitle \| department \| customFieldValue` | — | Fields to search within; multiple values allowed |
| `body.extensionTypes` | `string` | — | Filter by extension type (e.g. `User`, `Department`, `Voicemail`) |
| `body.extensionStatuses` | `Enabled \| Disabled \| NotActivated` | — | Filter by extension status; multiple values allowed |
| `body.extensionIds` | `string[]` | — | Limit results to specific extension IDs |
| `body.accountIds` | `string[]` | — | Limit results to specific account IDs (for federated directories) |
| `body.siteIds` | `string[]` | — | Limit results to specific site IDs |
| `body.department` | `string` | — | Filter by department name |
| `body.showFederated` | `boolean` | — | Include entries from federated (partner) accounts |
| `body.showExternalContacts` | `boolean` | — | Include external contacts in the results |
| `body.showAdminOnlyContacts` | `boolean` | — | Include contacts visible only to administrators |
| `body.page` | `number` | — | Page number for pagination |
| `body.perPage` | `number` | — | Number of records per page |
| `body.orderBy[].fieldName` | `firstName \| lastName \| extensionNumber \| phoneNumber \| email \| jobTitle \| department` | — | Field to sort results by |
| `body.orderBy[].direction` | `Asc \| Desc` | — | Sort direction for the corresponding `fieldName` |

---

## Returns

Returns a paginated list of directory entry objects matching the search criteria. Each entry includes the user's name, extension number, email, department, job title, phone numbers, and extension type.

---

## Example

=== "Claude prompt"

    ```
    Find all enabled users in the Engineering department and sort them by last name.
    ```

---

## Notes

- `path.accountId` defaults to `~`, which resolves to the authenticated user's account.
- Multiple values can be supplied for `body.searchFields`, `body.extensionStatuses`, and `body.extensionTypes` to broaden or refine the search.
- The `body.orderBy` array supports multi-level sorting: add multiple objects with different `fieldName` values to sort by primary and secondary fields.

---

!!! tip "Related tools"
    Once you have an extension ID from the directory, retrieve its full profile with [`platform_read_extension`](platform-read-extension.md) or check its presence with [`platform_read_unified_presence`](platform-read-unified-presence.md).
