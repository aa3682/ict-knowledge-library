# Lint Report: 2026-09-11 (f)

**Type:** meta
**Scope:** new `stub_only` check in `tools/lint.py`; first run
**Tooling:** `tools/lint.py` (extended this run)
**Status:** check added and mutation-tested. **It reports a defect far larger than previously stated — see the correction below.**

> Fifth run this date. Filed new rather than edited — `CLAUDE.md`: reports are one-per-run.

---

## ⚠⚠ Correction to reports (c), (d) and (e)

**Two numbers I reported earlier today were wrong.** Both understated the problem.

| Claim | Where | Actual |
|---|---|---|
| "39 of 190 Source IDs (21 %) are registry stubs" | report (e) | **36 of 191 have no locator at all (19 %)**; 4 more have a date but no video ID |
| "28 stub-only pages outside `31-models/`" | report (e) | **137 of 287 pages vault-wide (48 %)** |

The first was a measurement error: the count included entries whose only "date" was **my own ⚠
annotation** added hours earlier ("verified 2026-09-11"). The grader now reads only the source
description, up to the first ⚠.

The second was worse — a **definitional** error. I counted pages whose sources were all in a
hand-written list of stubs I happened to know about. The list was never the population. Measuring
the actual property — *does any cited source carry a video ID or timestamp?* — gives **137 pages,
nearly five times my estimate.**

This is the hazard the whole day's work has been about, reproduced in my own reporting: a number
that agrees with itself across several surfaces is not thereby verified.

---

## The check

`stub_only` flags a page **every** one of whose Source IDs is a registry stub — an entry in
`SOURCES.md` carrying no locator: no video ID, no timestamp. Nothing on such a page can be checked
against a lecture.

Locator strength, graded on the source description only (up to the first ⚠):

| Grade | Meaning | Count |
|---|---|---:|
| **strong** | 11-char video ID or `[MM:SS]` timestamp — quotable | 150 |
| **weak** | a date, no video ID — findable by hand, not quotable | 4 |
| **none** | bare gloss — **registry stub** | 36 |

Only `none` drives the check; `weak` is recorded for future use.

**Two deliberate design choices:**

- **Umbrella tags are exempt.** `SMC-COMMUNITY-LEXICON` is a tag for community terminology, not a
  claim about one lecture — there is deliberately nothing to locate. Exempting it prevents a
  permanent false positive.
- **Unknown IDs default to stub.** `SOURCES.md` has one range entry ("`ICT-2022-E01` through
  `ICT-2022-E12`") the grader cannot parse. Before hardening, an unparseable ID returned `None`,
  which is not `"none"`, so a page citing only such IDs would have **escaped the check** — a silent
  false negative in a check whose whole purpose is to stop silent passes. Now unknown means stub.

**Output is summarised by directory.** 137 individual lines would bury the other three warnings and
the check would be ignored within a week. `--stub-only` lists the pages.

---

## Mutation-tested

`bread-and-butter-setup` was temporarily reverted to its stub citation:

```
concepts/31-models/bread-and-butter-setup.md  <- ICT-2023-BREAD-AND-BUTTER
```

Caught. Restored — absent from the listing. The check finds the case it was written for.

---

## What the 137 actually are

Spread across **25 of 33 directories**, concentrated in the foundational ones:
`06-fair-value-gaps` ×12, `01-market-structure` ×10, `04-time-cycles` ×9, `02-liquidity` ×8,
`15-sessions` ×8, `31-models` ×8, `07-order-blocks` ×7, `11-silver-bullet` ×7.

**This is not 137 wrong pages.** It is 137 pages whose correctness is currently unknown, which is a
different and more useful statement. Two distinct populations sit inside it:

1. **Recoverable** — the concept has real lectures in `raw/` and the page simply cites a stub
   instead. `bread-and-butter-setup` was exactly this, and it turned out to be describing the wrong
   thing entirely. FVG, order blocks, MSS, killzones, PO3, Asian range and displacement all have
   dedicated corpus lectures. These are the priority: the evidence is already on disk.
2. **Genuinely unverifiable here** — the concept post-dates Aug 2017 (Silver Bullet, macros,
   Quarterly Theory, CRT, NDOG/NWOG, 2025–26 material). Nothing can be done but mark them, as
   `31-models/` was in report (e).

Sorting 137 pages into those two buckets is mechanical — grep the corpus per concept — and is the
obvious next pass.

---

## Checks

| Check | Result |
|---|---|
| `tools/lint.py` | 287 pages, 191 source ids, **0 problems**, 4 warnings |
| Warnings | the 3 known triaged ones, plus the new `stub_only` aggregate |
| Exit status | **0** — stub-only sourcing needs a research programme, not a red build |
| Mutation test | passes: flags the reverted page, silent once restored |
| `--stub-only` listing | 137 lines, one per page, with the stub IDs each cites |

---

## Open

**The 137 are a programme, not a task.** At roughly the rate of today's six-page pass, the
recoverable subset is many sessions of work. It is also the highest-value work in the vault: every
page fixed today was not merely mis-cited but, in three cases, **factually wrong**, and there is no
reason to think that rate falls.

Recommended order: (1) split the 137 by corpus coverage with a grep per concept, (2) work the
recoverable bucket directory by directory, foundations first, (3) mark the rest as report (e) did.

**Do not treat `problems: 0` as "the vault is fine."** It means the structure is sound. Roughly half
the content is unverified, and `stub_only` is now the number that says so.
