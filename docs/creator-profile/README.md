# Ray Jessee — creator profile

Public notes on a year of Google AI Studio apps, November 2025 through October 2026. Each app is labeled **Shipped**, **Prototype**, **Concept**, or **Not reviewed**. Concept pages are roadmap. Market pages are experiments with simulated or read-only data.

The live profile page is [here](https://cursor.com/canvas/store-b0bd88f2-8b81-44e5-ace0-b32437e614b5/c95f6d54-d3d4-4bda-87f9-ceb736dcba6b). The app-by-app record is the [AI Studio index](../ai-studio-apps/README.md). Where the underlying projects live is in [sources](../sources.md).

## Positioning

Ray builds with AI coding tools, and he designs, tests, and debugs the systems those tools produce. The studio exports show five roles, often in the same project.

**Product architect.** The early shells are small (a metrics dashboard, a landing page). Later exports are multi-panel consoles: a command center, a node map, an ambient companion, an operator console with a human approval step. He is composing a product surface, then filling it in.

**Domain constraint designer.** Risk rules show up as something an agent can be graded against: a weighted score, a written constitution, ring privileges, a numeric snipe gate, a manual approval queue. The interesting artifact is the rule, not the chart around it.

**Live integration tester.** The strongest engineering export, iShadow, calls real market-data sources and a read-only exchange accounts endpoint, writes nightly briefings, and keeps a history archive. The execute path in that export is an explicit mock. Other dashboards paint simulated numbers in a live-looking layout, and these pages say so.

**Incident diagnostician.** The earliest known artifact, TradeOps Recovery Console, is a November 2025 description of diagnosing a bot failure and an exchange auth problem. That project was not in the reviewed exports, so the claim stays unverified. Inside the reviewed set, the iShadow handoff records a broken authenticated read (a missing path prefix and the signed request URI). Exports that called a fixed host or a hard-coded socket are described here without those addresses.

**Governance enforcer.** Across the year the same rule gets sharper and more executable: the model may recommend, and a gate decides. In the SS_III constitution the operator outranks the constitution, the constitution outranks the gate, and the gate outranks the AI. Later care work carries the same idea into routine tracking for a Veteran family member, and into a private system kept off this repo.

## Core theme

**AI advises, rules decide.**

The sequence in the exports:

1. **SovereignShadow Assistant** (~November 2025) puts the rules in the agent's instructions: a five-factor score with a threshold of 60, a loss-limit ladder (per trade, day, week, emergency stop), a hot/cold capital split, and an adversarial "Brutal Critic" role. Prices and scores in that build are generated randomly.
2. **SS_III** (~February 2026) moves the rules into a constitution file: exposure caps, drawdown limits, an emergency threshold, a cap on consecutive losses, an asset allow-list, and a mode table. Normal and Caution can allow new positions. Degraded and Emergency block them. Exchange failure drops the mode to Degraded. Every recommendation, gate decision, and mode change is written to an audit log. The agent, Ralph, cannot open or close positions.
3. **KernelGuard** (June 2026, approximate) restates the split as an operating system. Strategies sit in user space. Capital sits in the kernel. Requests such as allocating capital are allowed or denied by control laws borrowed from fly-by-wire (Normal, Alternate, Direct, Flare). A process whose risk passes 90 is killed. Degraded modes shrink exposure on their own. The telemetry on screen is random. The rules are deterministic.
4. **Shadow Platform 3** (July 2026, approximate) turns the written rulebook into a score. Reserve, an alt-exposure cap, per-order risk, and a penalty for crowded venues produce a Snipe Score. The screen authorizes a snipe only above 7.5, and it logs a "risk crush" when size exceeds the limit. The log is labeled a simulation in the app.
5. **Steward** (October 2026, approximate) puts a person in the loop. Work moves from backlog, to scanning, to awaiting a gate, to executed. Authorization is manual. The console keeps an audit log and an operator "tilt" posture. The socket client stops reconnecting after three attempts.
6. The caregiving line applies the same instinct to a daily routine: local persistence, alarms, and a quarter-of-day schedule. The review describes a later private system with guard scripts and a localhost lock. That system is not in this repo.

## Growth timeline

Dates are approximate when they come from an AI Studio "Updated" stamp. See [sources](../sources.md).

| When | What changed | Label |
| --- | --- | --- |
| Nov 2025 | TradeOps Recovery Console, known from a description of bot-failure and exchange-auth diagnosis. Source was not in the review set. | Not reviewed |
| ~Nov 21, 2025 | SovereignShadow Assistant. A native-audio session whose real content is the governance spec. Signals are simulated. | Prototype |
| Late 2025 / early 2026 | Sovereign Shadow II, a small Gemini shell with decorative metrics. Shadow.Ai AlphaRunner, a large paper-mode council with structured model output. AlphaRunner's bridge host is omitted. | Prototype |
| Jan 15–Aug 18, 2026 | Veteran Daily Routine Tracker. Entries span those dates. Local routines, alarms, journal, and mini-games for a Veteran family member. UI ancestor of the private BrainGuardian system. | Prototype |
| ~Feb 16, 2026 | SS_III constitution timestamp. Clearest statement of "AI advises, rules decide." Visuals are an explainer with randomized flow values. | Prototype |
| Apr 2026, approximate | FleetControl AI, a client-style concept for salt-truck fleet ops. Map and reports around a simulated position feed. | Concept (roadmap) |
| Apr 15 and Jul 15, 2026 | Dates written in the Shadow.AI Command Center & Auditor source. Largest Shadow UI. Chat endpoints are real. Repo audit, API-hub pings, and market tiles are simulated. | Prototype |
| May 21, 2026 | Date written in br(AI)n (Sovereign Staff Governor). File-backed caregiving screens. The export's orchestrator description has no model calls behind it. | Prototype |
| Jun 2026, approximate | KernelGuard ring simulation. SHADOW.AI landing page, a static positioning piece. | Prototype, and Concept (roadmap) |
| Jun 22–Jul 6, 2026 | Care Giver OS. Summaries, voice, calendar creation, and drive export. The outbound-call endpoint writes a log. Spec and handoff notes ship in the export. | Prototype |
| Jul 2026, approximate | iShadow / NightOwl (read-only market and account integration). Shadow Platform 3 (executable simulation gate). OpenShadow (research endpoint with an offline fallback). | Prototype |
| Oct 2026, approximate | Shadow AI Prototype, an ambient assistant shell. Steward, an operator console whose main mechanic is the approval gate. | Prototype |

Every AI Studio export in this review is Prototype, Concept, or Not reviewed. The review describes a later caregiving system with a real user. That system lives in the private BrainGuardian repo and sat outside the 16-export source read.

From November 2025 through July 2026 the experiments are mostly about markets. From May 2026 the caregiving prototypes run alongside them. The governance habit is what both lines share.

Several July pages were last stamped July 29–30, 2026, in a cluster of six apps. That stamp is a re-save, not a creation date. Sovereign Shadow II, AlphaRunner, and SS_III are named in the review as carrying the July 30 stamp.

## How the work was built

The exports include the habits of someone directing coding agents: handoff notes, an `AGENTS.md` style spec, a generator that writes change requests for a coding agent, and an in-app "council" that maps roles to tools (a coding agent, a swarm consensus at 75 percent, a Gemini orchestrator). AlphaRunner's documented loop is paper mode. iShadow includes a written handoff for a follow-on coding agent.

Public copy has to stay level with the source. Many screens use live styling on simulated data. The [app index](../ai-studio-apps/README.md) records the gap app by app.

## Replit projects (pending)

None documented yet.

## Live demos (coming soon)

None linked yet.
