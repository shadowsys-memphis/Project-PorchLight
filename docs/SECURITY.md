# Security notes

This is a synthetic demonstration, **not** a secure production agent controller. It has no authentication, encryption, or real policy enforcement. Do not connect it to private agent memories, patient records, customer data, or privileged tools.

Do not report vulnerabilities containing secrets or real logs. Reproduce against fabricated fixtures only. Before a production implementation, add threat modeling, authorization checks at API boundaries, audit logging, at-rest encryption and keys outside cards, schema validation, rate limits, isolation tests, and secure provider/telemetry settings.
