# br(AI)n (Sovereign Staff Governor)

| | |
| --- | --- |
| Status | Prototype |
| Approx. date | May 21, 2026, written in the source. The surrounding caregiving work continues into June. |
| Screenshot | None published. The review's captures included family and health context and were held out of this repo. |

## What it claims

The project description presents an elite AI orchestrator for caregiving, with an admin panel and a daily view.

## What the source does

An Express server with JSON-file endpoints for a ledger, a brain file, state, and a schedule, plus an admin panel and a daily view. Persistence is real. The reviewed source contains no Gemini calls.

Description text and metadata included private health context. That text is omitted.

## Stack

Vite plus Express. JSON files as the store. No model client in the reviewed source.

## What it shows

A first caregiving prototype with real local persistence, and a reminder to read descriptions against the source. The orchestrator claim is roadmap copy on top of a file-backed admin and daily view. The later [Veteran Daily Routine Tracker](veteran-daily-routine-tracker.md) and [Care Giver OS](care-giver-os.md) are where the care line grows past this shell.
