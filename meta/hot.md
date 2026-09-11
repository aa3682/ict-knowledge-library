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

- **287 concept pages** across 33 numbered domain folders, **191 Source IDs**. Verified by
  `tools/lint.py`, which is the authority on both counts.
- **Two-layer state is intentional.** `raw/` holds 153 transcript packets (59 hrs); only a
  minority is distilled into pages. The rest is searchable but uncited.
- ⚠⚠ **Core Content lectures are the 2016–2017 mentorship re-uploaded in 2022.** Each names its
  own lesson number and month in its opening seconds. **Cite as 2016/2017** — the 2022 upload
  date is publication, not authorship. Month → calendar: 1 = Sep 2016, 03 = Nov 2016,
  04 = Dec 2016, 05 = Jan 2017, 06 = Feb 2017, 08 = Apr 2017, 09 = May 2017, 10 = Jun 2017,
  11 = Jul 2017, 12 = Aug 2017.
- ⚠⚠ **`ICT-2022-MENTORSHIP-OVERVIEW` is a registry stub** — no video ID, date, quotation or
  `raw/` packet. Same failure mode as `ICT-2018-BLOCKS`. **It is never evidence for a date.**
- **Method (non-negotiable):** read the transcript before writing; grep for an existing sibling
  first. ⚠ Never assert an absence without enumerating the source population — a 2026-08-05 pass
  was reversed for claiming absences from a 7 % sample.

## Recent Changes

- **2026-09-11.** The seven pages resting solely on the stub were checked against the corpus.
  **All six verifiable ones were mis-dated**; every replacement Source ID already existed.
  ERL/IRL, `range-expansion`, `range-contraction`, `r-multiple` → **2016**;
  `ny-am-open-range-model`, `london-close-reversal`, `ny-pm-reversal` → **2017**.
  `ict-2022-model` is now the only stub-only page, re-graded **`medium`**.
- ⚠ **Three of those model pages were factually wrong, not just mis-cited.** `ny-pm-reversal`
  called the reversal the default (ICT: the PM trend is "continuation **or** reversal", and his
  examples are continuations). `ny-am-open-range-model` put an FX/Silver-Bullet framing on
  June-2017 **futures** content — the real ranges are bonds 08:00–09:00, ES 09:30–10:30.
  `london-close-reversal` sold a window ICT demotes by name. **Assume the same shape elsewhere
  in `31-models/`.**
- **`tools/lint.py`** gained `years_vs_citations` and `timeline_placement` — the first checks
  reading a page against *evidence* rather than another copy of itself. Warnings only, exit
  stays 0. Run it before every commit.
- Aug 2026: distillation programme closed (17 new pages, 6 refinements, 3 re-datings).
  `tools/ingest_video.py` automates ingest steps 1–2 only; steps 3–9 are judgment.

## Active Threads

- **3 lint warnings, all triaged as expected** — `crt-vs-amd` (comparison page),
  `smt-failure` and `cpi-protocol` (documented open questions). ⚠ There is **no acknowledgement
  mechanism**, so they recur every run; recommend an in-page `lint: expected` marker before the
  noise gets ignored.
- **145 pages cite the stub alongside a real source.** Cosmetic on its own — but a page can cite
  a real source and still be *dated* off the stub. `years_vs_citations` now catches that class.
- `ict-2022-model` has **no MSS step**; its chain is sweep → displacement (FVG) → CE retest.
  Whether the 2022 teaching includes one is unresolved and needs a real 2022 source.
- Remaining corpus (~120 packets) searchable but uncited. That two-layer state is intended.
- Layout deviates from the canonical wiki-skill scaffold. Deliberate; see `CLAUDE.md`.
- Open decision: whether to point the `obsidian-vault` MCP server at this repo.
