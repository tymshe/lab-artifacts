#!/usr/bin/env python3
"""compaction_sizes.py: how big are your Claude Code compaction summaries?

Reads Claude Code session logs (default: ~/.claude/projects/**/*.jsonl), finds every compaction
(a `compact_boundary` event), and prints one line per compaction:

  session (first 8 chars of the file name), trigger (auto/manual), context before compaction
  (tokens, as logged by Claude Code), logged context right after, summary size in characters,
  summary size in tokens (estimated as characters / 4), and the ratio context-before / summary.

Then it prints medians. It prints counts only, never any message content.
Usage:  python3 compaction_sizes.py [--anon] [FILE_OR_GLOB ...]
        --anon  label sessions 1, 2, 3 ... instead of file-name prefixes (for sharing the output)     (Python 3.8+, standard library only)
"""
import glob, json, os, statistics, sys


def text_len(msg):
    c = (msg or {}).get("content") if isinstance(msg, dict) else msg
    if isinstance(c, str):
        return len(c)
    if isinstance(c, list):
        return sum(len(b.get("text") or "") for b in c if isinstance(b, dict))
    return 0


def meta(row):
    m = row.get("compactMetadata") or row.get("compact_metadata") or {}
    get = lambda *ks: next((m[k] for k in ks if isinstance(m.get(k), (int, float))), None)
    return (m.get("trigger") or "?"), get("preTokens", "pre_tokens"), get("postTokens", "post_tokens")


def scan(path, seen):
    rows = []
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(o, dict):
                    continue
                rows.append(o)
    except OSError:
        return []
    out = []
    for i, o in enumerate(rows):
        if o.get("type") != "system" or o.get("subtype") != "compact_boundary":
            continue
        key = o.get("uuid") or (path, i)
        if key in seen:          # the same compaction copied into a resumed or forked log
            continue
        seen.add(key)
        trigger, pre, post = meta(o)
        summ = None
        for r in rows[i + 1:i + 50]:   # the summary is the first compact-summary user message after the boundary
            if r.get("isCompactSummary"):
                summ = text_len(r.get("message"))
                break
            if r.get("type") == "system" and r.get("subtype") == "compact_boundary":
                break
        est = summ / 4 if summ else None
        out.append(dict(session=os.path.basename(path)[:8], trigger=trigger, pre_tokens=pre, post_tokens=post,
                        summary_chars=summ, summary_tokens_est=round(est) if est else None,
                        ratio=round(pre / est, 1) if (pre and est) else None))
    return out


def main(argv):
    anon = "--anon" in argv
    argv = [a for a in argv if a != "--anon"]
    pats = argv or [os.path.join(os.path.expanduser("~"), ".claude", "projects", "**", "*.jsonl")]
    files = sorted({p for pat in pats for p in (glob.glob(pat, recursive=True) or ([pat] if os.path.isfile(pat) else []))})
    seen, res = set(), []
    for p in files:
        res += scan(p, seen)
    if anon:
        ids = {}
        for r in res:
            r["session"] = ids.setdefault(r["session"], str(len(ids) + 1))
    print(f"files scanned: {len(files)}   compactions found: {len(res)}")
    if not res:
        return 0
    cols = ["session", "trigger", "pre_tokens", "post_tokens", "summary_chars", "summary_tokens_est", "ratio"]
    print("  ".join(cols))
    for r in res:
        print("  ".join("-" if r[c] is None else str(r[c]) for c in cols))
    def med(k):
        v = [r[k] for r in res if r[k] is not None]
        return (f"{k}: n {len(v)}, min {min(v)}, median {round(statistics.median(v), 1)}, max {max(v)}") if v else f"{k}: n 0"
    trig = {}
    for r in res:
        trig[r["trigger"]] = trig.get(r["trigger"], 0) + 1
    print("triggers: " + ", ".join(f"{k} {v}" for k, v in sorted(trig.items())))
    for k in ("pre_tokens", "summary_tokens_est", "ratio", "post_tokens"):
        print(med(k))
    print("summary_tokens_est = summary characters / 4 (logs carry no token count for the summary itself).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
