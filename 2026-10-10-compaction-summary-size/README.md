# compaction_sizes.py

**Purpose.** See how much history each Claude Code compaction squeezed into its summary, on your own
sessions: for every compaction, the context size before it, the summary size, and the ratio.

**When to use.** You run long sessions and want to know whether compacting later (near the full window)
or earlier changes how much the summary has to carry. Not a quality check: it measures size only.

**Steps.**
1. `python3 compaction_sizes.py` reads `~/.claude/projects/**/*.jsonl` by default (or pass files or globs).
2. Add `--anon` to label sessions 1, 2, 3 instead of file-name prefixes before you share the output.
3. Python 3.8+, standard library only. It prints counts only, never message content.

**How to verify.** The first line says how many files were scanned and compactions found. Each row shows
trigger (auto/manual), tokens before (as logged by Claude Code), tokens after, summary characters,
summary tokens (estimated as characters / 4) and the ratio; medians follow. If it finds 0 compactions,
check the path: it looks for `compact_boundary` events.

**What the test measured** (Claude Code 2.1.217 to 2.1.284, mostly claude-opus-5-5, one user): in 22
manual `/compact` runs on 6 sessions at 649,581 to 1,039,469 tokens, summaries stayed at about 3,480 to
6,019 estimated tokens, a median 194.3x shrink; one replayed session compacted at 402,128 tokens
shrank 68.7x. Not tested: auto-compaction at the default window, other users and projects, and what
the summaries keep or lose.
