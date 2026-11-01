# Public Architecture Sketch

```text
User-owned card (versioned, namespace-scoped)
   |-- verified facts / decisions / active objective
   |-- untrusted observations / evidence pointers
   |-- policies enforced by controller (future)
   v
Context router -- retrieval budget --> adapter --> supported model
   |
Outcome verifier --> missing criteria / evidence / approval --> outcome state
```

Design principles: data portability, provenance, lazy loading, explicit access control, privacy at collection time, and evidence rather than agent self-report. A public example is **not** a substitute for authenticated policy enforcement or an encrypted production store.

## Interface sketch (not implemented)

- `inspect(card)`
- `retrieve(namespace, task, budget)`
- `propose_observation(event)`
- `verify_outcome(task, evidence, approval)`
- `export_card(namespace)`

## Scope

The demo deliberately excludes all private environment details and does not make claims of tested compatibility with individual model backends.
