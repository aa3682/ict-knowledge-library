# Bread-and-Butter Setup

**Category:** 31-models
**Aliases:** B&B setup, bread and butter, B&B model, amplified scalping
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-BREAD-BUTTER-BUY, ICT-2017-BREAD-BUTTER-SELL
**Tags:** model, bread-and-butter, scalping, price-engine, killzones

## Definition

Bread and Butter is ICT's **scalping** pair of lessons — lessons 6 and 7 of **May 2017**, "ICT
amplified day trading and scalping" — not a daily-delivery narrative. Its subject is "**consistent
small price movements** that can be harvested, **not every day but just about every day**"
(`ICT-2017-BREAD-BUTTER-BUY`, 00:33).

Its content is **two price-engine models per direction**, distinguished by what the algorithm is
doing to existing positions:

| Direction | Engine 1 | Engine 2 |
|---|---|---|
| Buy programs | **offset accumulation** | **reaccumulation** |
| Sell programs | **offset distribution** | **redistribution** |

⚠ **This page previously described something else entirely** — a "PM → Asia → London → NY AM
daily delivery sequence" executed "with standard 2022/2023 model rules", dated 2023, including a
fabricated "roughly 50–60 % of days follow B&B cleanly". None of that is in either lecture.
Rewritten from source 2026-09-11.

## Formal Criteria

**The four engines.** Engine 1 runs price *through* a stop pool; engine 2 returns price to a PD
array without one.

- **Offset accumulation** (buy) — "reprice the market **below an old low** to promote sell stops
  … this in essence **engineers sellers at a deep discount**" (BUY 01:49–02:27). Purpose: offset
  current long holders or induce sellers at discount.
- **Reaccumulation** (buy) — "reprice the market lower **to a fair value price array** to provide
  smart money discount pricing for long entries … many times unfolds **after a recent sell stop
  raid**" (BUY 02:49). The entry is "typically **the optimal trade entry**" (06:10).
- **Offset distribution** (sell) — the mirror: "**accumulate buy side liquidity** for repricing
  **above an old high**; buy stops will be triggered, inducing counterparty buyers to pair short
  entries with" (`ICT-2017-BREAD-BUTTER-SELL`, 00:41–00:53).
- **Redistribution** (sell) — "reaccumulate fair value in retracements higher **at premium
  arrays**; weak short holders will be squeezed in the retracement higher" (SELL 00:58–01:11).

Both directions carry the same two conditions: the model "is seen frequently **while higher
timeframe institutional order flow is suggesting**" the trade direction, and "typically … models
**unfold quickly** and you must learn to **anticipate** them" (BUY 02:34–02:39, 03:42).

**Stated objectives** (BUY 03:49–05:40) — ICT gives these as numbers, not adjectives:

| | |
|---|---|
| Duration | **1–2 hours or less**; two hours is the maximum |
| Target | **15–30 pips** per trade |
| Chart | **M5** |
| Frequency | **2–3 setups per day**; about **one per session** |
| Risk:reward | **1:1** — "if you're thinking scalping, think one to one and that's about all you're going to get" |
| Risk per trade | **0.5–1 %**; 1 % "maybe a little high" until proficient |

**Time constraint.** "**All scalping should be done during ICT kill zones**, since the duration and
style of trading is so short term in nature we need the most volatile times of the trading day"
(BUY 06:22). ⚠ Unlike the day-trading model, this one uses **four** sessions, Asia and London close
included: "one in London, one in New York, one in **London close** and one in **Asia**" — across a
basket of four or five pairs, not one pair every session (04:33–05:05). Limit-order fills can land
outside a killzone, typically London lunch (05:00–07:00) or after 10:00; ICT's remedy is "**do all
your scalping with market orders** … use limit orders for your exits" (06:22–06:52).

## Formula / Math

```
buy_programs  := offset_accumulation | reaccumulation
sell_programs := offset_distribution | redistribution

offset_accumulation :=                    # engine 1: through the stops
    reprice_below(old_low)
    AND sell_stops_triggered
    AND seek(short_term_premium_array)    # to offset

reaccumulation :=                         # engine 2: to the array
    reprice_lower_into(fair_value_discount_array)
    AND typically_after(sell_stop_raid)
    AND entry == OTE

gate := HTF_institutional_order_flow_agrees AND in_ICT_killzone
objectives := {duration: <=2h, target: 15..30 pips, chart: M5, RR: 1.0, risk: 0.5..1.0%}
```

## Machine-Readable

```json
{
  "id": "bread-and-butter-setup",
  "category": "31-models",
  "aliases": ["B&B-setup", "bread-and-butter", "amplified-scalping"],
  "criteria": [
    {"id": "c1", "expr": "buy: offset_accumulation (below old low, stop run) OR reaccumulation (into discount array, entry == OTE)"},
    {"id": "c2", "expr": "sell: offset_distribution (above old high, stop run) OR redistribution (into premium array)"},
    {"id": "c3", "expr": "HTF institutional order flow must agree with the direction"},
    {"id": "c4", "expr": "in_killzone == true; scalps occur in london, ny, london_close and asia"},
    {"id": "c5", "expr": "objectives: duration <= 2h, 15..30 pips, M5, RR == 1:1, risk 0.5..1.0%, 2-3 setups/day"}
  ],
  "timeframes": ["M5"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["ict-day-trading-model","one-shot-one-kill","liquidity-sweep","ote-overview","premium-array","discount-array","killzone-overview","institutional-order-flow","open-float-liquidity-pool"],
  "sources": ["ICT-2017-BREAD-BUTTER-BUY","ICT-2017-BREAD-BUTTER-SELL"]
}
```

## Visual Pattern

```
   Buy programs — the two engines (M5, inside a killzone):

   ENGINE 1 — offset accumulation          ENGINE 2 — reaccumulation
   (through the stops)                     (to the array)

        ┌── premium array (offset)              ┌── premium array (offset)
        │                                       │
    ────┼───────                            ────┼───────
   old low ····│                             recent raid ····│
        sell stops ▼ swept                        │  retrace into
        └── reversal up                           └── discount FVG / OB
                                                     entry = OTE

   Sell programs mirror exactly:
     offset distribution  = above an old high, buy stops swept
     redistribution       = retrace up into a premium array
```

## Timeframes

M5 for execution — ICT names no other chart for this lesson. Direction comes from higher-timeframe
institutional order flow, read separately.

## Examples

**Example 1 — offset accumulation (from the lecture's own framing):** HTF order flow bullish. Price
reprices **below an old intraday low**, triggering the sell stops resting there — including breakout
sellers in the open float below that low. Those fills are the counterparty for smart-money longs.
Price then seeks a **short-term premium array** to offset. Scalp is taken on the reversal, target
15–30 pips, out inside two hours.

**Example 2 — redistribution (sell mirror):** HTF order flow bearish. Price retraces **higher into a
premium array**; weak short holders are squeezed out in the retracement, providing buy-side
liquidity. Price expands lower to a short-term discount array to offset. Entry at the premium array,
1:1 target.

## Common Mistakes

- **Reading B&B as a daily sequence.** It is a **scalping** lesson about four price engines, not a
  PM → Asia → London → NY narrative. That framing was on this page until 2026-09-11 and had no
  source.
- **Expecting more than 1:1.** ICT states the ceiling plainly — "that's about all you're going to
  get" (BUY 05:27). A page or trader promising better has left the lecture.
- **Confusing the two engines.** Offset runs price *through* a stop pool; reaccumulation returns it
  to a PD array, often *after* such a raid. Different triggers, different entries.
- **Taking one per session per pair.** The one-per-session frequency is across a **basket of four
  or five pairs** — "not all of them, just one of them" (05:05).
- **Scalping outside a killzone.** ICT's stated fix for stray limit fills in London lunch or after
  10:00 is to scalp with **market orders** and reserve limits for exits.

## Related Concepts

- [ict-day-trading-model](ict-day-trading-model.md) — the same month's larger framework; B&B is its
  scalping tier and, unlike it, trades all four sessions.
- [one-shot-one-kill](one-shot-one-kill.md) — the opposite end of the frequency/duration scale.
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [killzone-overview](../10-killzones/killzone-overview.md), [institutional-order-flow](../03-order-flow/institutional-order-flow.md), [open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md).

## Citations

- `ICT-2017-BREAD-BUTTER-BUY` (`OVfn-gDk2dE`, Month 09, **May 2017**, lesson 6) — "lesson six of the
  May 2017 ICT mentorship, ICT amplified day trading [and] scalping … **bread and butter buy
  setups**" [00:00–00:21]; "consistent small price movements that can be harvested, **not every day
  but just about every day**" [00:33]; the two buy engines [00:40–03:42]; objectives — duration,
  15–30 pips, M5, frequency, 1:1, 0.5–1 % [03:49–05:40]; "**all scalping should be done during ICT
  kill zones**" and the four-session/basket framing [04:33–06:52]; reaccumulation entry "is
  typically the **optimal trade entry**" [06:10].
- `ICT-2017-BREAD-BUTTER-SELL` (`-oMtfDvc18Y`, Month 09, **May 2017**, lesson 7) — "lesson 7 of the
  May 2017 ICT mentorship … **bread and butter sell setups**" [00:00–00:12]; **offset distribution**
  and **redistribution** defined as the mirror pair [00:32–01:11, 01:47, 02:45].
- ⚠ **Re-dated 2023 → 2017 and rewritten from source on 2026-09-11.** The page previously rested on
  `ICT-2023-BREAD-AND-BUTTER`, a registry stub, and its content matched neither lecture.
