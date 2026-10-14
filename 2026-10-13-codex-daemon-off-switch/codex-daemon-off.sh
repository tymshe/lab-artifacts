#!/bin/sh
# Turn off Codex CLI's background app-server daemon and its updater, and remove the daemon's package copies.
# Tested on Linux only, Codex CLI 0.162.1 (2026-10-13, n=3). Not tested on macOS or Windows.
set -u
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"
codex features disable daemon_auto_start          # writes [features] daemon_auto_start = false to config.toml
codex app-server daemon stop                       # stops the daemon; the updater keeps running
pkill -f 'app-server daemon pid-update-loop'       # stops the updater
rm -rf "$CODEX_DIR/packages/app-server-daemon"     # removes the ~450 MB copy per version
sleep 2
echo "check (expect no lines below):"
# Matches only the CLI daemon and its updater. A desktop app's own bundled 'codex app-server' is expected and is not the daemon.
pgrep -af 'packages/app-server-daemon/|--managed-daemon|app-server daemon pid-update-loop'
exit 0
