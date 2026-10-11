# Pick the /code-review effort for the comments you want (Claude Code 2.1.296)

- Few, high-confidence comments: `/code-review low`. On 16 public PRs (claude-sonnet-5-5), 63% of its findings matched a known issue, and it caught 42% of the known issues, at about 2 comments per review.
- Coverage: `/code-review medium`. 28% matched and 71% caught, at about 8 comments per review.
- Type the level every time (`/code-review low` or `/code-review medium`): a bare `/code-review` reuses the last level you typed.

Check it on your own code: pick one PR whose real problems you already know, run `/code-review low` and then `/code-review medium` on it, and compare (1) how many comments each gives and (2) how many of those point at a problem you know is real. Run medium twice if you can, because counts move a little between runs.
