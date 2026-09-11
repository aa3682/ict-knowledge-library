# NY PM Reversal

**Category:** 31-models
**Aliases:** NY PM fade, afternoon reversal, PM trend-fade
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-INDEX-PM-TREND, ICT-2017-DAYTRADE-ESSENTIALS
**Tags:** model, ny-pm, reversal

## Definition

ICT's afternoon teaching is the **PM trend** (his term; also "the afternoon swing") — the
**13:00–16:00 NY** price swing, taught for index futures in **June 2017**. A reversal is one of
its **two** outcomes, not its definition:

> "The PM trend **can be a continuation of the AM trend direction _or_ an intraday reversal going
> into the close**." (`ICT-2017-INDEX-PM-TREND`, 01:41)

⚠ **This page previously asserted the reversal as the default** — "the typical afternoon fade that
retraces the morning move." That is not what the lecture teaches, and its three worked examples are
**continuations**: price trades down into an AM-session order block and rallies away from it into
the high of the day (03:39–04:38). Corrected.

The window and its shape, as taught:

- NY PM session = **13:00 – 16:00** NY (not 13:30). "New York PM session is viewed by way of
  defining the 1 pm to [4] pm hours" (00:41–01:04).
- "The **true day high or low will tend to form between 3 pm and 4 pm** New York time" (01:15).
- "Typically **2 pm** New York time sees the move begin", though it can start as early as 1 pm
  (01:59–02:06). Afternoon measured moves "tend to be **faster** than … the AM session" (01:52).
- **Lunch is noon–13:00**, elastic: "it can actually be as early as **11 a.m.** to as late as
  **2 p.m.**", short after a fast morning, full after a lethargic one (02:41–03:24).

## Formal Criteria

A NY PM Reversal requires:

- NY AM delivered a clear directional move that reached a daily extreme (HOD or LOD).
- Lunch (12:00–13:30 NY) consolidated near the extreme.
- 13:30–14:30 NY: lunch range bound is swept.
- 14:00–16:00 NY: displacement opposite the AM direction; PM SB window often produces the entry.
- NY AM extreme is eventually swept during the reversal.

## Formula / Math

```
ny_pm_reversal:
    ny_am_delivered_directional_move
    AND ny_am_reached_daily_extreme
    AND lunch_consolidation_near_extreme
    AND in [13:30, 16:00] NY
    AND lunch_bound_swept
    AND opposite-direction displacement
    AND eventual sweep of NY AM extreme
```

## Machine-Readable

```json
{
  "id": "ny-pm-reversal",
  "category": "31-models",
  "aliases": ["NY-PM-fade", "afternoon-reversal", "PM-trend-fade"],
  "criteria": [
    {"id": "c1", "expr": "NY AM moved to daily extreme"},
    {"id": "c2", "expr": "PM session reverses, sweeps AM extreme"},
    {"id": "c3", "expr": "PM SB window often the entry"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["ny-pm-session","ny-pm-killzone","silver-bullet-ny-pm","ny-lunch","macro-time-1350-1410","macro-time-1450-1510","liquidity-sweep","ict-2022-model"],
  "sources": ["ICT-2017-INDEX-PM-TREND","ICT-2017-DAYTRADE-ESSENTIALS"]
}
```

## Visual Pattern

```
   NY PM Reversal (bearish reversal of bullish AM):

   08:00-12:00: NY AM rallies to HOD 1.0925.
   12:00-13:30: lunch consolidates 1.0918-1.0930.
   13:55: M5 wicks 1.0931 (lunch BSL swept).
   14:10: M5 displaces -18 pips, bearish FVG.
   14:25-15:30: continues down to PDL 1.0890.
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — PM reversal example:**
- HTF: W bullish but D nearly at upper bound (tired).
- 08:00–11:30: NY AM rallies +50 pips to HOD 1.0925 at PDH BSL.
- 12:00–13:30: lunch range 1.0918–1.0930.
- 13:55 NY: M5 wicks 1.0931 (lunch high + PDH BSL swept), closes 1.0922.
- 14:10 NY (PM macro): M5 displaces -18 pips, bearish FVG 1.0908–1.0912.
- 14:25 NY: M5 retests CE 1.0910. Short entry.
- SL 1.0933 (above sweep + buffer); risk 23 pips.
- TP NY AM range bottom 1.0875 → 35 pips → ~1.5R.

## Common Mistakes

- **Forcing PM reversal on every clean AM.** When HTF is strongly trending, NY PM often continues; reversal is more typical when AM was over-extended.
- **Lunch fade.** Don't trade the lunch consolidation itself; wait for the PM macro window 13:50+ for the actual reversal trigger.

## Related Concepts

- [ny-pm-session](../15-sessions/ny-pm-session.md), [ny-pm-killzone](../10-killzones/ny-pm-killzone.md), [silver-bullet-ny-pm](../11-silver-bullet/silver-bullet-ny-pm.md), [ny-lunch](../15-sessions/ny-lunch.md).
- [macro-time-1350-1410](../04-time-cycles/macro-time-1350-1410.md), [macro-time-1450-1510](../04-time-cycles/macro-time-1450-1510.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [ict-2022-model](ict-2022-model.md).

## Citations

- `ICT-2017-INDEX-PM-TREND` (`qZg_5bac518`, Month 10, **June 2017**, index trading lesson 3) —
  "the PM trend … the afternoon session in North America … typically after noon, New York lunch
  hour" [00:26–00:41]; session defined as 1 pm to 4 pm [00:41–01:04]; true-day extreme **15:00–16:00**
  [01:15]; **continuation _or_ reversal** [01:41]; 2 pm start [01:59]; lunch elasticity
  [02:41–03:24]; three worked continuation examples off AM order blocks [03:39–05:10]. ⚠ Opens
  with a **paper-trade-only** disclaimer — this is commodity/index content, not FX.
- `ICT-2017-DAYTRADE-ESSENTIALS` (`-cXnnHjy9s0`, Month 08, **April 2017**) — the FX day-trading
  model takes the opposite posture on the afternoon: the 14:00 hour and the **15:00 bond close**
  bound the day, and "generally **by noon you're done**, you're not really looking at anything past
  noon" [16:18–16:24]. ⚠ **The two lectures are not in conflict — they are different markets.**
  A page that reads as a general "NY PM model" without saying which is misleading.
- ⚠ **Re-dated 2022 → 2017 and re-cited on 2026-09-11.** Previously rested solely on
  `ICT-2022-MENTORSHIP-OVERVIEW`, a registry stub. ⚠ The Silver-Bullet PM framing was removed:
  SB is 2022 vocabulary and does not appear in this 2017 content.
