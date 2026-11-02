# ELE-OCT — Portable Agent Memory & Outcome Verification (Public Demo)

**PorchLight — Project #001**  
**Status:** Early public scaffold; NOT a production memory service.

> Your memory. Your progress. Any supported model. Pick up where you left off.

## Purpose
ELE-OCT explores user-owned portable memory, selective context retrieval, token efficiency, and evidence-based verification. The memory card should preserve continuity without repeatedly injecting full histories.

## Contents
- `examples/demo-card.json`: synthetic data only.
- `src/verify.py`: illustrative outcome-verification function; not a security boundary.
- `tests/test_verify.py`: four standard-library unit tests.
- `docs/ARCHITECTURE.md`: public design sketch.
- `docs/SECURITY.md`: security limitations.
- `docs/ROADMAP.md`: proposed dated milestones and acceptance gates.
- `benchmarks/70k-hello-test.md`: reproducible measurement protocol.

## Run
```bash
python3 -m unittest discover -s projects/001-ele-oct/tests -v
python3 projects/001-ele-oct/src/verify.py projects/001-ele-oct/examples/demo-card.json
```

This scaffold has no live model integrations, production authentication, encryption, or persistence. It does not claim measured token savings or universal compatibility.

## Contributing
Use fictional data and minimal reproducible examples. Never submit secrets, private logs, transcripts, customer data, or proprietary configurations. This project is not affiliated with Claude-Mem or any model provider.

## License
No license has been granted yet. A license will be selected before an open-source release.