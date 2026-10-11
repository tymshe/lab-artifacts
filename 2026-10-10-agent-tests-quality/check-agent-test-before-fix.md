Run the agent's new test against the code before the fix. If it passes there, it isn't testing your fix.

How: keep the agent's test file, put the source files back to the pre-fix version (e.g. git stash or git checkout <base> -- <source files>), run that test and expect it to fail; restore the fix and expect it to pass.
