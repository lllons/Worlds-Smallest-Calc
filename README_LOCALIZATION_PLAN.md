# README Localization Plan

This plan records how the five new README translations were added in this session and what reviewers should know going forward.

## Goal

Take the existing English `README.md` and produce five new translations so the project is reachable in more languages, without changing the one-line calculator or any other code:

- French — `README.fr.md`
- German — `README.de.md`
- Italian — `README.it.md`
- Brazilian Portuguese — `README.pt-BR.md`
- Arabic — `README.ar.md`

Each file mirrors the English source's structure: title, intro, quick start with the two unchanged code blocks, available-languages list, and license footer.

## Approach

Five background agents were spawned in parallel, one per language. Each agent received the English source and a fixed set of rules: keep code blocks and paths untranslated, add exactly one new entry to the "Available languages" list, place that entry in alphabetical order by English language name, save the file as UTF-8 with a single trailing blank line, and modify no other file.

After the agents reported back, every new file was read in this session and checked against the English source. Corrections applied manually:

- `README.ar.md` was incomplete — its "Available languages" list still reflected the older six-translation set, with no entry for the new French, German, Italian or Brazilian Portuguese files. The file was rewritten so its list contains the same 11 entries as the other new translations.
- `README.fr.md` listed only eight languages (the original six plus French) and in the wrong order. The list was re-ordered and extended to all 11.
- `README.de.md` had its language list in insertion order rather than alphabetical, and was missing the new Arabic, Italian and Brazilian Portuguese entries. The list was rewritten to all 11 entries in alphabetical order by English language name.
- `README.it.md` had its language list in insertion order, and was missing the new French, German, Brazilian Portuguese and Arabic entries. The list was rewritten to all 11 entries in alphabetical order by English language name.
- `README.pt-BR.md` had its language list in insertion order, and was missing the new French, German, Italian and Arabic entries. The list was rewritten to all 11 entries in alphabetical order by English language name.

## Cross-language consistency

The "Available languages" list across every new README now contains these 11 entries, in this order:

1. Arabic — `README.ar.md`
2. Chinese — `README.zh.md`
3. English — `README.md`
4. French — `README.fr.md`
5. German — `README.de.md`
6. Italian — `README.it.md`
7. Japanese — `README.ja.md`
8. Korean — `README.ko.md`
9. Brazilian Portuguese — `README.pt-BR.md`
10. Russian — `README.ru.md`
11. Spanish — `README.es.md`

Note: the pre-existing six READMEs (English, Chinese, Spanish, Russian, Japanese, Korean) still use the older six-entry list and are due for the same re-ordering pass; that is follow-up work tracked in the roadmap, not part of this plan.

## Things this plan deliberately does NOT do

- It does not change `Calc.py`. The roadmap says any change to the one-line core is a breaking change.
- It does not rewrite the six pre-existing READMEs — that is a separate parity audit per the roadmap's mid-term list.
- It does not add a `pyproject.toml`, GitHub Actions, or `CONTRIBUTING.md`. Those are separate roadmap items.
- It does not add tests. The new files are pure prose.

## How to verify

For each new file:

1. Read it and confirm the title matches the English source.
2. Confirm both fenced code blocks are present and byte-identical to the English source's blocks (the `python -c` line and the `gh repo clone` / `cd` / `python Calc.py` block).
3. Confirm the "Available languages" list contains all 11 entries above, ordered alphabetically by English language name.
4. Confirm the file ends with a single blank line and is UTF-8.
5. Confirm no other file in the repository was modified.

A `git status` after the commit should list exactly six new files: the five READMEs and this plan.
