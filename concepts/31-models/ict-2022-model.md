# ICT 2022 Model

**Category:** 31-models
**Aliases:** ICT 2022 setup, 2022 mentorship model, the 2022 model
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** model, 2022, mentorship, foundational

## Definition

The ICT 2022 Model is the **flagship multi-step institutional setup framework** taught in ICT's 2022 mentorship cycle — a structured combination of HTF bias, killzone selection, liquidity sweep, displacement-with-FVG, and OTE-style entry. It is the "complete" version of the ICT framework that downstream named models (Silver Bullet, Bread-and-Butter, Unicorn) instantiate at specific scales. The 2022 Model is the closest ICT publishes to a "single canonical setup."

## Formal Criteria

The 2022 Model's setup sequence:

1. **HTF bias** clear (D/W align).
2. **Killzone window** active — London Open `02:00-05:00`, NY AM `08:00-11:00`, or London
   Close `10:00-12:00` (NY time). ⚠ The windows are **tiered, not equal**, and the clock set is
   unsettled — see the sourcing note below.
3. **Liquidity sweep** of a known pool (Asian range, PDH/PDL, session high/low).
4. **Displacement** in the bias direction with an FVG inside or after.
5. **Entry on FVG retest** at CE (per 2025 default).
6. **SL** beyond the swept extreme.
7. **Targets** via SD projections + HTF DOL.

⚠ **The killzone step is the weakest-sourced part of this page.** `ICT-2022-MENTORSHIP-OVERVIEW`
is a registry stub — no video ID, no date, no timestamps, no packet in `raw/` — so neither the
window list nor its clock times can be checked against a lecture. Two things are known from
better-sourced pages:

- **The windows are tiered.** London open and New York open are "the **two dominant high volume
  times of the day**" (`ICT-2017-DAYTRADE-ROUTINE`, 00:23–02:23). London close is demoted by name:
  "I **lost interest in it** because it just doesn't give me enough of a payment"; it is "where we
  look to **really bank our positions**", and an entry only "for longer term one shot one kill or
  swing or position trades" (`ICT-2017-DAYTRADE-ESSENTIALS`, 14:31–15:28). Asia open is for "**very
  small little setups**" (16:31–17:17); past noon "you're done" (16:18–16:24). See
  [ict-day-trading-model](ict-day-trading-model.md), which carries this table in full.
- **The clock set is unresolved.** The times above are the public / 2016+2022 set
  ([killzone-overview](../10-killzones/killzone-overview.md)). The mentorship set differs — London
  **01:00–05:00**, New York **07:00–10:00** — and ICT rejects the 02:00 start by name there:
  "folks that are using my **free tutorials**, they're waiting for 2 o'clock … **this is the actual
  killzone I use**, so the time window begins at **1 a.m.**" (`ICT-2017-DEFINING-DAILY-RANGE`,
  08:16). Which set a 2022-era model takes needs a real 2022 source; see
  [killzone-times-table](../10-killzones/killzone-times-table.md).

The model is **time-and-pattern combined** — both the killzone and the structural sequence must align. The 2022 Mentorship taught it as the ICT framework's single integrated setup.

## Formula / Math

```
named_KZ_NY = {                 # public / 2016+2022 set
  "london_open":  (02:00, 05:00),
  "ny_am":        (08:00, 11:00),
  "london_close": (10:00, 12:00),
}

ict_2022_model :=
    htf_bias_clear
    AND in_killzone_window(t, named_KZ_NY)
    AND liquidity_sweep_just_occurred
    AND displacement_with_FVG_in_bias_direction
    AND entry_at_FVG_CE
    AND SL_beyond_sweep
    AND TP_at_SD_projections_or_DOL
```

## Machine-Readable

```json
{
  "id": "ict-2022-model",
  "category": "31-models",
  "aliases": ["ICT-2022-setup", "2022-mentorship-model"],
  "criteria": [
    {"id": "c1", "expr": "htf_bias + killzone + sweep + displacement + FVG + CE entry"},
    {"id": "c2", "expr": "all 7 steps required"},
    {"id": "c3", "expr": "killzone_NY in {london_open == [02:00,05:00], ny_am == [08:00,11:00], london_close == [10:00,12:00]}"},
    {"id": "c4", "expr": "killzone_tier: {london_open, ny_am} primary > london_close secondary (exit / longer-term entry); asia and post-noon not traded by this model"},
    {"id": "c5", "expr": "UNRESOLVED clock set: public_2016_2022 vs mentorship_2017 ([01:00,05:00] london, [07:00,10:00] ny); sole source is a registry stub"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["ict-2023-model","ict-2024-model","ict-day-trading-model","silver-bullet-overview","silver-bullet-rules","htf-bias-framework","killzone-overview","killzone-times-table","liquidity-sweep","displacement-definition","fair-value-gap","ce-as-primary-entry"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ICT 2022 Model (bullish example, NY AM):

   1. HTF bias bullish (D, W aligned)
   2. NY AM killzone active (08:00-11:00)
   3. M5 wicks below recent swing low (sweep)
   4. M5 displacement candle, bullish FVG forms
   5. M5 retests FVG CE → entry trigger
   6. SL just below sweep low
   7. Target PDH BSL or -1.5 SD projection
```

## Timeframes

M5–H4 entry; D/W for bias.

## Examples

**Example 1 — bullish 2022 Model on NY AM SB:**
- D bias bullish ✓; W bias bullish ✓ (HTF check).
- 10:00 NY (NY AM KZ + SB window) ✓.
- 09:55: M5 wicks 1.0908 (recent low SSL swept) ✓.
- 10:08: M5 displacement +18 pips, FVG 1.0928–1.0932 ✓.
- 10:18: M5 retests CE 1.0930; long entry ✓.
- SL 1.0906 (sweep - 2 pip buffer) ✓.
- TP -1.5 SD = 1.0975 ✓.
- All 7 steps confirmed → high-conviction execution.

## Common Mistakes

- **Skipping a step.** The model is integrated — missing HTF bias OR missing the sweep substantially reduces conviction.
- **Wrong killzone.** Pre-killzone or post-killzone setups don't qualify as 2022 Model proper.
- **Treating ICT 2022 Model as identical to Silver Bullet.** SB is a 60-min subset of the 2022
  Model; the broader model works the full killzone rather than the SB hour.
- **Treating the killzones as interchangeable.** They are tiered, not equal. London open and NY
  open are the primary windows; London close is where positions are banked, and an entry only for
  longer-term trades. See the sourcing note under Formal Criteria.

## Related Concepts

- [ict-2023-model](ict-2023-model.md), [ict-2024-model](ict-2024-model.md) — successor refinements.
- [ict-day-trading-model](ict-day-trading-model.md) — the 2017 mentorship framework this page
  restates, and the sourced authority for the killzone tiering.
- [silver-bullet-overview](../11-silver-bullet/silver-bullet-overview.md), [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md) — narrower 60-min variant.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [killzone-overview](../10-killzones/killzone-overview.md), [killzone-times-table](../10-killzones/killzone-times-table.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`. ⚠ Registry stub — no video ID, date or timestamps. The
  killzone claims above rest on `ICT-2017-DAYTRADE-ESSENTIALS`, `ICT-2017-DAYTRADE-ROUTINE` and
  `ICT-2017-DEFINING-DAILY-RANGE` instead.
