# Security and public disclosure

This is a **synthetic, non-production demonstration**, not a secure agent controller. It has no authentication, encryption, or enforced permissions. Never connect it to private memories, customer data, healthcare records, or privileged tools.

Only fictional fixtures may be committed. Exclude credentials, real logs, transcripts, personal details, internal architecture, endpoints, keys, databases, and production configuration.

Before production: threat model; validate schemas; enforce authorization at API boundaries; encrypt data at rest; store keys separately; test namespace isolation; audit writes; inspect telemetry and model-provider data flows; implement secure deletion and restore.

Before publishing changes: inspect the entire diff and commit history, run secret scanning, verify sample data is synthetic, and obtain owner approval. A `.gitignore` is not a security boundary.