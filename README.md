# lab-artifacts

Small files you can use in your own Claude Code work: scripts, prompts and checks, each exactly as it
ran in a measured test. One folder per test (named by date and topic). Each folder's README says what
the file is for, when to use it, how to use it, how to check it worked, and what the test measured,
with its sample size and limits.

| Folder | File | What it is |
|---|---|---|
| [2026-10-10-compaction-summary-size](2026-10-10-compaction-summary-size/) | `compaction_sizes.py` | Script: lists every compaction in your own Claude Code logs with context size, summary size and ratio |
| [2026-10-10-compact-instructions](2026-10-10-compact-instructions/) | `six-slot-instruction.txt` | Prompt: text to type after `/compact` so the summary is written as a handoff |
| [2026-10-10-plan-mode-vs-direct](2026-10-10-plan-mode-vs-direct/) | `plan-prompt.md`, `build-prompt.txt` | Prompts: write plan.md in one session, build it in a fresh one |
| [2026-10-10-agent-tests-quality](2026-10-10-agent-tests-quality/) | `check-agent-test-before-fix.md` | Check: does the test your agent wrote fail on the code before its fix? |
| [2026-10-11-open-code-review](2026-10-11-open-code-review/) | `review-effort.md` | Steps: pick the `/code-review` effort level for the comments you want |

Files are provided as is (see LICENSE). Numbers in the READMEs come from small runs; each README
states n and what was not tested.
