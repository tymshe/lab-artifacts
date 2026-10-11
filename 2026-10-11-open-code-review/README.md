# review-effort.md

**Purpose.** Pick the Claude Code `/code-review` effort level for the kind of review comments you want:
few and mostly right (`low`) or more coverage with more noise (`medium`).

**When to use.** Local PR review with `/code-review` in Claude Code. Not measured: `high`/`max`, other
models, the GitHub App or cloud review, private repos.

**Steps.** Follow `review-effort.md` (exactly as tested): type `/code-review low` or `/code-review medium`
each time, because a bare `/code-review` reuses the last level you typed.

**How to verify.** On one PR whose real problems you know, run both levels and compare how many comments
each gives and how many point at a real problem. Run medium twice if you can; counts move between runs.

**What the test measured** (Claude Code 2.1.296, claude-sonnet-5-5, 16 public PRs from five large
open-source projects with 50 known issues; /code-review medium 2 runs per PR, low 1 run per PR; two
outside judges had to agree): low had 63% of its findings match a known issue and caught 42% of the known
issues; medium 28% and 71%. Not tested: whether teams keep trusting a quieter reviewer over time.
