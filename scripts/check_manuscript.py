#!/usr/bin/env python3
"""Smoke checks for the Build AI, Understand AI skeleton (stdlib only).

The book is in development; these guard the invariants that already
hold — clean sources, series-standard licences, the boundary statement,
configured chapters present — and will grow as chapters are written.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
    "ship-it-python-in-production",
)


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def qmd_files():
    return skip_appledouble(sorted(ROOT.glob("**/*.qmd")))


class ManuscriptChecks(unittest.TestCase):
    def test_all_configured_files_exist(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        names = re.findall(r"^\s*-\s+(\S+\.qmd)\s*$", config, re.M)
        self.assertGreaterEqual(len(names), 20)
        for name in names:
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file(), name)

    def test_licence_files_present_and_adapted(self):
        for name in ("LICENSE", "LICENSE-CONTENT.md", "LICENSE-CODE.md"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file(), name)
        licence = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Build AI, Understand AI", licence)
        self.assertNotIn("Speak Software", licence)
        legal = (ROOT / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
        self.assertIn("Attribution 4.0 International", legal)

    def test_boundary_statement_present(self):
        text = (ROOT / "index.qmd").read_text(encoding="utf-8")
        for marker in ("not a Python course",
                       "Speak Software",
                       "Ship Python, Orchestrate AI"):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_sources_are_clean(self):
        for path in qmd_files():
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=str(path)):
                self.assertNotIn("{mermaid}", text)
                for target in STALE_LINKS:
                    self.assertNotIn(target, text)

    def test_prospectus_exists(self):
        prospectus = (ROOT / "PROSPECTUS.md").read_text(encoding="utf-8")
        self.assertIn("one call to the model", prospectus.lower())
        self.assertIn("hands-on-ai", prospectus)
        self.assertIn("Chapter plan", prospectus)

    def test_written_chapters(self):
        written = {
            "chapters/one-call.qmd": ("get_response", "{#sec-one-call}"),
            "chapters/who-the-model-is.qmd": ("pirate_bot", "{#sec-who-the-model-is}"),
            "chapters/no-memory.qmd": ("Conversation", "{#sec-no-memory}"),
            "chapters/any-provider.qmd": ("HANDS_ON_AI_SERVER", "{#sec-any-provider}"),
            "chapters/what-the-model-doesnt-know.qmd": ("grounded_by_hand", "{#sec-what-the-model-doesnt-know}"),
            "chapters/chunk-fetch-answer.qmd": ("get_top_k", "{#sec-chunk-fetch-answer}"),
            "chapters/giving-the-model-hands.qmd": ("register_tool", "{#sec-giving-the-model-hands}"),
            "chapters/the-react-loop.qmd": ("run_agent", "{#sec-the-react-loop}"),
            "chapters/workflows-as-folders.qmd": ("init_workspace", "{#sec-workflows-as-folders}"),
            "chapters/loops-with-a-goal.qmd": ("run_ratchet", "{#sec-loops-with-a-goal}"),
            "chapters/the-judge.qmd": ("judge(", "{#sec-the-judge}"),
            "chapters/typed-answers.qmd": ("classify", "{#sec-typed-answers}"),
            "chapters/the-older-ai.qmd": ("classical_ml.ipynb", "{#sec-the-older-ai}"),
            "chapters/train-a-tiny-model.qmd": ("train_tiny_model.ipynb", "{#sec-train-a-tiny-model}"),
            "chapters/teach-it-a-dialect.qmd": ("finetune_adapter_colab.ipynb", "{#sec-teach-it-a-dialect}"),
            "chapters/pictures.qmd": ("describe", "{#sec-pictures}"),
            "chapters/voice.qmd": ("transcribe", "{#sec-voice}"),
            "chapters/conclusion.qmd": ("six drawers", "{#sec-conclusion}"),
            "appendices/just-enough-python.qmd": ("build_payload", "{#sec-just-enough-python .appendix}"),
            "appendices/model-access.qmd": ("HANDS_ON_AI_CACHE", "{#sec-model-access .appendix}"),
            "appendices/project-gallery.qmd": ("Capstones", "{#sec-project-gallery .appendix}"),
            "appendices/going-deeper.qmd": ("Karpathy", "{#sec-going-deeper .appendix}"),
        }
        for name, markers in written.items():
            text = (ROOT / name).read_text(encoding="utf-8")
            with self.subTest(chapter=name):
                self.assertNotIn("## Skeleton", text)
                minimum = 1000 if name.startswith("chapters/") else 500
                self.assertGreater(len(text.split()), minimum)
                if name.startswith("chapters/") and "conclusion" not in name and not any(s in name for s in ("typed-answers", "the-older-ai", "train-a-tiny-model", "teach-it-a-dialect")):
                    self.assertIn("hands-on-ai` 0.6.0", text)
                for marker in markers:
                    self.assertIn(marker, text)

    def test_appendix_labels_use_sec_prefix(self):
        # Quarto only resolves @sec- cross-references; an #app- label
        # renders as a broken citation. Appendices follow the series
        # convention: {#sec-<slug> .appendix}.
        for path in qmd_files():
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=str(path)):
                self.assertNotIn("#app-", text)
                self.assertNotIn("@app-", text)

    def test_package_named_consistently(self):
        for path in qmd_files():
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=str(path)):
                self.assertNotIn("hands_on_ai book", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
