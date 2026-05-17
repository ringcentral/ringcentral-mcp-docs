# profile_get_current_extension

Returns the RingCentral extension for the authenticated bearer token. This tool always returns the caller's own extension and cannot query arbitrary account or extension IDs.

**Server:** [RingCentral MCP](../../servers/rc-labs-mcp.md)  
**CRM required:** No

---

## Parameters

This tool takes no parameters.

---

## Returns

Returns the extension object associated with the current bearer token, including the user's name, extension number, email address, account ID, and status. This is effectively the "who am I" endpoint for the authenticated session.

---

## Example

=== "Claude prompt"

    ```
    Who am I logged in as on RingCentral?
    ```

---

## Notes

- This tool is scoped strictly to the authenticated user; it cannot be used to look up other extensions.
- Use this as a reliable way to retrieve the current user's `extensionId` and `accountId` before passing `~` is insufficient.
- For richer extension details (regional settings, phone numbers, etc.), follow up with [`platform_read_extension`](platform-read-extension.md).

---

!!! tip "Related tools"
    Use [`platform_read_extension`](platform-read-extension.md) for a more detailed extension profile, or [`platform_read_unified_presence`](platform-read-unified-presence.md) to check your current presence status.
