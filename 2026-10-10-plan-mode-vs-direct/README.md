# plan-prompt.md and build-prompt.txt

**Purpose.** A two-session planning flow: the first session reads the code and writes plan.md (goal,
files, steps, check) and stops; a fresh session builds from plan.md.

**When to use.** When you want a written plan you can read or keep between sessions. In our test it did
not make the agent solve more tasks and cost more than asking directly, so it is not a default.

**Steps.**
1. Session 1: paste `plan-prompt.md`, then your task text. It writes `plan.md` and changes nothing else.
2. Read or edit `plan.md` if you want to.
3. Session 2 (fresh): paste `build-prompt.txt` ("Implement the plan in plan.md.").

**How to verify.** After session 1, `git status` shows only `plan.md` new; it lists every file to change
and a check command. After session 2, run that check.

**What the test measured** (Claude Code 2.1.295, claude-sonnet-5-5 at medium effort, 5 tasks in a copy
of the public Hono repo, 10 runs per arm): hidden tests passed on 8/10 runs asked directly, 7/10 in plan
mode with the plan approved unchanged, and 8/10 with this flow; plan mode cost 3.1x and this flow 2.4x
asking directly. At 10 runs per arm a gap under 5 passes is noise. Not tested: the value of a human
reading or correcting the plan, other models, repos or longer tasks.
