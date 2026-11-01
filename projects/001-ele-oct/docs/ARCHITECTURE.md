# Public architecture sketch

```text
Owner-controlled versioned memory card
  ├─ verified facts, decisions, objectives
  └─ untrusted observations and evidence references
       ↓
Namespace + policy enforcement (planned)
       ↓
Task-scoped retrieval → token budget → model adapter
       ↓
Evidence verification → owner approval → outcome state
```

Principles: lazy memory loading; minimal necessary context; data portability; provenance; isolation; no automatic promotion of observations to verified facts.

Proposed interfaces (not implemented): `inspect(card)`, `retrieve(namespace, task, budget)`, `propose_observation(event)`, `verify_outcome(task, evidence, approval)`, `export_card(namespace)`.

The public demo deliberately excludes private deployment details and makes no claims of validated provider compatibility.