# README Localization Plan

This plan records how the five new README translations were added in this session and what reviewers should know going forward.

## Goal

Take the existing English `README.md` and produce five new translations so the project is reachable in more languages, without changing the one-line calculator or any other code:

- French — `README.fr.md`
- German — `README.de.md`
- Brazilian Portuguese — `README.pt-BR.md`
- Italian — `README.it.md`
- Arabic — `README.ar.md`

Each file mirrors the English source's structure: title, intro, quick start with the two unchanged code blocks, available-languages list, and license footer.

## Approach

Five background agents were spawned in parallel, one per language. Each agent received the English source and a fixed set of rules: keep code blocks and paths untranslated, add exactly one new entry to the "Available languages" list, place that entry in alphabetical order by English language name, save the file as UTF-8 with a single trailing blank line, and modify no other file.

After the agents reported back, every new file was read in this session and checked against the English source. Two corrections were applied manually:

- `README.ar.md` still contained one English sentence ("Then type any expression and press Enter to evaluate it.") and two untranslated section headings ("Quick start", "Available languages"). All three were translated to Arabic.
- `README.it.md` kept the English heading "Quick start" and was changed to "Avvio rapido".
- `README.de.md` had its language list in insertion order rather than alphabetical, and was re-ordered by English language name.

## Cross-language consistency

The "Available languages" list across every README should now contain these seven entries, in this order:

1. Arabic — `README.ar.md`
2. Chinese — `README.zh.md`
3. English — `README.md`
4. French — `README.fr.md`
5. German — `README.de.md`
6. Italian — `README.it.md`
7. Japanese — `README.ja.md`
8. Korean — `README.ko.md`
9. Russian — `README.ru.md`
10. Spanish — `README.es.md`

(Note: the agent brief asked the new translation's own entry to be inserted alphabetically, so each README's list points to ten languages, including itself. The English source and the pre-existing six translations are also due for the same re-ordering pass; that is follow-up work, not part of this plan.)

## Things this plan deliberately does NOT do

- It does not change `Calc.py`. The roadmap says any change to the one-line core is a breaking change.
- It does not rewrite the existing six READMEs (English, Chinese, Spanish, Russian, Japanese, Korean) — that is a separate parity audit per the roadmap's mid-term list.
- It does not add a `pyproject.toml`, GitHub Actions, or `CONTRIBUTING.md`. Those are separate roadmap items.
- It does not add tests. The new files are pure prose.

## How to verify

For each new file:

1. Read it and confirm the title matches the English source.
2. Confirm both fenced code blocks are present and byte-identical to the English source's blocks (the `python -c` line and the `gh repo clone` / `cd` / `python Calc.py` block).
3. Confirm the "Available languages" list contains the seven pre-existing entries plus the new translation's own entry, ordered alphabetically by English language name.
4. Confirm the file ends with a single blank line and is UTF-8.
5. Confirm no other file in the repository was modified.

A quick `git status` after the commit should list exactly six new files: the five READMEs and this plan.
