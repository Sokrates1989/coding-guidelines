# Persistence Ownership and Synchronization

**Rule ID:** `QUALITY-PERSISTENCE-SYNC`  
**Status:** Active.  
**Applies when:** Persisted data, local stores, backend data APIs, offline/hybrid synchronization, drafts, attachments, settings, or recovery are planned, created, changed, reviewed, or diagnosed.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-09-24`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Decide data ownership before implementation

For every affected dataset and material field, identify the owner and intended persistence scope from current product requirements and implementation evidence. Distinguish:

- **Account-synced:** durable user data expected across devices.
- **Device-local:** durable data or preferences intentionally specific to one installation.
- **Server-only:** authoritative service data with no required local counterpart.
- **Ephemeral or derived:** state that is not independently persisted.

Record the expected behavior in each supported runtime mode (for example local-only, online, and hybrid), including offline availability, cross-device visibility, deletion, attachments, and conflict handling where relevant. Do not infer account scope solely from the existence of a backend endpoint, or device scope solely from an existing local table. Do not create a fake local endpoint for server-only data or send device-only data to the account service merely for symmetry.

If the intended ownership or mode behavior could materially change the design and is not established, MUST ask the operator before implementing that storage contract. Ask a targeted question such as whether the data follows the account across devices, remains on this device, or exists only on the server. Clarify offline availability, conflict decisions, and attachment handling when they affect the result. Continue safe read-only investigation and independent in-scope work while awaiting the answer; do not silently choose synchronization semantics.

## Interface-only persistence boundary

Persisted data SHOULD be accessed through a typed, interface-defined capability owned by the feature or a reusable package. When the repository declares an interface-only persistence standard or supports multiple providers/runtime modes, production reads, writes, and deletes MUST cross that boundary. UI, domain, and orchestration code depend on the interface; only concrete adapters implementing it may call raw storage or persistent remote APIs. This includes SharedPreferences, browser localStorage, secure storage, Hive/Drift, files, backend HTTP persistence calls, and server database clients. A local-only or server-only dataset still has one appropriate interface boundary; it does not need an artificial second store. Preserve owner scoping, revisions, transactions, tombstones, and attachment semantics in the contract where relevant.

Reuse and extend suitable package contracts, including AI-chat storage, rather than creating competing app-specific abstractions. Package consumers supply platform adapters through injection. Under a declared interface-only standard, existing direct access is migration debt, not evidence of an exception: new code MUST NOT add another bypass, and touched legacy paths must be migrated or assigned a bounded migration dependency. Database migrations and isolated test fixtures may use raw storage under their own safety rules. Do not claim repository-wide compliance until a complete production-source inventory and an automated adapter-boundary check find no unapproved bypasses.

## Verify the complete path, not just an interface

Before declaring persistence support, trace the concrete write and read path from UI or API caller through repository, local and remote adapters, dependency injection, runtime-mode selection, startup/replay workers, and storage. Abstract interfaces, backend routes, schemas, and unit tests of isolated adapters are not proof that the active application uses both sides.

For account-synced data in a supported hybrid mode, the coherent implementation MUST cover:

1. Durable local writes and an offline mutation queue or equivalent, including updates and deletion markers.
2. Owner-scoped, authorized remote writes with retry and idempotency, plus complete remote reads (including pagination or cursors).
3. Startup and reconnect reconciliation (plus manual sync where offered) wired into the active runtime; repeatable replay after app restart.
4. A documented ordering or revision policy for concurrent changes, including the required user decision when automatic conflict resolution is not authorized.
5. Local application of remote changes and a way to detect and repair divergence without silently discarding unsynced user data.
6. Attachment upload/download and reference lifecycle when the dataset includes binary content.

Use the repository's established architecture and avoid redundant mechanisms. A feature that requires only online or only local persistence MUST follow that explicit contract; it is not incomplete merely because it lacks a second adapter. If an account-synced feature cannot be finished end to end in the current scope, identify the missing path explicitly and do not report the backend endpoint as a completed hybrid feature.

## Completion evidence

Keep the dataset ownership and mode decision near the authoritative feature documentation or implementation plan. For each changed account-synced dataset, verify the supported modes and at least the relevant failure boundaries: offline write and reconnect, process restart, second-device hydration, concurrent edits, deletion, owner isolation, and attachment failure. Include larger-than-one-page histories and equal timestamps when the pull protocol can encounter them. Tests MAY use isolated adapters and disposable services; never infer live-device or production success from unrun checks. Report what was implemented, what was validated, and any remaining endpoint or mode gap precisely.
