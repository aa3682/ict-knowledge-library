# External Range Liquidity (ERL)

**Category:** 02-liquidity
**Aliases:** ERL, external liquidity, range-bounding liquidity
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-REINFORCING-LIQUIDITY, ICT-2017-INTRADAY-TOP-DOWN
**Tags:** liquidity, erl, external, dealing-range

## Definition

External Range Liquidity is liquidity that sits **outside** the current dealing range — at or beyond the LTH and LTL that bound it. ERL is the algorithmic full-delivery destination: when an ERL pool is taken, an [external-structure](../01-market-structure/external-structure.md) break occurs and the dealing range is redefined. Mirror concept to [internal-range-liquidity](internal-range-liquidity.md).

## Formal Criteria

- The reference dealing range has bounds LTH_ext (top) and LTL_ext (bottom).
- ERL = any liquidity at or beyond:
  - LTH_ext (above the range top — buy-side ERL).
  - LTL_ext (below the range bottom — sell-side ERL).
- Examples: prior swing highs/lows beyond the range, equal highs/lows beyond the range, prior session/day/week highs/lows beyond the range.
- Taking ERL = external BOS = bias change.

## Formula / Math

```
is_ERL(level) := level >= LTH_ext OR level <= LTL_ext
```

After ERL is taken, a new dealing range begins forming and the old ERL becomes a historical reference.

## Machine-Readable

```json
{
  "id": "external-range-liquidity",
  "category": "02-liquidity",
  "aliases": ["ERL", "external-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "level >= LTH_ext OR level <= LTL_ext"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["internal-range-liquidity","external-structure","draw-on-liquidity","dealing-range","liquidity-pool","bos-bullish","bos-bearish"],
  "sources": ["ICT-2016-REINFORCING-LIQUIDITY","ICT-2017-INTRADAY-TOP-DOWN"]
}
```

## Visual Pattern

```
   ─── BSL ERL: PWH, prior LTHs ───  ← above the range
                                       (full-delivery target)

   LTH_ext ────────────────────────
        (current dealing range)
   LTL_ext ────────────────────────

   ─── SSL ERL: PWL, prior LTLs ───  ← below the range
                                       (full-delivery target)
```

## Timeframes

Most useful H1+. ERL on D / W are major reversal/continuation reference points; ERL on M15 are intra-day full-delivery destinations.

## Examples

**Example 1 — H4 ERL ladder:**
- H4 dealing range: LTH_ext 1.1000, LTL_ext 1.0800.
- Bullish-bias H4 sequence: sweep H4 LTL SSL (1.0795 wick, close 1.0810) → CHoCH → eventual run to LTH ERL at 1.1000 → external BOS → new range starts above 1.1000.
- The 1.1000 BSL ERL is the full-delivery target; intermediate IRL gets taken on the way.

## Common Mistakes

- **Calling internal-side liquidity ERL.** ERL is strictly at or beyond the range bounds — internal swing pivots are IRL, not ERL.
- **Misreading ERL take as a sweep only.** When ERL is taken with a close beyond, that's an external BOS / bias flip, not just a sweep. Sweep + return = still inside range.
- **Ignoring the redefinition.** Once ERL is taken with confirmation, the old LTH/LTL stop being ERL and become historical structure inside the new range.

## Related Concepts

- [internal-range-liquidity](internal-range-liquidity.md) — partial-take counterpart.
- [external-structure](../01-market-structure/external-structure.md) — what taking ERL means structurally.
- [draw-on-liquidity](draw-on-liquidity.md) — ERL is the prime full-delivery DOL target.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the bounded zone whose extremes are ERL.
- [bos-bullish](../01-market-structure/bos-bullish.md) / [bos-bearish](../01-market-structure/bos-bearish.md) — what taking ERL produces.

## Citations

- `ICT-2016-REINFORCING-LIQUIDITY` (`npL3ZXJ5zOU`, Month 04, **December 2016**, module 2) —
  "first on the menu today is going to be **external range liquidity**" [00:49]; "the current
  trading range will have **buy side liquidity above the range high** … **sell side liquidity
  below the range or low**" [00:54–01:02], sought because "you don't want to have any resistance
  in your path of profitability" [01:24–01:28]. Worked through on a sweep: "price sweeps above
  this old high … **that will be a form of external range liquidity because it's outside the
  range**" [03:11–03:19], after which "we now have to **redefine** the high" [05:39].
- ⚠ **The label is relative to the range you define, not absolute.** Same lecture: "**in the
  context from this high to this low it's internal range liquidity, but from this low to this high
  it's external range liquidity**" [05:46–06:13]. A page that treats ERL as a fixed property of a
  price level has lost this.
- `ICT-2017-INTRADAY-TOP-DOWN` (`Oec_0NM_OeY`, Month 12, **August 2017**) — "I'm defining a range,
  either I'm going to operate as internal range liquidity or I'm going to be working off
  **external range liquidity**" [17:12]; ERL is paired with turtle soup as one of his two intraday
  patterns [36:37–36:56].
- ⚠ **Re-dated 2022 → 2016 on 2026-09-11.** Previously cited only the registry stub
  `ICT-2022-MENTORSHIP-OVERVIEW`; `TIMELINE.md` had already flagged the mis-dating.
