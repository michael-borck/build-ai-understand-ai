# Build AI, Understand AI: Prospectus

Date: 2026-10-11. Status: first draft complete including the advanced arc (2026-10-19); fresh-reader pass, live listing run, adapter training run, print build, and cover pending.

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
No training, no gradients, no maths prerequisites in Parts I to V
(the optional Part VI fences its training off; see the advanced
arc plan below). The reader writes
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
- Mostly not a machine-learning book. Parts I to V: no training,
  no tensors; the model is a black box with a documented front
  door. Optional Part VI opens the box a crack in notebooks, at
  toy scale, with its own stated prerequisites.

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
Done 2026-10-18: Chapter 1 (*One Call to the Model*) drafted as the
pilot chapter, pinned to `hands-on-ai` 0.6.0 in the chapter header.
Registered as `build` in `book-publisher/books.yml` and
`publishing.yml`. Pilot sets the per-chapter pattern: epigraph,
package companion and version pin, misconception, build, Python
needed, concept first, real-life analogy, the build, a curtain-back
section, failure modes, where a demo can mislead, five graded
exercises, summary, reflection, journal, next steps.

Done 2026-10-18 (continued): Chapters 2 to 4 drafted, completing
Part I, each checked against the `hands-on-ai` 0.6.0 source
(`pirate_bot` listing is the package's own function; `Conversation`
save format, config precedence, and cache-off default verified by
running the package offline). One skeleton note corrected in the
writing: packaged bots take no `return_usage` argument, so Chapter 2
measures instruction cost through the reader's own bot instead.

Done 2026-10-18 (Part II pass): Appendix A drafted early, as the
queue asked; all 17 of its examples run and match their printed
output. Chapters 5 and 6 drafted, completing Part II, against
`hands_on_ai.rag` (`chunk_text` output in Chapter 6 is program
output; index save/load and `get_top_k` ranking verified offline
with test embeddings; live embedding calls still need an author
run against a reachable server).

Done 2026-10-18 (Part III pass): Chapters 7 and 8 drafted against
`hands_on_ai.agent`. Tool execution, the calculator description
mismatch (its dictionary-style example errors when fed to its own
function), ReAct parsing, and all three loop exits verified offline
with a scripted model. Live agent runs still need an author pass;
note that `format="react"` on small local models is expected to
wobble, and the richer `agent/agents/` tools with multi-argument
signatures do not fit the registry's one-string calling convention,
so the chapters build only on one-argument tools.

Done 2026-10-18 (Part IV pass): Chapters 9 to 11 drafted against
`hands_on_ai.workflow`, `hands_on_ai.loop`, and `hands_on_ai.eval`.
Workflow run/review/reset cycle, loop budget exit, ratchet
keep-only-wins log, and judge parsing (including score clamping
and unparsable replies returning `None`) verified offline with
scripted stand-ins. Part III committed and pushed as `0728bbb`
before this pass.

Done 2026-10-18 (completion pass): Part IV committed as `744846f`
(local, ahead of origin at time of writing). Chapters 12 to 14 and
Appendices B to D drafted against `hands_on_ai.vision`,
`hands_on_ai.voice`, and the package project guides, completing
the first draft at roughly 37,000 words. Vision payload shape and
voice error behaviour verified offline; live vision and audio
calls still need an author run with a vision model and audio
servers reachable.

## Advanced arc plan (recorded 2026-10-18; approved and executing)

Goal: two additions without breaking the learning-lab pitch.
(1) Typed, fast judgments (structured output / System 1 style) as
a first-class primitive. (2) Part VI, an optional advanced arc
that demonstrates training, fine-tuning, and preference learning
at toy scale, for understanding rather than production use.

Contract change: Parts I to V keep the no-training, no-new-maths
promise and treat the model through its documented front door.
Part VI is optional, opens the box a crack in notebooks, declares
extra prerequisites (PyTorch for the tiny-model notebook; a Colab
GPU for the adapter), and is simplified, never production-ready.
Readers who stop at the conclusion lose nothing. Preface,
prospectus boundaries, and README are amended, not quietly bent.

Typed Answers: one new chapter at the end of Part IV, after The
Judge (Judge stays Chapter 11), written against a new
`hands_on_ai.decide` module (classify, decide, score_output,
extract) on the existing Instructor/Pydantic stack. Local
schema-constrained backend by default; optional TypeSafe Jev
backend (`TYPESAFE_API_KEY`) for calibrated-probability
comparison; local confidence is self-reported and uncalibrated
and the text says so. `eval.judge` is refactored onto the shared
structured core while keeping its `{score, reasoning, raw}` API.

Part VI (Inside the Box), three committed chapters plus a gate
(a classical-ML bridge, *The Older AI in the Room*, added at its
head on 2026-10-19 with the naming/scope fixes below):
Train a Tiny Model (one CPU/Colab notebook, character-level tiny
transformer, loss and sampling visible); Teach It a Dialect
(SFT LoRA adapter distilled from the LocoLabo capstone notebook,
50 to 100 examples at book scale, sealed eval, GGUF to Ollama,
negative result legitimate), with Learn from Preferences (DPO on
judge-ranked pairs; GRPO only with a Python-checkable reward) as
a section of that chapter unless an actual adapter run produces
usable pairs worth a separate chapter. Training code lives in
`hands-on-ai/notebooks/`, never in the installable package; no
torch or Unsloth in core dependencies. Karpathy pointers in
Appendix D move from nanoGPT to nanochat/MicroGPT after primary
re-verification at drafting time.

Execution checklist (update as items land):

- [x] 1. Package: `hands_on_ai.decide` with offline tests;
      judge refactored onto it, API unchanged.
- [x] 2. Book: contract amended; stubs added; conclusion moved
      last; `_quarto.yml` order updated.
- [x] 3. Book: Typed Answers chapter against shipped `decide`.
- [x] 4. Notebook: `train_tiny_model.ipynb` executed end to end;
      Part VI Chapter 1 written against its artefacts.
- [x] 5. Notebook: distilled adapter notebook; Part VI Chapter 2
      written (DPO section per the gate above).
- [x] 6. Conclusion and Appendix D updated to six drawers;
      checks, render, audit green.

Validation: package tests scripted offline plus one live local
run per primitive (and Jev if a key exists); notebooks executed
with outputs saved; manuscript checks extended; full render with
cross-references resolving; chapter-number prose swept after
renumbering. Highest risk: an actual adapter training run (GPU
and time). If it cannot be completed honestly, Part VI ships at
the tiny-model chapter plus the adapter chapter written against
the LocoLabo notebook with its run explicitly marked author-side.

Next beyond this plan, in order:
1. Author fresh-reader pass over the whole draft, including one
   live run of every model-dependent listing.
2. Print build (PDF/EPUB via the standard pipeline; the audit's
   print-support files are still missing) and cover design,
   including registry entries in `book-publisher/design/`.
3. Listings stay frozen in the book, pinned per chapter (the
   `decide` chapters pin the package version that ships it).

Naming audit (2026-10-19): subtitle and package tagline scoped
to LLM systems; preface gains an explicit AI-field note; the
classical bridge chapter and classical_ml notebook added so the
title umbrella is earned narrowly rather than merely excused.
No rename: PyPI/import installed base and series pattern kept.
