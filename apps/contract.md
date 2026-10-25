# App contract

**Draft, version 0.** This is the only platform interface an app in `apps/` may rely on. When an app
needs something that is not listed here, the contract is extended first and the app second.
Otherwise the app is no longer portable, and the move to another platform becomes a rewrite.

## What an app may assume

| Capability | The app may assume | Why the app needs it |
|---|---|---|
| Agent turn | It can send a message and receive a stream of events until the turn ends | This is the product |
| Session identity | A session survives a disconnect and can be resumed by id | A live app cannot lose state when the user closes a tab |
| State read and write | It can store and read its own state under the session | The app knows more about the user than the agent does |
| Tools and skills | It can call a named tool with typed arguments and gets a typed result or a typed error | Actions are the point |
| Approvals | A destructive action can be routed to a human and returns allow, deny or edit | Every serious app needs a gate |
| Cancellation | A running action can be stopped, and the stop is reported | The user changes their mind |
| Credentials | The app can request a scoped credential for a third party without holding the secret | Auth is per user and per app, not per platform |
| Trace | Every turn and tool call has an id the app can log and show | Support and debugging |
| Model policy | The app can ask for a capability level, not a specific model | Otherwise the app is pinned to a vendor |
| Quota | The app can read remaining budget and is told when it is exhausted | Cost control |

## What an app must not assume

- Any file path, container, sandbox or process layout.
- Any module, package or class name from the platform.
- Any database schema, table or column.
- The prompt text, the number of model calls, or the order of internal steps.
- Vendor-specific event fields beyond the ones in this contract.
- That a tool runs in the same process, the same region or the same account as the app.

## Portability test

Run this before calling an app portable:

1. Search the app's folder for the platform name. Every hit must be inside a *Current implementation*
   note.
2. Replace that note with a different platform's name. Nothing else in the document should need to
   change.
3. If step 2 breaks a statement about behaviour, the statement described an internal. Move it to
   `openjiuwen/`.

## Open questions

This contract is not agreed yet. Three decisions come before version 1:

1. **Who owns the session?** If the platform owns it, the app is a view. If the app owns it, the
   platform must accept state it did not create.
2. **Where do permissions live?** In the platform, in the app, or in the user's identity provider.
3. **Who chooses the model?** A capability level is portable; a model name is not.
