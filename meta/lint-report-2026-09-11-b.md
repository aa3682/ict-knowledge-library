# Lint Report: 2026-09-11 (b)

**Type:** meta
**Scope:** source check — `ICT-2022-MENTORSHIP-OVERVIEW`; resolution of the contradiction left open by [lint-report-2026-09-11](lint-report-2026-09-11.md)
**Tooling:** `tools/lint.py`; `raw/` corpus grep (153 packets)
**Status:** contradiction resolved; sourcing defect found and recorded; one grading question open

> Second run on the same date. Filed as a new report rather than an edit to the morning's —
> `CLAUDE.md`: lint reports are one-per-run, prior reports are not edited.

---

## The source does not exist

`ICT-2022-MENTORSHIP-OVERVIEW`, the **sole** citation on `ict-2022-model.md`, is a registry stub.
Its whole entry in `SOURCES.md` was:

```
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 mentorship season.
```

No video ID, no date, no quotation, no timestamps, and **no packet in `raw/`**. It sits directly
beside `ICT-2022-E01`–`E12 — episode-level citations (placeholder)`. This is the failure mode the
2026-08-11 entry named for `ICT-2018-BLOCKS`: *"where the build had no real source, it also tended
to invent the mechanics."*

The 120+ `ICT-2022-MENTORSHIP-CORE-CONTENT-*` packets in `raw/` are **not** this ID's content.
They are the 2016–2017 mentorship re-uploaded in 2022, already cited under their own
`ICT-2016-*` / `ICT-2017-*` IDs — the Month 08 packets self-date on tape ("this is April 2017
content for the ICT mentorship", `-cXnnHjy9s0` 00:00).

So the contradiction could not be settled by reading the cited source. It was settled against the
corpus instead.

---

## Resolution: the three-window list stands; "any killzone" was wrong

Common Mistakes claimed the model "includes **any killzone** / DOL combination." No source in the
corpus supports treating the five killzones as interchangeable, and two contradict it directly:

- **London open and New York open are the two primary windows.** The daily routine filters the
  economic calendar to "the **kill zones of London open and New York open**, because those are
  **two dominant high volume times of the day**" (`ICT-2017-DAYTRADE-ROUTINE`, 00:23–02:23).
- **London close is demoted by name.** "I've taught London close day trading strategy in the past,
  I used to do it, **I lost interest in it because it just doesn't give me enough of a payment**";
  it is "the time of day where we look to **really bank our positions**", and an entry only "for
  longer term one shot one kill or swing or position trades"
  (`ICT-2017-DAYTRADE-ESSENTIALS`, 14:31–15:28).
- **Asia and the afternoon are not this model's windows.** Asia open is "primarily 8 p.m. … we're
  looking for **very small little setups**" (16:31–17:17); of the afternoon, "generally by noon
  you're done, you're not really looking at anything past noon" (16:18–16:24).

The three-window list in Formal Criteria therefore survives — but as a **tier, not a flat
whitelist**. Recorded as JSON `c4`, as a Formal Criteria note, and as a new Common Mistakes bullet.
The "any killzone" clause is gone.

---

## Correction to this morning's pass

The earlier run wrote **"public / 2016+2022 set per `killzone-times-table`"** into Formal Criteria
step 2, and hardened `02:00-05:00 / 08:00-11:00 / 10:00-12:00` into JSON `c3`. The times match
`killzone-overview` and are not themselves invented — but **the attribution was an inference, and
it is the contested half of a conflict the vault already documents.**

The mentorship set is London **01:00–05:00**, New York **07:00–10:00**, and in it ICT rejects the
02:00 start by name: *"folks that are using my **free tutorials**, they're waiting for 2 o'clock …
**this is the actual killzone I use**, so the time window begins at **1 a.m.**"*
(`ICT-2017-DEFINING-DAILY-RANGE`, 08:16), framed as settled — *"this is the definitive teaching …
if you've seen anything different in the past, this is the real one"* [02:13].

Asserting the public set for a page whose source is a stub put a guess into machine-readable form —
the opposite of what that pass was for. The attribution is withdrawn; `c5` now records the clock
set as **UNRESOLVED** and names both candidates.

---

## Checks

| Check | Result |
|---|---|
| `tools/lint.py` | 287 pages, 191 source ids, **0 problems** |
| JSON parses / `id` matches / 10 keys | ok |
| 10 sections, 7 top-matter fields | ok |
| `related[]` resolve (12/12), prose links (15/15) | ok |
| `ict-2022-model.md` line count | 145 — inside 70–150, but near the ceiling |

---

## Open — a grading question for the owner

`ict-2022-model.md` carries **`ICT Confidence: high`** on the strength of a citation that cannot be
read. Under the `AGENTS.md` taxonomy, `high` means ICT-original and `medium` means limited public
sourcing; this page has *no* verifiable sourcing.

**Recommendation: downgrade to `medium`** until a real 2022 source is located. Not applied — the
field is page-level metadata that downstream consumers filter on, and re-grading a flagship page is
the owner's call, not a lint fix.

---

## Blast radius of the stub — surveyed

**172 of 287 pages cite `ICT-2022-MENTORSHIP-OVERVIEW`.** Split by whether anything else backs them:

| | Pages |
|---|---:|
| Cite the stub **alongside** at least one real source | 153 |
| Cite the stub as their **only** source | **7** |

The 153 are not urgent — the stub is a decorative extra on a page that stands on real citations.
Stripping it there is cosmetic and can wait for a bulk pass.

**The 7 that rest on it alone are unverifiable as written:**

```
01-market-structure/range-expansion.md
02-liquidity/external-range-liquidity.md
02-liquidity/internal-range-liquidity.md
31-models/ict-2022-model.md          ← handled in this pass
31-models/london-close-reversal.md
31-models/ny-am-open-range-model.md
31-models/ny-pm-reversal.md
```

Three of the six untouched ones are **model pages in `31-models/`**, the same neighbourhood as the
page that produced this report — which is the shape of a build artifact rather than six independent
coincidences. Each needs the same treatment `ict-2022-model` just got: check the claim against the
corpus, re-cite or flag. **Not attempted here** — that is six source checks, not a lint fix, and it
should be its own pass.

`ICT-2022-E01`–`E12`: **zero** pages cite them. The placeholders are inert.
