# codex-daemon-off.sh

**Purpose.** Turn off Codex CLI's background app-server daemon and its updater (`pid-update-loop`),
and remove the daemon's package copies, so no Codex background processes are left running.

**When to use.** On a Linux dev box, CI runner or shared machine where Codex CLI has already run with
the default and you want no Codex background processes. **Tested on Linux only** (Codex CLI 0.162.1);
not tested on macOS or Windows. Skip it if you want Codex to keep auto-updating itself: with the
daemon off you update Codex by hand. On a fresh machine, `codex features disable daemon_auto_start`
alone was enough; `codex --no-daemon` per session also left nothing.

**Steps.** Run it once with `sh codex-daemon-off.sh` (it uses `$CODEX_HOME` or `~/.codex`), exactly as
tested. Rerun the check line after every Codex update.

**How to verify.**
`pgrep -af 'packages/app-server-daemon/|--managed-daemon|app-server daemon pid-update-loop'`
No output (exit code 1) means neither the daemon nor the updater is running. If only the
`pid-update-loop` line is left after `daemon stop`, the updater is still alive: kill it. If the
ChatGPT/Codex desktop app is open, its own bundled `codex ... app-server` is expected and is not the
CLI daemon; this pattern skips it.

**What the test measured** (Codex CLI 0.162.1, npm, Linux x86_64, 3 runs per setup, each from an empty
Codex home, process lists after each session and 70 s, 5 min and 6 min later): the default left 2
processes (daemon + updater) in 3 of 3 runs; `daemon stop` alone left the updater running 70 s later in
3 of 3; this script's full recipe left 0 in 3 of 3, through 3 more interactive sessions, 3 `codex exec`
turns and 6 minutes of waiting. Each daemon package copy was 452470422 bytes, and a forced update kept
the old copy (904940986 bytes for 2 versions). Not tested: macOS, Windows, IDE/desktop-app clients,
remote-control mode, a real release landing, the hourly updater cycle.
