# Lint Report: 2026-09-11 (c)

**Type:** meta
**Scope:** the 6 remaining pages resting solely on `ICT-2022-MENTORSHIP-OVERVIEW`; confidence re-grade on `ict-2022-model`
**Tooling:** `tools/lint.py`; `raw/` corpus search (153 packets); structural + TIMELINE-placement validators
**Status:** closed — 6/6 re-cited and re-dated, 0 stub-only pages remain besides `ict-2022-model` itself

> Third run this date. Filed new rather than edited — `CLAUDE.md`: reports are one-per-run.
> Closes the follow-up opened by [lint-report-2026-09-11-b](lint-report-2026-09-11-b.md).

---

## Headline

**All six were verifiable, and all six were mis-dated.** None of them is 2022 content. Every one had
a real, already-registered Source ID sitting in `SOURCES.md` — no new IDs were needed. The stub was
standing in for sources the vault already had.

| Page | was | now | Real source |
|---|---|---|---|
| `internal-range-liquidity` | 2022 | **2016** | `ICT-2016-REINFORCING-LIQUIDITY`, `ICT-2017-INTRADAY-TOP-DOWN` |
| `external-range-liquidity` | 2022 | **2016** | same |
| `range-expansion` | 2022 | **2016** | `ICT-2016-MARKET-EFFICIENCY-PARADIGM`, `ICT-2017-CONSOLIDATION-TRADING` |
| `ny-am-open-range-model` | 2022 | **2017** | `ICT-2017-BOND-OPENING-RANGE`, `ICT-2017-INDEX-OPENING-RANGE`, `ICT-2017-BOND-CONSOLIDATION-DAYS` |
| `london-close-reversal` | 2022 | **2017** | `ICT-2017-DAYTRADE-ESSENTIALS`, `ICT-2017-DEFINING-DAILY-RANGE` |
| `ny-pm-reversal` | 2022 | **2017** | `ICT-2017-INDEX-PM-TREND`, `ICT-2017-DAYTRADE-ESSENTIALS` |

`TIMELINE.md` had **already predicted two of these**: its 2025 section carried a ⚠ note saying the
ERL/IRL vocabulary is "Dec 2016, not 2022 … invisible to the placement check and **left for a
follow-up**." This pass is that follow-up; the note is now marked closed.

---

## Content defects found, not just citations

Three pages asserted mechanics the corpus contradicts. Re-citing alone would have left the errors in
place with better-looking footnotes.

**`ny-pm-reversal` — the central claim was backwards.** The page said ICT teaches the PM reversal as
"the typical afternoon fade that retraces the morning move." The lecture says the opposite is
equally expected: *"The PM trend **can be a continuation of the AM trend direction _or_ an intraday
reversal going into the close**"* (`ICT-2017-INDEX-PM-TREND`, 01:41) — and its three worked examples
are **continuations**, price trading into an AM order block and rallying away from it. Also
corrected: session is **13:00**–16:00, not 13:30; lunch is **noon–13:00** (elastic 11:00–14:00), not
12:00–13:30; the true-day extreme tends to form **15:00–16:00** (01:15).

**`ny-am-open-range-model` — wrong instrument, wrong clock, anachronistic framing.** ICT's opening
range is **per instrument**: bonds **08:00–09:00**, e-mini S&P **09:30–10:30** — "an opening range
of **one hour**" in both cases. The page's `08:00–08:30` "short OR" appears nowhere. The page framed
it as an FX "NY AM killzone" model; both lectures are **futures**, opened with paper-trade-only
disclaimers. And it targeted the "NY AM **Silver Bullet** hour" — SB is 2022 vocabulary applied to
June-2017 content. Gained a real, quantified trigger the page never had: a narrow opening range,
"**12 ticks or less** … generally you'll have an **expansion move**".

**`london-close-reversal` — inverted ICT's own ranking.** Presented as a front-line day-trade model.
ICT demotes the window by name: *"I've taught London close day trading strategy in the past, I used
to do it — **I lost interest in it because it just doesn't give me enough of a payment**"*
(`ICT-2017-DAYTRADE-ESSENTIALS`, 14:31–14:47). It is where he **banks positions**; a reversal entry
happens "**at times**", and for **longer-term** trades. Removed as unsourced: that the reversal
"frequently produces the day's HOD or LOD", and the European-desk-unwind mechanism. The 5-condition
checklist is marked library-constructed — ICT enumerates no criteria for this setup.

**`external-range-liquidity` / `internal-range-liquidity` — a distinction the pages had flattened.**
The labels are **relative to the range you choose**, not properties of a price level: *"in the
context from this high to this low it's internal range liquidity, **but from this low to this high
it's external range liquidity**"* (`ICT-2016-REINFORCING-LIQUIDITY`, 05:46–06:13). Recorded on both.

**`range-expansion` — a four-phase taxonomy, not a pair.** The page framed expansion against
contraction alone. ICT names four: *"expansion, retracement, reversal, and consolidation"*
(`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, 12:41), alternating within a single day.

---

## Applied on request

`ict-2022-model`: **`ICT Confidence: high` → `medium`**, header and JSON. Its sole citation remains
unreadable; `medium` is the taxonomy's "limited public sourcing". It is now the **only** page in the
vault resting on the stub alone — correctly, since no other source dates or describes it.

---

## Checks

| Check | Result |
|---|---|
| `tools/lint.py` | 287 pages, 191 source ids, **0 problems** |
| 7 touched pages: JSON / id / 10 keys / 10 sections / 7 fields | ok |
| Header `Source IDs` ↔ JSON `sources[]` agree | ok, 7/7 |
| Every cited Source ID resolves in `SOURCES.md` (no orphans) | ok |
| Header `Year Introduced` ↔ JSON `year_introduced` | ok, 7/7 |
| TIMELINE placement matches each page's year | ok, 7/7 |
| Links + `related[]` resolve | ok |
| Line counts | 108–145, all inside 70–150 |
| Pages still stub-only | **1** (`ict-2022-model`, by design) |

One ID was miscopied mid-pass (`ICT-2017-BOND-CONSOLIDATION` for
`ICT-2017-BOND-CONSOLIDATION-DAYS`) and corrected before commit; the orphan-source check above
exists because of it.

---

## Adjacent, not actioned

`range-contraction` was not in scope — it cites `ICT-2016-PO3` alongside the stub, so it is in the
153-page "cosmetic" group. But it carries **`Year Introduced: 2022` against a 2016 citation**, the
same internal mismatch just corrected on its partner page. Flagged in TIMELINE's 2022 section.
**Worth assuming the other 152 contain more of these** — a page can cite a real source and still be
dated off the stub. That is a different sweep from this one: a year-vs-citation consistency check
across the whole vault, which `tools/lint.py` does not currently run.
