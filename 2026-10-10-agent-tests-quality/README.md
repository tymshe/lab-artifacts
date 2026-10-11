# check-agent-test-before-fix.md

**Purpose.** A quick check of a test your coding agent wrote with its fix: run it on the code before the
fix. If it passes there too, it does not test the fix.

**When to use.** Whenever an agent adds a test next to a bug fix and you plan to keep it.

**Steps.** Keep the agent's test file, put the source files back to the pre-fix version (for example
`git stash`, or `git checkout <base> -- <source files>`), run the test and expect it to fail; restore the
fix and expect it to pass. The exact text is in `check-agent-test-before-fix.md`.

**How to verify.** The test fails on the pre-fix code and passes with the fix. A test that passes both
times is not useless: in our test most such cases guarded behaviour the task said to keep (for example
"numbers should keep working"). It just doesn't test the fix.

**What the test measured** (Claude Code 2.1.295, claude-sonnet-5-5 at medium effort, told by one CLAUDE.md
line to write and keep tests, 15 fixes in a copy of the public Hono repo, 1 run each): of 30 test cases,
23 failed before the fix and passed after; 7 passed both, and by our reading 6 of those 7 are edge-case
or keep-old-behaviour guards. The check does not catch a test that fails before the fix but checks too
little: in one case a kept test passed while the fix was incomplete.
