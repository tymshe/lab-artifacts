# six-slot-instruction.txt

**Purpose.** Ask Claude Code to write its compaction summary as a handoff: goal, your rules, decisions,
dropped approaches, state, open questions and the exact next step, each with its reason.

**When to use.** Before compacting a long session where your rules and the approaches you ruled out
matter for what comes next. Plain compaction in our test kept the current state reliably but your rules
and dropped approaches only about a third of the time.

**Steps.**
1. Type `/compact ` followed by the text in `six-slot-instruction.txt` (one line, exactly as it ran).
2. For auto-compaction, a PreCompact hook can print the same text; that route ran once in the test and
   did no better than plain compaction there.

**How to verify.** After compacting, ask the session for one of your rules and one approach you dropped,
and check the answer against what you said before compacting.

**What the test measured** (Claude Code 2.1.295, claude-sonnet-5-5, copies of 2 real ~1M-token sessions
of one user, 17 items, 2 runs per arm): plain `/compact` and auto-compaction kept the current state in
16 of 16 item-runs but the user's rules in 4 of 12 and dropped approaches in 4 of 12. This text typed
into `/compact` kept 28 of 34 item-runs vs 22 for plain `/compact`: a lean, not shown to help reliably
(per-item gain +14.7 points, 95% bootstrap interval -1.5 to 32.4). A generic "keep my rules" line kept
24 of 34. Not tested: other users, models or versions, several compactions in a row, whether the agent
keeps following the rules later, and work quality after compaction.
