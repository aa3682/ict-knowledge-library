# Lint Report: 2026-09-11 (e)

**Type:** meta
**Scope:** content sweep of all 29 `concepts/31-models/` pages for the defect classes found earlier today
**Tooling:** `tools/lint.py`; stub-detection over `SOURCES.md`; anachronism scan; `raw/` corpus search
**Status:** closed — 1 page rewritten from source, 1 leftover fixed, 6 re-graded, 7 registry stubs marked

---

## The folder splits cleanly in two

| Cohort | Pages | Length | Sourcing | Defects found |
|---|---:|---|---|---:|
| Corpus-distilled (Aug 2026 programme) | 18 | 146–305L | video IDs + timestamps | **0** |
| Original-build synthetics | 11 | 81–145L | **registry stub only** | **all of them** |

Every defect in this folder is in the stub-only cohort. The long pages carry quoted, timestamped
citations and survived every check run against them. That is a useful boundary: **the distinguishing
feature is not the year or the topic, it is whether a human ever read a transcript for the page.**

---

## The stub problem is 10× larger than the 2022 ID

`ICT-2022-MENTORSHIP-OVERVIEW` was not special. Applying the same test to the whole registry — an
entry is evidence-bearing if it carries a video ID or a timestamp:

**39 of 190 Source IDs (21 %) are registry stubs.**

In `31-models/`, **11 of 29 pages cite a stub and nothing else**:
`bread-and-butter-setup`, `diamond-pattern`, `ict-2022-model`, `ict-2023-model`, `ict-2024-model`,
`ndog`, `nwog`, `sunday-open-gap`, `unicorn-model`, `venom-model`, `zircon-model`.

---

## `bread-and-butter-setup` — the page did not describe its own subject

The worst finding of the sweep, and it was recoverable: the corpus holds **two dedicated lectures**
whose Source IDs were already registered (`ICT-2017-BREAD-BUTTER-BUY`, `ICT-2017-BREAD-BUTTER-SELL`).
The page cited neither.

| | Page said | Lectures teach |
|---|---|---|
| What it is | "recurring daily delivery sequence" | a **scalping** lesson pair |
| Content | PM → Asia → London → NY AM, 4 steps | **four price engines**, 2 per direction |
| Execution | "standard 2022/2023 model rules" | M5, 15–30 pips, ≤2 h, **1:1**, 0.5–1 % risk |
| Year | 2023 | **May 2017** (lessons 6 and 7) |
| Frequency | "roughly **50–60 % of days**" | **fabricated** — no such figure exists |

The real content: **offset accumulation** and **reaccumulation** for buys, **offset distribution**
and **redistribution** for sells — engine 1 runs price *through* a stop pool, engine 2 returns it to
a PD array, "typically the **optimal trade entry**". **Rewritten from source**, re-dated, re-cited,
moved in TIMELINE.

⚠ One incidental finding with wider reach: this lesson uses **four** killzones — "one in London, one
in New York, one in **London close** and one in **Asia**" — against the day-trading model's two.
**Scalping and day-trading have different session sets**, which no page had recorded. Relevant to
the `ict-2022-model` killzone question still open from report (b).

---

## Anachronism scan

Mechanical: pages dated ≤2017 mentioning vocabulary that post-dates them (Silver Bullet, macro
times, Quarterly Theory, Unicorn, NDOG/NWOG, Venom, Zircon, CRT). **Two hits, both on pages fixed
earlier today:**

- `ny-am-open-range-model` — a ⚠ note *documenting* the removal. Correct, no action.
- `ny-pm-reversal` — **a genuine leftover I missed this morning.** Common Mistakes still said "wait
  for the PM **macro window** 13:50+ for the actual reversal trigger": 2022 vocabulary on 2017
  content, and unsourced. Replaced with ICT's own timing — "typically **2 pm** New York time sees
  the move begin" (`ICT-2017-INDEX-PM-TREND`, 01:59). The scan earned its keep by catching a miss in
  my own work from three hours earlier.

The other 27 pages are clean on this axis.

---

## The unverifiable cohort — marked, not invented

`diamond`, `unicorn`, NDOG/NWOG and `venom` return **zero corpus hits**; the corpus ends Aug 2017
and these concepts post-date it. (The single "unicorn" hit is ICT saying mechanical systems "do not
exist" — unrelated.) Nothing can be checked, and nothing should be fabricated to fill the gap.

Applied instead, consistently:

- **7 registry stubs marked ⚠ in `SOURCES.md`** with the pages that depend on them, and the explicit
  caveat that **absence of corpus evidence is not evidence against the concept** — only that the
  page's specifics are the 2026-05 build's reconstruction rather than quoted teaching.
- **6 pages re-graded `high` → `medium`** — `ict-2023-model`, `ndog`, `nwog`, `sunday-open-gap`,
  `unicorn-model`, `venom-model` — under the rule the owner approved for `ict-2022-model`:
  stub-only sourcing is the taxonomy's "limited public sourcing". Each carries a Citations note
  saying so. `diamond-pattern` and `ict-2024-model` were already `medium`; `zircon-model` is
  `demo-stage` with content explicitly withheld, which was already honest.
- `ICT-2023-BREAD-AND-BUTTER` marked **superseded and uncited** — retained, since IDs are
  append-only, but flagged do-not-cite.

---

## Checks

| Check | Result |
|---|---|
| `tools/lint.py` | 287 pages, 191 source ids, **0 problems**, 3 warnings (the known triaged three) |
| `timeline_placement` caught the re-date within one run | yes — `bread-and-butter-setup` 2017 vs TIMELINE 2023, fixed |
| Header ↔ JSON confidence across 31-models | consistent, 29/29 |
| Line counts | `bread-and-butter-setup` 187L, in line with the other corpus-distilled pages (174–305L) |

---

## Open

**The other 28 stub-only pages outside `31-models/`.** This sweep covered one folder. The registry
test is mechanical and the same 21 % applies vault-wide — `22-quarterly-theory` in particular leans
on `ICT-2023-QUARTERLY-THEORY`, a stub now marked. Recommend the same treatment folder by folder,
prioritising anywhere a real corpus lecture exists (the `bread-and-butter` case), since those are
the recoverable ones.

**A `stub-only` lint check would make this mechanical** — flag any page whose every Source ID lacks
a video ID or timestamp. Cheap to add, and it would have surfaced all 11 of these without a manual
pass. Not built: the stub test lives in this report, not in `tools/lint.py`.
