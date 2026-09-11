---
type: meta
title: "Hot Cache"
updated: 2026-09-11
---

# Recent Context

## Last Updated

2026-09-11. Source-integrity pass on the 2022-era pages. Prior substantive work: the
video-corpus distillation programme, closed 2026-08-11.

## Key Recent Facts

- **287 concept pages** across 33 domain folders, **191 Source IDs**. `tools/lint.py` is the
  authority on both counts.
- **Two-layer state is intentional.** `raw/` holds 153 transcript packets (59 hrs); only a
  minority is distilled. The remaining ~120 are searchable but uncited — by design.
- ⚠⚠ **Core Content lectures are the 2016–2017 mentorship re-uploaded in 2022.** Each names its
  own lesson number and month in its opening seconds. **Cite as 2016/2017** — the 2022 upload
  date is publication, not authorship. Month → calendar: 1 = Sep 2016, 03 = Nov 2016,
  04 = Dec 2016, 05 = Jan 2017, 06 = Feb 2017, 08 = Apr 2017, 09 = May 2017, 10 = Jun 2017,
  11 = Jul 2017, 12 = Aug 2017.
- ⚠⚠ **36 of 191 Source IDs are registry stubs** — no video ID, no timestamp, nothing to locate
  (`ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2018-BLOCKS` and 34 more). **A stub is never evidence for
  a date.** ⚠⚠ **137 of 287 pages — 48 % — cite nothing but stubs**, so roughly half the vault's
  content cannot be checked against any lecture. `tools/lint.py --stub-only` lists them.
  **`problems: 0` means the structure is sound, not that the content is verified.**
- **Method (non-negotiable):** read the transcript before writing; grep for an existing sibling
  first. ⚠ Never assert an absence without enumerating the population — a 2026-08-05 pass was
  reversed for claiming absences from a 7 % sample.

## Recent Changes

- **2026-09-11.** Nine pages re-cited from the corpus; **every one was mis-dated**, and each
  replacement Source ID **already existed** in `SOURCES.md`. ERL/IRL, `range-expansion`,
  `range-contraction`, `r-multiple` → **2016**; `bread-and-butter-setup`,
  `ny-am-open-range-model`, `london-close-reversal`, `ny-pm-reversal` → **2017**. `31-models`
  swept; 6 unverifiable pages re-graded `medium`, 7 stubs marked in `SOURCES.md`. Full record in
  `log.md`.
- **`tools/lint.py`** gained `years_vs_citations`, `timeline_placement` and `stub_only` — the
  first checks reading a page against *evidence* rather than another copy of itself. Warnings
  only, exit stays 0. Run it before every commit.
- ⚠ **Two figures logged on 2026-09-11 were corrected the same day** (28 stub-only pages →
  **137**). It was a definitional error: the count used a hand-written list of known stubs
  instead of measuring the property. **A number that agrees with itself across several surfaces
  is not thereby verified.**
- Aug 2026: distillation programme closed. `tools/ingest_video.py` automates ingest steps 1–2
  only; steps 3–9 are judgment.

## Active Threads

- **4 lint warnings**: the `stub_only` aggregate, plus 3 triaged as expected — `crt-vs-amd`
  (comparison page), `smt-failure` and `cpi-protocol` (documented open questions). ⚠ No
  acknowledgement mechanism, so those 3 recur every run; recommend an in-page `lint: expected`
  marker before the noise gets ignored.
- ⚠⚠ **NEXT PROGRAMME: the 137 stub-only pages.** Not 137 wrong pages — 137 whose correctness is
  **unknown**. Two populations: **recoverable** (real lectures sit in `raw/` and the page cites a
  stub instead — FVG, order blocks, MSS, killzones, PO3, Asian range, displacement all have
  dedicated lectures) and **genuinely unverifiable** (post-Aug-2017: Silver Bullet, macros,
  Quarterly Theory, CRT, NDOG/NWOG), which can only be marked. Split by corpus coverage first,
  then work the recoverable bucket foundations-first. ⚠ Every page fixed on 2026-09-11 was not
  merely mis-cited — **three were factually wrong**; assume that rate holds.
- `ict-2022-model` has **no MSS step**; chain is sweep → displacement (FVG) → CE retest.
  Unresolved; needs a real 2022 source. ⚠ Killzone tiering differs by model — the **scalping**
  lesson uses four sessions (Asia and London close included), the day-trading model two.
- Layout deviates from the canonical wiki-skill scaffold. Deliberate; see `CLAUDE.md`.
- Open decision: whether to point the `obsidian-vault` MCP server at this repo.
