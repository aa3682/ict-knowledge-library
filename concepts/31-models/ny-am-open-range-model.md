# NY AM Open Range Model

**Category:** 31-models
**Aliases:** NY AM open range, NY opening range, OR model
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-BOND-OPENING-RANGE, ICT-2017-INDEX-OPENING-RANGE, ICT-2017-BOND-CONSOLIDATION-DAYS
**Tags:** model, ny-am, opening-range

## Definition

The opening range is the **first hour of the cash session**, used as the day's reference range.
ICT teaches it in **June 2017**, and he teaches it **per instrument, with different clocks** — it
is a futures concept, not a generic FX "NY AM" model:

| Instrument | Opening range (NY) | Highest volume |
|---|---|---|
| 30-yr Treasury bond (ZB) | **08:00 – 09:00** | 08:00 – 09:30 |
| E-mini S&P (ES) | **09:30 – 10:30** | 09:30 – 10:00 |

For bonds the window is load-bearing: "the opening range between 8 a.m. and 9 a.m. **tends to
create the bond market high or low of the day**" (`ICT-2017-BOND-OPENING-RANGE`, 03:47). A narrow
opening range is the setup condition — "if you look at an opening range of **12 ticks or less** …
generally, you'll have an **expansion move** of some kind … that volatility squeeze … and then
finally it'll snap and move in a direction that you would have predetermined based on
institutional order flow" (`ICT-2017-BOND-CONSOLIDATION-DAYS`, 09:37–10:07).

⚠ **Three claims previously on this page are not in the corpus** and have been removed: an
`08:00–08:30` "short OR" (no source — the bond range is a **full hour**), the framing of the range
as an FX/"NY AM killzone" model (the lectures are **bonds and index futures**, both opened with a
paper-trade-only disclaimer), and the Silver Bullet targeting (**SB is 2022 vocabulary**; this is
2017 content and the term does not appear in it).

## Formal Criteria

- Time window: 08:00 → 08:30 NY (short OR) or 08:00 → 09:00 NY (long OR).
- OR_high = max(high) over the window.
- OR_low = min(low) over the window.
- Sweep of OR_high or OR_low during 09:00–11:00 NY is the trigger event.
- HTF bias filters which sweep direction is the entry side.

## Formula / Math

```
or_window = [08:00, 08:30] NY    # or [08:00, 09:00] for long OR
or_high = max(high) over or_window
or_low  = min(low)  over or_window

trigger:
    if HTF bullish AND OR_low_swept post-window: long bias on reversal
    if HTF bearish AND OR_high_swept post-window: short bias on reversal
```

## Machine-Readable

```json
{
  "id": "ny-am-open-range-model",
  "category": "31-models",
  "aliases": ["NY-AM-OR", "NY-opening-range", "OR-model"],
  "criteria": [
    {"id": "c1", "expr": "OR window = [08:00, 08:30] or [08:00, 09:00] NY"},
    {"id": "c2", "expr": "OR-bound sweep + HTF-bias-aligned reversal"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["ict-2022-model","silver-bullet-ny-am","ny-am-killzone","ny-am-session","liquidity-sweep","htf-bias-framework"],
  "sources": ["ICT-2017-BOND-OPENING-RANGE","ICT-2017-INDEX-OPENING-RANGE","ICT-2017-BOND-CONSOLIDATION-DAYS"]
}
```

## Visual Pattern

```
   NY AM Open Range Model:

   08:00 ─── 08:30 ─── 09:00 ─── 11:00 NY
   ──── OR window ──────
   |          |
   OR_high (BSL pool)            ← sweep during NY AM SB
   OR_low  (SSL pool)
   |          |
                          ↓
              09:55–10:30: sweep one OR bound, reverse, displace.
              Long if SSL swept on bullish bias; short if BSL swept on bearish.
```

## Timeframes

M5–H1.

## Examples

**Example 1 — bullish NY AM OR sweep:**
- HTF bullish.
- 08:00–08:30: OR formed at 1.0900–1.0915.
- 09:55: M5 wicks 1.0896 (OR_low swept), closes 1.0908.
- 10:08: M5 displacement +18 pips, FVG up at 1.0918–1.0922.
- 10:25: M5 retests CE 1.0920. Long entry.
- SL 1.0894 (sweep low - 2-pip buffer); risk 26 pips.
- Target PDH 1.0950 → 30 pips → 1.15R; or extended -1.5 SD ~1.0975 → 55 pips → 2.1R.

## Common Mistakes

- **OR sweep without HTF context.** Counter-bias OR sweeps frequently fail.
- **Single OR window.** Some traders use 08:00–08:30; others 08:00–09:00; pick one and apply consistently.
- **Trading the OR breakout itself.** The model is "sweep + reverse," not "OR breakout buy/sell." Sweeps are entries; clean breakouts often lack reversal confirmation.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [ny-am-session](../15-sessions/ny-am-session.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).
- [futures-opening-range](../15-sessions/futures-opening-range.md) — the June-2017 futures form of the same construct: **08:00–09:00 NY for the 30-year bond** and **09:30–10:30 NY for the index futures**, each anchored to that market's own volume peak. It is the earliest opening-range teaching located in the corpus, and it also carries the range-size rules (≤12 ticks = squeeze; extended range = expect a return) that this page does not.

## Citations

- `ICT-2017-BOND-OPENING-RANGE` (`CGbSpa_9Z9Y`, Month 10) — "**June 2017** ICT Mentorship, ICT
  Bond Trading Lesson 1, **Basics and Opening Range Concept**" [00:23]; NY session for bonds
  "begins at **8.20 a.m. to 3 p.m.**" [01:11]; highest volume **08:00–09:30** [03:16]; "the opening
  range begins at **8 a.m.** New York time and ends **9 a.m.**" [03:29]; "the opening range between
  8 a.m. and 9 a.m. **tends to create the bond market high or low of the day**" [03:47].
- `ICT-2017-INDEX-OPENING-RANGE` (`ORbtHOUzAIM`, Month 10) — "**June 2017**, ICT mentorship, ICT
  index trading, concepts lesson one, **basics and opening range concept**" [00:22]; ES true day
  **09:30–16:00** [02:51]; highest volume "between **9.30 a.m. and 10 a.m.**" [02:35]; "opening
  range is going to be seen with **9.30 a.m.** … and ends at **10.30 a.m.** … so you have an
  opening range of **one hour**" [03:07–03:15].
- `ICT-2017-BOND-CONSOLIDATION-DAYS` (`RgpxhuVp5Xg`, Month 10) — the narrow-range trigger, "**12 ticks
  or less**" [09:37–10:07].
- ⚠ **Re-dated 2022 → 2017 and re-cited on 2026-09-11.** Previously rested solely on
  `ICT-2022-MENTORSHIP-OVERVIEW`, a registry stub.
