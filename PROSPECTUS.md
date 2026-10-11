# Build AI, Understand AI: Prospectus

Date: 2026-10-11. Status: skeleton and outline; no chapters written.

The doing lives in the companion package `michael-borck/hands-on-ai`
(`pip install hands-on-ai`): eight modules, roughly forty documentation
pages and fifty-five project guides. This book is the narrative the
package leaves out: the why, the progression, and the misconceptions
each module kills. Package and book cross-link; neither duplicates the
other.

## Thesis

Most people now use AI systems daily and understand none of them. The
tools hide the machinery, the machinery is genuinely simple, and the
gap between those two facts is where confident nonsense gets shipped.
Every module in the companion package reduces to one call to the model
wrapped in plain Python: chat adds a system prompt, retrieval adds
code that fetches context, an agent adds a loop that runs your
functions, a workflow adds folders, a loop adds a goal, an eval adds
a judge. A reader who builds each of those in miniature, in an
afternoon each, stops being fooled by demos.

The bet is the package's bet: models change every few months, the
ideas underneath change slowly. The book teaches the ideas and uses
the package as the vehicle, the way a physics course uses a lab kit.
No training, no gradients, no maths prerequisites. The reader writes
a little Python (taught in an appendix) and reads a little more.

## Audience and boundaries

The reader who uses AI tools and wants to know what is underneath
them. Minimal programming; every Python construct used is taught in
Appendix A. Boundary statement for "What this book is not":

- Not a Python course. Appendix A supplies just enough; *Code
  Python, Consult AI* teaches the language itself.
- Not *Speak Software*. That book directs agents without code; this
  one opens the box the agents are built on. A routing note in the
  preface sends the never-touch-a-keyboard reader there first.
- Not *Ship Python, Orchestrate AI*. Workflows, loops and judges
  appear here in miniature, to be understood, not in production
  form, to be shipped.
- Not a machine-learning book. No training, no tensors. The model
  is a black box with a documented front door; the book is about
  everything on this side of that door.

## Position in the series

Thirteenth title. Sits on the Python track beside *Code Python,
Consult AI* as the "how the machine works" half of the curriculum:
that book teaches the language, this one teaches the thing the
language is talking to. It is also the natural second book for the
*Speak Software* graduate who wants to see underneath the intern.
The package (`hands-on-ai`) is to this book what the labs repo is
to *Speak Software*: the living, versioned doing.

## Sources to cite

- The package's own philosophy document ("learning lab, not a
  production framework"; smallness as the feature).
- The ReAct paper (reason and act in language models).
- The original RAG paper (retrieval-augmented generation).
- Karpathy on vibe coding and on NanoGPT (the "go deeper" exit).
- The author's *Conversation, Not Delegation* for the judge-as-
  literacy argument and the Conversation Loop.

## Chapter plan

Fourteen chapters in five parts. Every chapter: one concept, one
module of the package, one misconception killed, one small build.

| Part | Chapter | Kills the misconception |
|---|---|---|
| I. The Model | 1. One Call to the Model | "AI is magic" — it is one function call over HTTP |
| | 2. Who the Model Is Being | "the AI has a personality" — a system prompt is just text in the request |
| | 3. No Memory Between Calls | "it remembers me" — statelessness, context windows, token budgets |
| | 4. Any Provider Will Do | "I'm locked into one vendor" — OpenAI-compatible endpoints, local models |
| II. Grounding | 5. What the Model Doesn't Know | "it knows everything" — cutoffs, hallucination, the need for evidence |
| | 6. Chunk, Fetch, Answer | "RAG is a framework" — it is search, then a prompt with the search results in it |
| III. Action | 7. Giving the Model Hands | "agents are products" — a tool is a function the model may ask for |
| | 8. The ReAct Loop | "the agent thinks" — reason, act, observe; a loop you can read |
| IV. Control | 9. Workflows as Folders | "orchestration needs a framework" — numbered folders of reviewable stages |
| | 10. Loops with a Goal | "more steps means better" — do, check, repeat; the ratchet keeps only wins |
| | 11. The Judge | "I can eyeball quality" — the LLM judge, and why judging is the new literacy |
| V. The Senses | 12. Pictures | "vision is different" — images go in, descriptions come out, same call |
| | 13. Voice | "voice AI is different" — transcribe, think, speak; a loop around the chat loop |
| — | 14. The Shape Underneath (conclusion) | "I need to learn a framework" — everything was one call plus plain Python |

## Appendices

| Appendix | Purpose |
|---|---|
| A. Just Enough Python | Variables, functions, loops, dictionaries, f-strings: every construct the book uses, taught in ten pages |
| B. Model Access | Providers, keys, free local models with Ollama, cost notes, the cache for reproducible classroom reruns |
| C. The Project Gallery | The package's project guides mapped by module and difficulty, with suggested capstones |
| D. Going Deeper | The exit map: real SDKs, LlamaIndex, Pydantic AI, Pipecat, Karpathy's Zero to Hero |

## Companion package responsibilities

The book relies on but does not duplicate: module reference docs, the
project guides, the quickstart notebook, the classroom setup guide.
Book-side tools to build later: nothing yet; the check script only.
Open question for later: whether worked listings live in the book
(frozen, pinned to a package version) or in the package repo
(living). Leaning frozen-in-book with version pinned per chapter.

## Publication model

Quarto book in this workspace, standard series pipeline (licence
files, collection licence check, rendered-book validation, source
checks; register in `book-publisher/books.yml` when the first real
chapter lands). Formats: HTML primary; PDF/EPUB via the standard
print pipeline. Cover after the draft stabilises.

## Writing queue (2026-10-11)

Done: skeleton (14 chapter stubs, 4 appendices), prospectus, licence
files, preface draft, check script adapted from *Speak Software*.

Next, in order:
1. Part I first draft (chapters 1–4) against the package's current
   release; pin the version in RESOURCES.
2. Appendix A (Just Enough Python) early, since every chapter
   depends on its constructs.
3. Parts II–IV; Part V last (vision and voice demos age fastest).
4. Project gallery appendix once capstones are chosen.
5. Fresh-reader pass, print build, cover.
