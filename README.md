# Build AI, Understand AI

**How Modern AI Systems Actually Work, in Small Readable Pieces**: a book for people who use AI every day and want to know what is underneath. Build tiny versions of chat, retrieval, agents, workflows, loops, judges, vision and voice, and see that all of them are one model call wrapped in plain Python.

Part of the [books.borck.education](https://books.borck.education) series. The hands-on companion is the [hands-on-ai package](https://michael-borck.github.io/hands-on-ai/) (`pip install hands-on-ai`).

## Status

In progress: prospectus, preface draft, and Part I (Chapters 1 to 4) drafted against `hands-on-ai` 0.6.0. The remaining 10 chapters and 4 appendices are stubs. See `PROSPECTUS.md` for the plan and the writing queue.

## Build

```bash
quarto render
```

## Checks

```bash
python scripts/check_manuscript.py
```

## Licence

Book content: [CC BY 4.0 International](https://creativecommons.org/licenses/by/4.0/)
([LICENSE-CONTENT.md](LICENSE-CONTENT.md)). Original code examples and accompanying software
(including the check script in `scripts/`): [MIT License](https://opensource.org/licenses/MIT)
([LICENSE-CODE.md](LICENSE-CODE.md)). See [LICENSE](LICENSE) for scope.

Separately credited third-party material retains its stated terms.
