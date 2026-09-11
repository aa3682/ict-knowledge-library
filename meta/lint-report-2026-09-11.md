# Lint Report: 2026-09-11

**Type:** meta
**Scope:** targeted — `concepts/31-models/ict-2022-model.md` (killzone machine-readability)
**Tooling:** inline structural validator (JSON parse, id/filename match, 10-section + 7-field check, `related[]` and prose-link resolution)
**Status:** closed for the two items in scope; one contradiction left open (see below)

---

## Trigger

A query against the 2022 Model asked for the exact killzone windows. The answer could not be
assembled from the page's JSON block alone — the windows existed only as three bare names in
prose. This pass closes that gap.

---

## Summary

| Check                               | Result |
|-------------------------------------|--------|
| Pages touched                       | 1      |
| JSON parses                         | ok     |
| `id` matches filename               | ok     |
| Top-level JSON keys == 10           | ok     |
| 10 required sections                | ok     |
| 7 required top-matter fields        | ok     |
| `related[]` entries resolve         | ok (11/11) |
| Prose links resolve                 | ok (12/12) |
| Line count (70–150 discipline)      | 115    |
| Contradictions found                | 1 — **open** |

---

## Items closed

**1. JSON carried no time data.** `criteria` held `c1` (`... + killzone + ...`) and `c2`
(`all 7 steps required`). Neither resolved which windows qualify, so any consumer reading the
JSON alone had to join to `killzone-overview` by hand. Added `c3`:

```
{"id": "c3", "expr": "killzone_NY in {london_open == [02:00,05:00], ny_am == [08:00,11:00], london_close == [10:00,12:00]}"}
```

Encoded as a `criteria[].expr` entry rather than a new top-level `killzones` key. **All 287 JSON
blocks in the vault use the same 10 top-level keys with zero exceptions**; an 11th key here would
have forked the schema, which `AGENTS.md` reserves for prior discussion. The precedent for time
values inside `criteria` is `killzone-times-table` c3.

**2. Killzone scope asserted only in Formal Criteria prose.** The three windows were named but
never given times on the page, and were absent from the Formula block. Fixed by:

- Formal Criteria step 2 now carries the NY-time windows inline and names the time set
  (public / 2016+2022), linking `killzone-times-table`.
- The Formula block defines `named_KZ_NY` explicitly and the predicate now reads
  `in_killzone_window(t, named_KZ_NY)` rather than the bare `in_killzone_window`.
- `killzone-times-table` added to `related[]` and to `## Related Concepts`, so the new prose
  dependency is machine-readable rather than prose-only.

**Time-set note.** The 2022 Model is sourced from `ICT-2022-MENTORSHIP-OVERVIEW`, so it takes the
public / 2016+2022 killzone set. The April-2017 mentorship set (London `01:00-05:00`, NY
`07:00-10:00`, per `ICT-2017-DEFINING-DAILY-RANGE`) does **not** apply here. Recorded on the page
so a future edit does not silently swap sets.

---

## Open — contradiction, needs a source decision

`ict-2022-model.md` states the killzone requirement twice, incompatibly:

- **Formal Criteria step 2** names exactly three windows (London Open / NY AM / London Close).
- **Common Mistakes, bullet 3** says the model "includes **any killzone** / DOL combination."

If step 2 is exhaustive, the Asia (`20:00-00:00`) and NY PM (`13:30-16:00`) killzones are excluded
and bullet 3 is wrong. If bullet 3 is right, step 2 is an illustrative list, not a whitelist.

This pass did **not** resolve it. Either reading is a doctrinal claim that needs
`ICT-2022-MENTORSHIP-OVERVIEW` re-read to settle, and a lint pass is the wrong place to decide it.
An earlier draft of this edit asserted the exclusion in three places; that was backed out.

Precedent for the fix once the source is checked: the ⚠ block in `killzone-times-table`, which
records a genuine two-set conflict on the page rather than silently picking a side.

---

## Collateral — stale counts in the hot cache

`meta/hot.md` claimed **252 concept pages / 97 Source IDs**. `tools/lint.py` reports **287 pages /
191 Source IDs**, matching the 2026-08-11 log entry. The hot cache had not been updated since
2026-08-09 and was a month stale on both figures. Corrected, and the source of the numbers
(`tools/lint.py`, dated) is now stated on the page so the next reader can tell fresh from stale.

**Not actioned:** `meta/hot.md` is now 749 words against a ~500-word budget (`CLAUDE.md` →
operations map). It was already over before this pass; the entries added here account for ~150 of
the overage. Trimming it means deciding which of the standing ⚠ notes have aged out, which is a
judgment call for the owner rather than a lint fix.

---

## Also noted, not actioned

`ict-2022-model.md` contains **no MSS step** — the term does not appear on the page, and neither
`ict-2023-model` nor `ict-2024-model` introduces one (`unicorn-model` is the only file in
`31-models/` that references MSS). The canonical chain on the page is
sweep → displacement (FVG forms) → CE retest. This is consistent with `displacement-definition`,
which treats displacement as the filter that validates MSS events rather than a step beside them.
Flagged in case the 2022 source does teach MSS as a discrete confirmation, which would mean the
page understates the sequence. Same disposition as the contradiction above: needs the source.
