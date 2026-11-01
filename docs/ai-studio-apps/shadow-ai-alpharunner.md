# Shadow.Ai AlphaRunner

| | |
| --- | --- |
| Status | Prototype |
| Approx. date | Late 2025 or early 2026, from `@google/genai` 1.30.x and Gemini 3 Pro preview / 2.5 Flash ids. AI Studio stamp July 30, 2026 (bulk re-save). |
| Screenshot | None. The app did not render in the headless review. The model client is created at import, so the pass stopped without a key. |

## What it claims

A strategy studio: classify strategies, keep a knowledge graph, generate prompts for a coding agent, and convene an AI council. The council maps roles onto tools: Claude Code, a swarm that requires 75 percent consensus, and a Gemini orchestrator.

## What the source does

The largest early app in the set: about 5,400 lines across 23 files. Eleven Gemini calls use structured JSON schemas (`gemini-3-pro-preview` and `gemini-2.5-flash`) to classify strategies into categories such as Vault, Sniper, and Ladder, to build a knowledge graph, and to write change requests a coding agent could apply.

A bridge client expects a backend on a fixed host over plain HTTP. Without that backend the panels are empty placeholders. The host address is a security smell and is omitted here. The run notes describe the loop in paper mode.

## Stack

Vite. `@google/genai` ^1.30. Structured-output calls to Gemini 3 Pro preview and Gemini 2.5 Flash. A separate bridge process that was not part of a safe public deployment.

## What it shows

Multi-agent orchestration as a design: structured prompts, a council of roles, and a prompt generator aimed at a coding agent. The documented execution mode is paper. The bridge, as exported, is an incident note, not a deployment guide.
