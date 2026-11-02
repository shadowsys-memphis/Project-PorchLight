# The 70K Hello Test

## Question
Does a greeting unnecessarily trigger large context reconstruction?

## Protocol
1. Record a fresh-session greeting baseline on the target runtime, without changing safety instructions.
2. Capture input, output, cache-read, cache-write, tool-result, and memory-injection tokens **separately**, when the provider exposes them.
3. Repeat at least five times under comparable conditions. Do not infer cache proportions from total usage.
4. Enable task-scoped lazy memory retrieval; repeat five times.
5. Compare median total token volume, uncached input, latency, cost where known, and response correctness.
6. Confirm essential operating instructions remain active and that later task-specific recall still works.

## Pass gate
A greeting loads no irrelevant project memory; savings are measured rather than assumed; a later project-specific task retains verified continuity. Report raw values and limitations. The historical ~70,000-token greeting is an unverified anecdote until trace evidence is obtained.