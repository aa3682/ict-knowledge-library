---
type: meta
title: "Hot Cache"
updated: 2026-09-11
---

# Recent Context

## Last Updated

2026-09-11. Last substantive work: **video-corpus distillation programme - BACKLOG CLOSED**
(2026-08-09/11), plus a targeted lint on the 2022 Model's killzones (2026-09-11, below). The vault sits on top of a
153-packet / 59-hour transcript corpus in `raw/`. All 31 triaged lectures have been read and
resolved: **17 new concept pages, 6 refinements of existing pages, 3 dating corrections**, and
7 correctly rejected as non-concepts. Lint clean.

## Key Recent Facts

- **287 concept pages** across 33 numbered domain folders (+1 directory README in
  `99-glossary/`). **191 Source IDs.** Counts verified by `tools/lint.py`, 2026-09-11;
  this block previously read 252/97 and was a month stale.
- **Two-layer state is intentional.** `raw/` holds 153 packets / 59 hrs / 148 usable;
  only a minority is distilled into concept pages. The rest is searchable but uncited.
- ⚠ **Core Content lectures are the 2016–2017 mentorship re-uploaded in 2022.** Each names
  its own lesson number in its opening seconds. **Cite as 2016/2017**; the 2022 upload date
  is publication, not authorship. Month → calendar map: Month 1 = Sep 2016 … Month 03 =
  Nov 2016, Month 05 = Jan 2017, Month 06 = Feb 2017, Month 08 = Apr 2017, Month 09 =
  May 2017, Month 10 = Jun 2017, Month 11 = Jul 2017.
- **Method (non-negotiable):** read the transcript before writing; grep for an existing
  sibling first. Near-misses already caught this way — `old high` (541 mentions) was an
  alias for four existing concepts, open float ≠ the IPDA 60-day lookback, and "carrying
  charge" means two different things in commodities vs FX.
- ⚠ A 2026-08-05 correction pass was **partly reversed**: it read 3 of the channel's 43 OTE
  videos and asserted absences from that 7 % sample. Do not repeat confident-absence claims
  without enumerating the source population.

## Recent Changes

- **2026-09-11 lint** — `ict-2022-model` killzones were prose-only; the three windows now
  carry NY times in Formal Criteria, the Formula block (`named_KZ_NY`), and JSON `criteria.c3`.
  Encoded as a `criteria[].expr`, **not** a new top-level key: all 287 JSON blocks carry the
  same 10 keys, zero exceptions. Report: [lint-report-2026-09-11](lint-report-2026-09-11.md).
- **Tranche 3** — [ict-day-trading-model](../concepts/31-models/ict-day-trading-model.md),
  [timeframe-selection](../concepts/25-htf-bias/timeframe-selection.md),
  [bond-yield-analysis](../concepts/03-order-flow/bond-yield-analysis.md),
  [explosive-market-selection](../concepts/31-models/explosive-market-selection.md).
- **Two refinements forced by the same reading** — `commitment-of-traders` gained the
  **recentred zero line** (12-month midpoint replaces the printed zero), and `open-interest`
  gained the **10–15 % qualifying gate**, which corrected a standing claim on that page that
  no numeric threshold was taught.
- Tranches 1–2 (same day) — COT, open-float, interest-rate-differentials, carrying-charge;
  then mega-trade, filling-the-numbers, reclaimed-order-block, market-efficiency-paradigm.
- New capability: `tools/ingest_video.py` produces a transcript packet in `raw/`. It
  automates AGENTS.md ingest steps 1–2 only; steps 3–9 are judgment and are printed, not
  performed. Run `--self-check` before trusting it.

## Active Threads

- **Backlog CLOSED:** [distillation-backlog-2026-08-09](distillation-backlog-2026-08-09.md).
  16/16 concepts, 2/2 merges. Nothing pending from it.
- **All three open threads closed 2026-08-10, two by enumeration rather than new material:**
  - *"Eight vs six" projected ranges* — six is the taught set; all five Month-10 index lectures
    checked, the follow-up lesson walks the same six. "Eight" is a repeated misstatement.
  - *30 % vs 34 % breakeven accuracy* — three figures exist in the corpus (30 % recurring,
    33 % once, 34 % once). **30 % is the convention**, modelled arithmetically in
    `ICT-2016-NO-FEAR-LOSING`. `r-multiple` carries the worked table.
  - *`ny-judas-swing` / `judas-swing-failure` at 2018* — **confirmed, not changed.** All 16
    corpus files mentioning "Judas" attach the label to the London/after-midnight protraction
    only. The absence is sourced against the enumerated population.
- **Lint is now `tools/lint.py`**, not a re-typed one-liner. Run it before every commit.
  It gained header↔JSON checks for **sources** and **year** (2026-08-10), then **2026-09-11**
  two checks that read a page against *evidence* rather than against another copy of itself:
  **`years_vs_citations`** (declared year vs the years its own Source IDs encode, stubs excluded)
  and **`timeline_placement`** (AGENTS.md lint step 4, which had never been implemented). Both are
  **warnings — exit stays 0**; a year mismatch needs judgment, not a red build. Currently
  **3 warnings, all triaged as expected** (`crt-vs-amd` is a comparison page; `smt-failure` and
  `cpi-protocol` are documented open questions). ⚠ There is **no acknowledgement mechanism**, so
  those 3 recur every run — recommend an in-page `lint: expected` marker before the noise gets
  ignored.
- ⚠⚠ **`ICT-2022-MENTORSHIP-OVERVIEW` IS A REGISTRY STUB (2026-09-11).** No video ID, date,
  quotation or `raw/` packet — same failure mode as `ICT-2018-BLOCKS`. **172 pages cite it;
  153 also carry a real source.** ✅ **All 7 that rested on it alone are resolved (2026-09-11):
  six were verifiable, all six mis-dated — ERL/IRL and `range-expansion` → 2016,
  `ny-am-open-range-model` / `london-close-reversal` / `ny-pm-reversal` → 2017, every one re-cited
  to a Source ID that already existed.** `ict-2022-model` is now the only stub-only page, and is
  re-graded `medium`. ⚠ **Next: a year-vs-citation sweep of the other 152** — `range-contraction`
  is dated 2022 against a 2016 citation, so a page can cite a real source and still be dated off
  the stub; `tools/lint.py` runs no such check. The
  `ICT-2022-MENTORSHIP-CORE-CONTENT-*` packets are **not** this ID's content; they are the
  2016–2017 mentorship under their own IDs.
- **Killzone contradiction CLOSED** on `ict-2022-model`: three-window list stands, "any
  killzone" was wrong, windows are **tiered** (London open + NY open primary; London close =
  bank positions / longer-term entry only; Asia + post-noon out). Clock set left UNRESOLVED —
  public `02:00` vs mentorship `01:00`, which ICT rejects by name. Open for the owner: the page
  still reads `ICT Confidence: high` on an unreadable citation; **recommend `medium`**.
  Still unactioned: the page has **no MSS step**; chain is sweep → displacement (FVG) → CE.
- ⚠ **Three model pages were factually wrong, not just mis-cited (2026-09-11).** `ny-pm-reversal`
  called the reversal the default — ICT says the PM trend is "**continuation or** reversal", and
  his examples are continuations. `ny-am-open-range-model` had an FX/Silver-Bullet framing on
  **June-2017 futures** content; the real ranges are bonds **08:00–09:00** and ES **09:30–10:30**.
  `london-close-reversal` sold a window ICT demotes by name ("**I lost interest in it**"). Assume
  the same shape elsewhere in `31-models/`.
- Remaining corpus (~120 packets) is searchable but uncited. That two-layer state is intended.
- Layout deviates from the canonical wiki-skill scaffold (kebab-case files, markdown
  relative links, bold-key headers, no `wiki/` wrapper). Deliberate; see `CLAUDE.md`.
- Decision still open: whether to point the `obsidian-vault` MCP server at this repo.
