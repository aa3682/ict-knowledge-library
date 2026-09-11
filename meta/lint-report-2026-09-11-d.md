# Lint Report: 2026-09-11 (d)

**Type:** meta
**Scope:** new `years_vs_citations` and `timeline_placement` checks in `tools/lint.py`; first run and triage
**Tooling:** `tools/lint.py` (extended this run)
**Status:** closed — checks added, mutation-tested, run; 2 defects found and fixed, 3 warnings triaged as expected

> Fourth run this date. Filed new rather than edited — `CLAUDE.md`: reports are one-per-run.
> Closes the sweep recommended by [lint-report-2026-09-11-c](lint-report-2026-09-11-c.md).

---

## Why the existing checks could not see this

`tools/lint.py` already had `sources_agree`, `years_agree` and `citations_cover_sources`. All three
compare **one surface of a page against another surface of the same page**. They pass cleanly when
every surface carries the *same wrong year* — which is precisely what a stub-sourced page looks
like. Six pages were dated 2022 against 2016/2017 material for months with a green lint.

`years_vs_citations` is the first check that reads the declared year against **evidence**: the years
encoded in the page's own Source IDs.

**Stub and placeholder IDs are excluded from the comparison** (`UNDATED_SOURCES`:
`ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2018-BLOCKS`, `ICT-2022-E01`–`E12`). Including their year is
how the mis-dating happened in the first place — a page citing only the stub would "agree" with
2022 forever.

---

## Result: 5 warnings, 2 real

Far smaller than expected. The 2026-08-10/11 re-dating passes had already caught most of it.

| Page | Warning | Verdict |
|---|---|---|
| `range-contraction` | 2022 vs 2016 citation | **REAL — fixed** |
| `r-multiple` | 2017 vs 2016 citation | **REAL — fixed** |
| `crt-vs-amd` | 2024 vs 2016 citation | false positive by design |
| `smt-failure` | 2018 vs 2017 citation | known, already documented |
| `cpi-protocol` | 2022 predates all citations | known, already documented |

**`range-contraction` → 2016.** The page predicted in report (c). Contraction is the
**consolidation** member of the four-phase set from Month 1, September 2016 — not expansion's binary
partner — and the phases alternate within a single day: "every day starts with **consolidation**,
Asian range" → manipulation → "**another expansion** move down into the New York session" →
"**another consolidation**" (`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, 13:56–14:23). Re-cited to that
source alongside `ICT-2016-PO3`; the stub is dropped.

**`r-multiple` → 2016.** The 3:1 floor is **month two**, October 2016: "identify trade setups that
permit **three reward multiples to one risk or higher**" (`ICT-2016-GROWING-SMALL-ACCOUNTS`,
05:23–05:40), with the accuracy arithmetic in the same month (`ICT-2016-NO-FEAR-LOSING`,
04:42–06:32). The 2017 swing lectures **refine** it — 5:1/10:1, the 34 % break-even — so those IDs
stay and `Year Refined` is unchanged. Stub dropped. This one no prior pass had flagged.

**`crt-vs-amd` — the false-positive class, kept visible.** A disambiguation page is dated by the
newer of the two concepts it separates (Romeo's 2024 CRT) while citing an older source for the other
(`ICT-2016-PO3` for AMD). The rule genuinely does not apply. **Not suppressed** — suppressing
`*-vs-*.md` would hide a real mis-dating on a comparison page. The warning now carries an inline
hint instead, so triage is instant.

**`smt-failure` and `cpi-protocol` — the check rediscovered two known issues independently.** Both
already carry ⚠ notes on the page and in TIMELINE: `smt-failure` is retained "as an open question,
not as a sourced 2018 introduction" after all 153 packets were enumerated for SMT-failure content
and none found; `cpi-protocol` is documented as unverifiable from a corpus that ends Aug 2017. No
action — but the fact that a mechanical check independently surfaced both is the best evidence it
works.

---

## Second check added, beyond what was asked

`timeline_placement`. AGENTS.md → Lint **step 4** requires "every concept file appears under its
`Year Introduced` heading" and **nothing implemented it**. Consequence: every re-dating pass silently
desynced `TIMELINE.md` from the pages it moved. This session broke placement **twice** — the
`range-contraction` and `r-multiple` re-dates above — and only an ad-hoc script caught it.

Also a warning, not a problem: TIMELINE lists many pages inside grouped bullets, and a page can
legitimately be named in a later year's section as a refinement.

Currently **0 placement warnings** across 287 pages.

---

## Mutation-tested

A check that never fires is indistinguishable from a check that is broken. `range-contraction` was
temporarily reverted to `2022` on a scratch copy; both new checks fired:

```
concepts/01-market-structure/range-contraction.md: Year Introduced 2022 is later than its
  earliest citation 2016 (ICT-2016-MARKET-EFFICIENCY-PARADIGM) — dated off a stub?
concepts/01-market-structure/range-contraction.md: Year Introduced 2022 but TIMELINE.md
  lists it under ['2016']
```

Restored; warnings back to 3.

---

## Checks

| Check | Result |
|---|---|
| `tools/lint.py` | 287 pages, 191 source ids, **0 problems**, 3 warnings (all triaged above) |
| Exit status | **0** — warnings deliberately do not fail CI; they need judgment, not a red build |
| TIMELINE placement, vault-wide | **0** misplaced |
| Pages still citing the stub at all | 145 (was 172; the 27-page drop is this session's re-citations) |

---

## Open

Warnings have no acknowledgement mechanism. `smt-failure`, `cpi-protocol` and `crt-vs-amd` will warn
on every future run, and a permanently-noisy check gets ignored. Options: an `# lint: expected` marker
read from the page, or an allowlist file with a reason per entry. **Recommend the in-page marker** —
it keeps the justification next to the claim instead of in a file nobody opens. Not built; it is a
convention change and belongs to the owner.
