# London Close Reversal

**Category:** 31-models
**Aliases:** LDN close reversal, London close fade, European unwind reversal
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-DAYTRADE-ESSENTIALS, ICT-2017-DEFINING-DAILY-RANGE
**Tags:** model, london-close, reversal

## Definition

A reversal occurring in the **London close killzone, 10:00–12:00 NY**
(`ICT-2017-DEFINING-DAILY-RANGE`, 04:31). ICT does teach it — but as an **occasional** event inside
a window he otherwise uses for **exits**, not as a primary setup:

> "London close is the time of day where **we look to really bank our positions**. And there are
> **times when**, if the market is in a reversal intraday but it goes down into a logical level of
> support or trades up into a logical level of resistance, **that may be the very moment in time
> that a reversal occurs**. London close is **not always** just simply close existing trades and
> move to the sidelines — many times London close can be incorporated as **an entry point for
> longer-term one-shot-one-kill or swing or position trades**."
> (`ICT-2017-DAYTRADE-ESSENTIALS`, 14:52–15:28)

⚠ **ICT demotes this window by name** in the same breath: "I've taught London close day trading
strategy in the past, I used to do it — **I lost interest in it because it just doesn't give me
enough of a payment**" [14:31–14:47]. Any page that presents the London close reversal as a
front-line day-trade model has inverted his own ranking of it. When he does enter here, the stated
purpose is a **longer-term** position, not an intraday scalp.

⚠ **Two claims previously on this page are unsourced** and have been removed: that the reversal
"**frequently produces the day's HOD or LOD**", and the European-desk-unwind mechanism. Neither
appears in the corpus. The 5-condition checklist below is **library-constructed**, not ICT's — he
gives no enumerated criteria for this setup.

## Formal Criteria

A London Close Reversal requires:

- The London-open KZ delivered a clear directional move (bullish or bearish).
- That move ran into a known HTF level (PDH/PDL/PWH/PWL or FVG).
- During 10:00–12:00 NY (London Close KZ + NY AM overlap), price reverses.
- The reversal sweeps the London-open extreme as part of the move.
- HTF bias is mixed or transitioning — pure-trend HTF rarely sees full LC reversals.

## Formula / Math

```
london_close_reversal:
    london_open_directional_move_present
    AND move_reached_HTF_level
    AND in [10:00, 12:00] NY window
    AND price_reverses_against_morning_direction
    AND london_open_extreme_eventually_swept
```

## Machine-Readable

```json
{
  "id": "london-close-reversal",
  "category": "31-models",
  "aliases": ["LDN-close-reversal", "London-close-fade"],
  "criteria": [
    {"id": "c1", "expr": "London open delivered move"},
    {"id": "c2", "expr": "reversal during 10:00-12:00 NY"},
    {"id": "c3", "expr": "morning-extreme eventually swept"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["london-close","london-close-killzone","ny-am-killzone","silver-bullet-ny-am","ict-2022-model","liquidity-sweep"],
  "sources": ["ICT-2017-DAYTRADE-ESSENTIALS","ICT-2017-DEFINING-DAILY-RANGE"]
}
```

## Visual Pattern

```
   London Close Reversal (bearish reversal of bullish morning):

   03:00–10:00: London open delivered +60 pips up to HOD 1.0925.
   10:30 NY: M5 wicks 1.0928 (sweeps HOD BSL), closes 1.0918.
   11:00 NY: M5 displaces -25 pips, bearish FVG.
   11:30: M5 retests FVG; short entry.
   12:00–13:30: continues bearish into NY lunch.
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — bearish reversal of bullish AM:**
- HTF bias mixed; W bullish but D approaching exhaustion.
- 03:00–10:00 NY: London delivered +60 pips, HOD 1.0925 at PDH BSL.
- 10:30 NY: M5 wicks 1.0928 (HOD/PDH BSL swept), closes 1.0918.
- 11:00 NY: M5 displaces 25 pips down, bearish FVG 1.0908–1.0912.
- 11:25 NY: M5 retests CE 1.0910. Short entry.
- SL 1.0930 (above sweep + buffer); risk 20 pips.
- TP NY AM-low SSL or PDL → reasonable 2-3R.

## Common Mistakes

- **Forcing reversal every day.** Many days continue London-open direction through NY AM; LC Reversal isn't guaranteed.
- **Reversing strong-trend days.** When HTF is unambiguously aligned with London-open direction, fading at LC is fighting the algorithm.
- **Missing the swept-extreme requirement.** A reversal that doesn't first sweep the morning extreme isn't a true LC Reversal — it's just a pullback.

## Related Concepts

- [london-close](../15-sessions/london-close.md), [london-close-killzone](../10-killzones/london-close-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [ict-2022-model](ict-2022-model.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2017-DAYTRADE-ESSENTIALS` (`-cXnnHjy9s0`, Month 08, **April 2017**, lesson 1) — the
  demotion and the conditional reversal, [14:31–15:28], quoted above.
- `ICT-2017-DEFINING-DAILY-RANGE` (`_2nUKLAD9ig`, Month 08, lesson 2) — the window itself: **ICT
  London close killzone 10:00 → 12:00** [04:31], inside a time set ICT frames as settled — "this is
  the **definitive teaching** … if you've seen anything different in the past, **this is the real
  one**" [02:13]. ⚠ That same set puts London open at **01:00–05:00** and New York at
  **07:00–10:00**; see [killzone-times-table](../10-killzones/killzone-times-table.md).
- ⚠ **Re-dated 2022 → 2017 and re-cited on 2026-09-11.** Previously rested solely on
  `ICT-2022-MENTORSHIP-OVERVIEW`, a registry stub.
