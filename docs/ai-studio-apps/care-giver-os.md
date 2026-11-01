# Care Giver OS

| | |
| --- | --- |
| Status | Prototype |
| Approx. date | June 22–July 6, 2026. |
| Screenshot | None published. The review's captures included family and health context and were held out of this repo. |

## What it claims

A caregiver operating view with summaries, a voice companion, calendar and drive actions, and an outbound call control.

## What the source does

Express plus Gemini. Summaries use `gemini-3.5-flash`. Voice uses a Flash text-to-speech path. Calendar event creation and Drive export use the caller's OAuth token. Summary and assistant endpoints are real.

The outbound call endpoint writes a log line and stops there.

The export includes spec habits that show up across this body of work: `AGENTS.md`, a handoff note, an intake protocol, schema-mapping notes, and skill scripts for a follow-on agent. Those files also contained private health detail. The detail is omitted. No token, calendar id, or document id is published here.

## Stack

Vite plus Express. Gemini 3.5 Flash for summaries. Flash TTS for voice. Google Calendar and Drive through the caller's OAuth token.

## What it shows

Live integration on the care side (calendar and drive, under the caller's own token) next to the same spec-writing habit as the market handoffs. The call control is a stub. Governance here is the boundary around what the assistant is allowed to do with the caller's account, and the decision to keep health context out of a public record.
