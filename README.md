# Project-PorchLight

## ELE-OCT — Portable Agent Memory & Outcome Verification (Public Demo)

**By Porchlight — Project #001**
**Status:** Early public-facing *scaffold*, NOT a production memory service.

> Your memory. Your progress. Any **supported** model. Pick up where you left off.

## What is the problem?

Many AI tools remember activity but cannot reliably prove that a user's original objective was completed. Continuity across model providers is also fragile and context loading can be wasteful.

ELE-OCT explores an owner-controlled, model-independent card with: compact context budgets, explicit project boundaries, provenance-tagged observations, protected verified facts, and evidence-based task completion.

## What this repository contains

- `examples/demo-card.json`: completely fictional structured data.
- `src/verify.py`: **minimal illustrative** acceptance verifier, not a production security boundary.
- `tests/test_verify.py`: runnable standard-library tests for three evidence scenarios.
- `docs/ARCHITECTURE.md`: public, generic system overview.
- `docs/SECURITY.md`: limitations and responsible-use guidance.

This starter **does not** include user files, private agent transcripts, real model adapters, encryption, persistence services, or full access control. No universal model support is claimed.

## Quick demo

```bash
python3 -m unittest discover -s tests -v
python3 src/verify.py examples/demo-card.json
```

The demonstration intentionally marks an agent's claim of completion as **UNVERIFIED** until the criterion has evidence and approval. It does not access the network or any real provider.

## Roadmap

1. Read-only synthetic card inspector; strict schemas.
2. Token-budgeted retrieval with provider-specific metrics.
3. Adapter prototypes for Claude Code, LM Studio and Ollama.
4. Secured verification API and human authorization.
5. Reproducible 70K Hello Test methodology (not a claim of proven savings).

## Contributing

Issues with minimal reproductions and synthetic examples are welcome after publication. Please do not submit private project data, logs, or credentials. Be respectful of maintainers of related projects; no affiliation with Claude-Mem, Anthropic, LM Studio, or Ollama is implied.

## License

**To be selected and approved before public release** (e.g., MIT or Apache-2.0); this starter deliberately makes no license grant until a license file is added. Do not publish as an open-source release without resolving this.
