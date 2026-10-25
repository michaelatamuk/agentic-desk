# Middleware

What sits between the platform and the apps. Two projects, two different jobs.

| Folder | Job | Boundary |
|---|---|---|
| `laix/` | Decides whether, when and how an app acts | A layer: a contract above and below it, swappable on its own |
| `cortex/` | Extends the platform: skills, safety, routing, memory, tracing | Plugins into the platform, attached from the inside |

Both are in the middle; only LAIX is middleware in the strict sense, because it sits between two
parties that do not know each other. Cortex extends one of those parties rather than sitting between
them. The practical difference: LAIX can be sold or swapped without touching the platform or the
app; Cortex changes the platform it is installed into.

The boundary between the two is not settled. Cortex's routing, context selection and runtime overlap
LAIX's resource policy, live context and execution bridge — see `cortex/scope.md` for the four
decisions that have to be made before either team writes code assuming an answer.
