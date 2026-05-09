# createCallLog

Creates a single call activity log in the connected CRM platform. Can accept a raw RingCentral call log record (from [`rcGetCallLogs`](rc-get-call-logs.md)) or manually supplied fields.

**Server:** [App Connect](../../servers/app-connect.md)  
**CRM required:** ⚠️ Yes

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `incomingData` | `object` | — | A complete RingCentral call log record. Pass items from `rcGetCallLogs` directly here — no field mapping needed. |
| `contactId` | `string` | — | CRM contact ID to associate the log with. |
| `contactType` | `string` | — | Type of the CRM contact object (e.g. `"Contact"`, `"Lead"`). Required by some CRMs when `contactId` is set. |
| `note` | `string` | — | Free-text note or call summary to attach to the log entry. |

!!! info "At least one parameter recommended"
    All parameters are technically optional, but a useful log entry typically needs at least `incomingData` or `contactId` + `note`.

---

## Returns

| Field | Type | Description |
|-------|------|-------------|
| `logId` | `string` | ID of the created CRM activity record |
| `crmUrl` | `string \| null` | Deep link to the log entry in the CRM UI |

---

## Example

=== "Passing rcGetCallLogs data directly"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createCallLog",
        "arguments": {
          "incomingData": {
            "logInfo": { /* single record from rcGetCallLogs.records[] */ }
          },
          "contactId": "0031g00000XxYyZAAZ",
          "contactType": "Contact",
          "note": "Customer called to discuss renewal. Interested in Enterprise plan."
        }
      }
    }
    ```

=== "Manual log with note only"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "createCallLog",
        "arguments": {
          "contactId": "0031g00000XxYyZAAZ",
          "contactType": "Contact",
          "note": "Left voicemail. Will follow up next Tuesday."
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Log today's call with Jane Smith to Salesforce. Note: discussed Q3 renewal, she's interested in upgrading to Enterprise.
    ```

=== "Sample response"

    ```json
    {
      "logId": "00T1g00000AbCdEAAZ",
      "crmUrl": "https://acme.salesforce.com/00T1g00000AbCdEAAZ"
    }
    ```

---

## Recommended workflow

The most complete log entry combines data from `rcGetCallLogs` with a contact lookup and a human-written note:

```
1. rcGetCallLogs       → get raw call record
2. findContactByPhone  → resolve CRM contact ID
3. createCallLog       → post log with incomingData + contactId + note
```

See the [CRM Integration Workflow](../../guides/crm-workflow.md) guide for a full walkthrough.

---

!!! warning "One log per call"
    This tool creates **one** log entry per invocation. To log multiple calls, call it once per record from `rcGetCallLogs`.

!!! warning "CRM connection required"
    This tool will return an authentication error if no CRM is connected.
