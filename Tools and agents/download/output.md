# RISK ANALYSIS REPORT
## Proposed AAPL Trading Strategies & Execution Plan — Session of November 4, 2026
**Prepared by: Crew Manager, incorporating risk assessment by Risk Advisor**
**Scope:** All five ranked day-trading strategies, the execution plan, the sizing framework, the model/data inputs, and the process/behavioral wrapper. Account: $50,000. Per-trade risk: $200–$375 (0.40%–0.75%).

---

## 0. HEADLINE ASSESSMENT (Read This First)

The plan is **competently engineered but structurally fragile.** The execution scaffold — no fills before 9:35 ET, 9:45 arming, OCO brackets, 15:50 flat-by, one-to-two-position cap — is genuinely good and **should be kept.** The **strategic core is weaker than it appears**, for five reasons:

1. **The highest-conviction trade (Rank 1, short) has an inferior risk/reward (0.76:1) and is positioned against both the primary structural trend and the morning's actual macro catalyst** — a Democratic sweep that produced a *relief rally* and an ~11% collapse in VIX. Its edge is asserted as "frequency," but no measured frequency is supplied.
2. **The Rank 2 reframed trigger has been changed after the fact from a breakout to a pullback-hold** — a different trade with a different payoff distribution. Ambiguity at 9:45 ET on a session where pre-market price is already *above* the trigger is an operational hazard, not a detail.
3. **Three of five strategies are long AAPL.** The 1.4×-account correlation trap is correctly flagged, but the deeper issue is that the plan's *effective net exposure is path-dependent* — it can become long right before the fade, or short right before the breakout.
4. **Every quantified risk number is a proxy** built on Gaussian returns × 1.20, geometric moving averages, and a possibly-inconsistent data source. Options context (implied ~4.3% earnings move, $330–$360 implied range) is *consistent* with the used volatility — good — but the 33% fat-tail-overlaid annualized figure is an **uncalibrated guess** with no EVT, no realized-kurtosis fit, and no intraday seasonality adjustment.
5. **Ranks 1 and 5 both carry R/R < 1:1.** On an expected-value basis these two should be presumptively skipped or downsized in this specific regime unless the measured win-rate evidence (≥65% and ≥62% respectively, see §3) is produced *before* the bell.

**Net recommendation:** Trade the plan **with the modifications in §9.** Specifically: Rank 1 capped at 0.2% risk with a structural (not 1σ) stop and a hard rule that it is cancelled if VWAP > $339 at 10:00; Rank 2 trigger defined by written rule and restricted to ORB-only on this tape; Rank 3 and Rank 4 mutually exclusive *by rule*; Rank 5 skipped (50% of sessions unattractive) unless the ATR/catalyst screen passes; and a **portfolio-level intraday loss circuit-breaker at $750 (−1.5%)** that does not currently exist.

---

## 1. MARKET / PRICE RISK

### 1.1 The regime is a post-earnings, event-resolved, high-tail tape — not a mean-reverting tape
Nov 4 is defined by **two simultaneous de-risking catalysts resolving in opposite directions for AAPL**:

- **Bearish, idiosyncratic:** FQ4 beat but *forward gross-margin guide of 45–46% vs 47.9% in the September quarter and vs ~46.3% consensus* — a ~1–3pp structural margin cut driven by unprecedented DRAM/NAND costs and Siri AI ramp costs. Management commentary is explicit: "What we're seeing with memory pricing right now is unprecedented" and "looking beyond the December quarter, we see the pricing for memory purchases continuing to increase." **This is a new, open-ended, unquantified cost curve** — the worst kind of input for a mean-reversion model, because it changes the *level* of fair value rather than producing a one-day shock.
- **Bullish, systematic:** Democratic sweep resolves midterm uncertainty; S&P futures up, Nasdaq up, **VIX ~18.5, −2.33 (−11.19%)**, 10Y down 2bp, DXY −0.58%. The market "greeted Democrats' historic midterm victory by rebounding dramatically from overnight losses."

**Risk:** The +2.26% pre-market gap to $339.40 is **mostly beta/gamma relief, not firm-specific demand.** Index-level relief rallies are the *single most common false-positive generator for opening-gap fade strategies* and the *single most common trap for gap-continuation strategies.* Both Rank 1 and Rank 2 are betting on opposite resolutions of the same coin on the same day, and the plan does not specify which wins if the market is simply "up 0.36% and AAPL does nothing."

- **Severity: High. Probability: High (already realized).**
- **Mitigation:** Before 9:45, write down three numbers from the tape: (a) SPY/QQQ % change at 9:35, (b) AAPL pre-market VWAP, (c) AAPL relative-to-NDX strength. **Rule: if NDX > +0.75% at 9:35, Rank 1 requires a *lower* trigger ($333.00 5-min close, not $334.50) and half size.** If NDX < +0.25%, Rank 2's ORB variant is the only long allowed.

### 1.2 "Distribution day" is a single-observation inference and is being overweighted
The Rank 1 thesis rests on "63.16M shares = 1.5× average on a *down* day." This is **one data point, and its directional meaning is contested by the plan's own data-quality note:** WSJ reports range $334.35–$349.19, volume 67.84M. Note that the plan's close of $331.90 is *below* the WSJ low of the range. Both cannot be right. Either:
- (a) 63.16M / $331.90 is right → mild distribution; or
- (b) 67.84M / ~$344.63 close is right → a **1.86% down day on 1.6× volume from a range that touched $349.19** → *much heavier* distribution, and the pre-market +2.26% is a **gap-and-fill setup on a confirmed lower-high**, which is bullish for the fade.

**Risk:** The plan excluded (b) as a "stale artifact" but did not verify it; if (b) is closer to truth, *every* ATR, σ, and VWAP-derived threshold is off by several tenths of a percent. At least three mutually inconsistent sources exist (the canonical $331.90, a $337.18 +1.59% alternate, and a $345.10 print). **The plan should treat close as $331.90 ± $5.28 (1σ of source dispersion)** — i.e., the *level itself is uncertain* by roughly ±1.6%.

- **Severity: High. Probability: Certain (documented inconsistency).**
- **Mitigation:** (1) **Re-verify the Nov 3 OHLCV from three sources (Nasdaq.com, Apple IR, IBKR historical) before 9:00 ET**, and record which is authoritative. (2) Until verified, **shift all Rank 1 thresholds to the *lower* of candidate closes** (trigger $333.50, not $334.50) and all Rank 2 thresholds to the *higher* (entry $336.50–$337.00). (3) **Recompute ATR from the actual 14-day series** rather than asserting $9.17; if the range was actually $334.35–$349.19, true ATR is materially larger and Rank 1's $6.55 stop is even tighter relative to volatility.

### 1.3 Volatility is elevated *and* the plan's stop distances are inconsistent with it
- σ_daily 1.75% → 1σ on $339.40 = **$5.94**. ATR = **$9.17 (2.7% of spot)**. That is a *high-ATR, wide-range* day by construction: the guide is 2.5% and a −4% premarket response has already printed.
- Rank 1 stop distance: $334.40 → $340.95 = **$6.55 = 1.10σ = 0.71 ATR**.
- Rank 2 stop distance: $336.25 → $330.55 = **$5.70 = 0.97σ = 0.62 ATR**.
- Rank 3 stop: $319 → $313.06 = $5.94 = exactly 1σ.
- Rank 4 stop: $352 → $345.56 = $6.44 = 1.08σ.

**A 1.0σ stop on a 1.75%-σ, 2.7%-ATR day is a coin-flip stop.** Approximately **31.7% of the time a single-σ boundary is crossed intraday** under a driftless Gaussian (2 × (1 − Φ(1)) ≈ 0.317) — and under fat tails plus the known opening-range volatility expansion, materially more. On AAPL's *normal* 1.5-ATR range day ($13.75), a $6.55 stop sits inside the noise band.

- **Severity: High. Probability: High.**
- **Mitigation:** (1) **Stops at ≥1.5σ or a structural level, whichever is farther** — for Rank 1 that means **$341.80–$342.00 (R1 top / prior range high)** with a size cut to ~46 shares to hold ~$350 risk. (2) Convert "1σ stop" language into a formula: `stop_distance = max(1.5 × σ_daily × spot, 1.25 × ATR)` → today that is **max($8.91, $11.46) = $11.46**, which is *outside* the tradeable band for a day trade. **Conclusion: this volatility regime makes intraday directional day trades on AAPL structurally unattractive at 0.4–0.75% risk.** That is itself the most important risk finding: **the trade sizing is incompatible with today's volatility.** Either size down to 0.2–0.3% ($100–$150) or require a wider intraday horizon / smaller position.

### 1.4 The 52-week-range position (81.7%) and −5.6% from ATH create asymmetric mechanical supply
At $339.40, AAPL is **$12.33 (3.6%) below the ATH**, with R1 $338–340 already at spot and R2 $346–349 immediately above. The dense resistance cluster ($338–340, $346–349, $351.73) means **the long strategies must chew through three supply shelves in one session** — Rank 2's T1 at $346 requires +2.8% from entry, T2 at $349 requires +3.7%. On a session with a structural margin downgrade outstanding, that is a **low-probability path.**

- **Severity: Medium-High. Probability: Medium.**
- **Mitigation:** Rank 2's T1/T2 should be **re-anchored to R1/R2 only if price has already cleared the prior day's high** ($334.50 or $349.19 — pick one after §1.2 verification). Do not expect $346 on day one of a margin-guide cut; **take 50% at $341.50–$342** and trail the rest.

---

## 2. STRATEGY-SPECIFIC RISK

### 2.1 RANK 1 — FAILED-GAP FADE (short) — **Highest-controversy trade in the book**

**A. The R/R is negative-EV as specified.** Entry $334.40, stop $340.95, T1 $331.90 (+$2.50), T2 $329.92 (+$4.48), runner $325.58 (+$8.82). The stated "R/R per stop ~0.76:1" is the *T1-only* number; the risk unit is $6.55, so T1 = 0.38R, T2 = 0.68R, runner = 1.35R.
- Bucket probabilities for a blended exit (40% T1, 20% T2, 10% runner, 30% stopped): EV = 0.40(0.38) + 0.20(0.68) + 0.10(1.35) − 0.30(1.0) = **+0.123R → positive but thin.**
- If the actual win rate is 55% instead of 70% (far more realistic on a relief-rally tape), EV turns **negative.** **The trade is a coin-flip with a 0.76:1 payoff.** It requires a **≥57% hit rate to T1 alone** just to break even.

**B. The stop at $340.95 is inside the squeeze zone.** It sits at 1.10σ = **0.71 ATR**, *below* the psychologically obvious $341. On a **short into a +2.26% gap on a VIX-collapse day**, the dominant failure mode is an **opening drive to $344–$349**, which stops you at $340.95 *and then* reverses to $331. The stop is precisely on the wrong side of the likely squeeze path.

**C. The short is fighting a structural uptrend and today's macro tape.** AAPL is 81.7% of range, up ~33% over 12 months. Shorting a mega-cap tech leader on a *relief* day with NDX +0.83% and VIX −11% is the **classic "short into strength" asymmetric mistake.** The bearish evidence (DZ Sell $300, KeyBanc overvaluation) is *categorical and already known*; the bullish evidence (BofA buy-the-dip, Bernstein PT raise to $380, +12% revenue, Services ATH) is *current and improving.*

**D. Distribution-day thesis is weaker than asserted.** 1.5× volume on −1.9% is a "mild" supply day; a *true* distribution day on a margin-guide cut would be 2.5–3×. Ironically, the plan's own excluded WSJ data (67.84M) *strengthens* the bearish case — but was excluded.

**E. Event overlap:** Nov 4 is Fed-adjacent (Dec hike odds ~81% per FedWatch), an ADP beat, ISM Services, AMD/SMCI/ANET earnings beats, and election resolution — **five simultaneous risk-on catalysts.** The probability that the gap fades *and stays faded* is lower than the model implies.

**Mitigation (specific):**
- Move the protective stop to **$342.10** (above R1 top + 0.35σ buffer) and **shrink to 46 shares** (risk ~$349, 0.70%) *or* keep 57 shares and accept 0.78% risk — **not both.**
- Add a **conditional squeeze filter: cancel the short if 5-min close > $341.50 before the trigger fires.**
- Take **60% out at T1** (not 40%) so the trade is "paid for" before the runner.
- **Require the trigger to be a *rejection* of R1, not a fade of it:** only go short on a 5-min close **below $333.00 after an attempt at ≥$341** (a lower-high). If price never reaches $341, **no trade** — the correct answer ~50% of the time on this tape.
- Add: **no Rank 1 entry if the 9:35–9:45 range high > $342.00.**

**Verdict: Trade only with (1) $342.10 stop, (2) 46–50 shares, (3) a rejection-of-$341 trigger, (4) 60% out at T1, (5) cancellation if NDX > +0.75% at 9:45 and price > VWAP.**

### 2.2 RANK 2 — GAP-HOLD LONG (reframed ORB / pullback-hold) — **Trigger ambiguity is the top operational risk**

**A. The reframe is a different trade, not a clarification.** The original trigger ("above $336") is *already true* at the open (pre-market $339.40). The reframe to "pullback-hold of $336 or ORB" produces **two distinct entries with different stops and different expected values:**
- Pullback-hold: buy $336.00, stop $330.55, risk $5.45 (≈0.92σ) — a *mean-reversion long at R1 support.*
- ORB: buy $339.50–$340.00 on a 5-min close above the opening-range high, stop $330.55, risk ~$9.45 (**1.59σ**) — a *momentum long with a wide stop and only ~0.7:1 at T1.*

The stated "blended R/R ~2.2:1" is a **weighted average of two trades with materially different skews** and is not actionable at the bell. The "CRITICAL TRAP" flag is correct but the fix is incomplete: the plan still allows a market-buy at the open under the pullback variant if price never pulls back — i.e., you chase $339.40 with a $330.55 stop at 1.6:1, not 2.2:1.

**B. The stop at $330.55 is below the prior close ($331.90) and just above S1.** A long with a stop through the prior day's close on a gap-up day means **max loss $375 on a 63–68-share position with only ~2.2:1 to a 3.7% target** — acceptable *only* if the ORB variant uses tight stops; a market-buy at $339.40 with an $8.85 stop is not.

**C. Correlated double-count with Rank 4.** If AAPL gaps up and keeps going, BOTH Rank 2 ORB and Rank 4 ATH breakout trigger. **Two longs at $337 and $352 = ~$70K** — and more importantly, **the same directional hypothesis expressed twice** (see §4).

**Mitigation (specific, written pre-open):**
1. **Delete the literal "above $336" trigger entirely.**
2. **Define Pullback-Hold as:** limit at $336.00, valid only 9:45–11:00, requiring a 5-min close ≥ $336.00 (green reversal candle) before fill. No fill → cancel at 11:00.
3. **Define ORB as:** 5-min close > opening-range high (first 30 min) AND RVOL ≥ 1.2×; entry stop-limit with a $0.30 buffer; stop at the *lower* of $334.50 (broken support) or 1.25 ATR below entry.
4. **If both conditions could be met, ORB takes priority** and the pullback order is auto-cancelled (prevents double-long).
5. **Cap at 1 position if Rank 4 has already triggered.**

**Verdict: Only trade ORB if price > VWAP and NDX > +0.50%; only trade pullback if price touches $336 and holds. Never both.**

### 2.3 RANK 3 — S2 DIP-BUY BOUNCE (long) — **Requires a 6% intraday drop the tape does not support**

**A. The setup requires a ~6% intraday decline** ($339.40 → $319) — **−3.4σ / −2.2 ATR** from the open, on a day with VIX falling 11% and the election resolved favorably. Under the plan's own σ (1.75%), the probability of touching $319 intraday is roughly **P(min < −3.43σ) ≈ 0.03%** on a Gaussian basis, perhaps **1–3%** with fat tails — *not* a high-probability setup. The plan calls this "best R/R 3.6:1" at S3/S4 but ranks it **#3** — internally inconsistent.

**B. The stop at $313.06 is below S3 ($308–312, the 50-DMA proxy).** A dip-buy at $319 with a stop *inside* the very support zone that justifies the trade will be hit by the intraday wiggle that precedes a bounce. If price reaches $319, the natural next test is **$312.00.**

**C. The staged-limit structure (3 × 21 shares at $320/$319/$318.20) creates a phantom position.** If only the first and second limits fill and price reverses, the average entry is $319.50 with a stop at $313.06 on 42 shares — a *different* R/R than designed.

**Mitigation:**
- Use **one** limit at $319.00 with 50% size (32 shares); add the second 32 only if a 5-min reversal candle prints.
- Set stop at **`min(S3 low − 0.5 ATR, entry − 1.5σ)` = `min($311.00, $313.60) = $311.00`**, sized to hold ~$375 risk (~46 shares at $8.00 risk).
- **Hard rule: no Rank 3 trade if the day is down < 4% by 13:00.**
- **Do NOT invoke the Swing Gate on it** unless price ≥ $315 and profitable at 15:55 (the Swing Gate's S3 zone is *below* Rank 3's entry — avoid double-counting the same idea as two positions).

**Verdict: Low priority today. No trade is a valid outcome.**

### 2.4 RANK 4 — VOLUME-CONFIRMED ATH BREAKOUT (long) — **Volume translation is the weak link**

**A. "55M volume" was translated to "≥1.5× same-time-of-day relative volume."** This is the plan's most defensible analytical fix, but it has three flaws:
- **1.5× RVOL at 10:00 is a very different signal from 55M full-day.** On a typical 42M day, 55M is ~1.3×; 1.5× at 10:00 implies ~63M full-day pace — *arithmetically consistent*, but *only if* the time-of-day volume distribution is normal. **Today's volume is front-loaded by the gap and the election**, so 10:00 cumulative volume will be inflated by the auction by 20–40%. **The 1.5× gate may trigger trivially.**

**B. $352 entry vs $345.56 stop = $6.44 (0.70 ATR).** Again a sub-1σ stop. An ATH breakout that immediately retraces 0.7 ATR is *by definition* a failed breakout. Use the plan's own "false-breakout tell" ($348) as the *stop*, not the tell.

**C. The "runner to $380" is 8% away and is a *fantasy* on a day bounded by a margin guide cut.** The 3-month EV is $328.5 (negative). Taking a runner to $380 on a Nov 4 intraday breakout **contradicts the plan's own long-horizon model.**

**D. ATH breaks fail more often than they hold in high-valuation, late-cycle names** (PE 36.96, PEG ~3.9, $4.84T cap). The ATH was set only 12 days earlier (Oct 23) and the stock is *below* it on a margin cut — **this is a lower-high, not a base breakout.**

**Mitigation:**
- Use **RVOL vs the 20-day same-minute median, not same-time-of-day average, and require 1.8×** (adjusted for front-load). Add a **second condition: cumulative volume at 10:00 ≥ 22M** (~35% of a 63M day).
- Set **stop at $347.90** (below the tell); 38 shares → risk ~$156 (0.31%) — *less* than the plan's $250 and better placed. Add shares on a successful re-test.
- **Cap the runner at $360 (R4)** and use a trailing 1.0 ATR stop above $355. Cancel the $380 runner.
- **Only trade if price > $352 with RVOL ≥ 1.8× AND NDX > +0.50% AND no news in the prior 60 minutes.**

**Verdict: Acceptable only under the tightened volume + no-news gates. ONE re-entry max; two failed attempts = stand down.**

### 2.5 RANK 5 — QUIET-OPEN VWAP RANGE FADE — **Lowest conviction; skip today**

**A. R/R ~0.9:1 with $200 risk is a negative-EV lottery unless win rate > 53%.** On a day with 1.75% σ, a ~4.3% implied earnings band, a *known* margin catalyst, and an election, the "quiet open" premise is **false.** The plan already tags it "skip unless range confirmed" — **make that a hard rule, not a tag.**

**B. A bi-directional scalp at 50 shares with $200 risk = $4/share stop = 0.44σ.** On a 0.71-ATR day, that is a statistical coin flip with negative skew. **This trade should not exist in this volatility regime.**

**Mitigation:**
- **Skip Rank 5 entirely if ATR/spot > 2.5% (today 2.7%) OR a scheduled catalyst exists (today: yes) OR the pre-market gap > 1.5% (today 2.26%).** All three conditions fail → **no trade.**
- If one ever passes, require **2:1 R/R** and 30 shares, not 50.

---

## 3. EXECUTION RISK

### 3.1 The opening auction is where most of the plan's edge is destroyed
The stock gaps +2.26% to $339.40. The **first 30–60 minutes** are dominated by gap-fill algorithms, stop runs, and retail market orders — the plan correctly bans entries before 9:35 and arming before 9:45. **But it does not ban *cancelling* the "rejection" trigger if price has run to $344 by 9:45.** Rank 1 will be the most-tempted trade at exactly the wrong time.

**Mitigation:** Add **"no Rank 1 entry if the 9:35–9:45 range high > $342.00."** Add **"no Rank 2 ORB entry if the opening 5-min candle is > 1.0 ATR."**

### 3.2 Stop order-type risk (the plan is right in principle but incomplete)
- **Rank 1 uses a stop-limit $340.95 with a wide $342.50 limit.** This is the *right* instrument for a short into a squeeze (limits slippage to $1.55). **But a stop-limit that is not filled leaves a naked short into a gap — the worst possible outcome.** The $1.55 buffer ($340.95 → $342.50) is 0.26σ; on a squeeze a $1.55 skip is plausible.
- **Mitigation:** Widen the Rank 1 stop-limit buffer to **$344.00 (a $3.05 buffer, 0.9σ)** — *and* keep a hard mental stop at $342.50 that triggers a **mental market exit** if the limit is skipped. Alternatively, use **stop-market with explicit acknowledgment that slippage may be $0.50–$1.00 (0.15–0.30%) on 46 shares = $23–$46.** For a 0.7% risk trade, a 0.3% slippage event is a **43% risk amplification** — material but tolerable; *not* tolerable on a 68-share Rank 2 long ($68 slippage on $375 risk = 18%).

### 3.3 The "5-min candle close = confirm/veto, not entry instruction" rule is under-specified
If the close prints $334.45 (below the $334.50 trigger), the trade enters at $334.40. **But the plan uses a *stop-limit* with a tight buffer for trend entries — meaning it may not fill at all if the next candle gaps.** **This creates a fill-uncertainty asymmetry: passive/mean-reversion entries get filled (resting limits), trigger entries often don't.** Over time, the realized mix of strategies is *systematically biased toward the passive (fade) trades* — which are the low-R/R trades. **This is a subtle but real selection bias in the plan's execution design.**

**Mitigation:** For trend entries (Rank 2 ORB, Rank 4), use **market-on-confirmation with a 10-second window** — accept $0.03–$0.08 slippage rather than a non-fill. Measure realized fill rate for 5 sessions before adjusting.

### 3.4 "Flat by close" under a gap-down scenario
If AAPL gaps down at 13:00 (e.g., on a DRAM/NAND spot-price headline or Samsung commentary), the plan's **15:15 passive limit exits will *not* be filled in a falling market at all**; the 15:50 flat-by becomes a **forced stop-market at the worst moment of the day** (the closing auction imbalance).

- **Severity: High. Probability: Medium (~30% gap-down >5% per plan).**
- **Mitigation:** **At 14:45, convert all positions to market-on-close-capable orders and flatten by 15:15, not 15:50.** If a position is *losing* and below entry by > 0.5σ at 14:30, **flatten immediately at 14:30**, not 15:50. Add a **"trend-day governor": if AAPL is > 1.5× ATR from the open at 14:00, no passive limits — exit at market.**

---

## 4. SIZING, LEVERAGE, AND CORRELATION RISK

### 4.1 The 1.4×-account trap is real and the plan's guard is too loose
Three longs at ~$70K on $50K = **1.4× gross.** A **5% adverse gap** (the plan itself assigns P ≈ 30% to >5% *over the earnings window*; 5% intraday ≈ 2.8σ) = **−$3,500 = −7% of the account in one move.** That is **10× the per-trade risk budget.** The "one max two" rule cuts gross to ~$47K (0.94×) — still **2.5× the intended single-trade risk.**

**Mitigation (specific):**
1. **Hard portfolio heat cap: aggregate open risk ≤ 1.0% ($500) at all times**, not per-trade. If Rank 1 ($349) and Rank 2 ($375) are both open → **no Rank 4.**
2. **Correlation haircut:** any two *same-direction* positions are sized at 60% each (Rank 2 63 → 38 shares; Rank 4 38 → 23) because their correlation ρ ≈ 0.85–0.95. Two 0.75% trades at ρ = 0.90 have portfolio risk ≈ **√(0.75² + 0.75² + 2×0.75×0.75×0.90) = 1.35%**, not 1.5% — a ~10% "diversification" discount *not worth the added fill complexity.*
3. **Best answer: one position at a time.** The plan's edge is unproven; **concurrent position-taking multiplies variance without multiplying edge.** Constrain to **1 open position, period, on the first session.**

### 4.2 Per-trade risk band is internally inconsistent with volatility
0.40–0.75% = $200–$375 on $50K with a **2.7% ATR and 1.75% σ**. Rank 1's stop is 0.71 ATR → 57 shares × $6.55 = $373. **A 0.75% risk budget with a 0.71-ATR stop means the *position* is tiny in risk but *large in notional* ($19,061, 38% of account).** Fine for AAPL liquidity, but **the risk is dominated by the stop's probabilistic hit rate, not the dollar budget.** The right framing: **"what is the probability the stop is hit before the target?"** On a 0.71-ATR stop with a ~1.35-ATR target, that probability is **> 55% even with a directional edge.**

**Mitigation:** **Reduce per-trade risk to 0.25% ($125) for all intraday directional trades this session** — the volatility alone justifies it. Reserve the 0.5–0.75% band for the S3/S4 swing gate, which has a 3.6:1 R/R and a *structural* stop.

### 4.3 Beta 1.07 understates the event beta
AAPL's historical beta to the S&P is 1.07, but on **midterm-resolution day** AAPL's *event beta* to the relief rally is higher *and* its *idiosyncratic* beta to the margin guide is *negative.* The two are partially offsetting — which is exactly why the stock is +2.26% rather than +4% (index relief) or −4% (margin cut). **The offset is fragile: if the memory-cost narrative dominates the afternoon (DRAM spot, Samsung commentary), the offset flips to additive.**

---

## 5. EVENT / GAP / CATALYST RISK

### 5.1 The plan's own numbers describe a fat left tail that its strategies are not sized for
- **P(1-month drawdown > 10%): ~30%** · **P(> 15%): ~13%** · **P(3-month > 20%): ~14–16%** · **P(3-month > 30%): ~5%.**
- **Next earnings (late Jan 2027): implied one-day move 7–9%; P(gap-down > 5%) ≈ 30%; P(gap-down > 10%) ≈ 12%.**

These are *portfolio-survival* numbers. A single 0.75% trade is fine against them; **a stack of three correlated longs is not.** The swing gate's 0.5% overnight cap is the correct response — but the day-trading sizing does not inherit it.

**Mitigation:** Enforce the **portfolio heat cap (§4.1)** and require **flat-by-close unless the Swing Gate passes** (already in the plan — good). Add an explicit **"earnings blackout: no position of any kind within 5 trading days of late-Jan 2027 earnings"** to the checklist.

### 5.2 Interim gap catalysts are under-weighted
**DRAM/NAND spot prices, Samsung/Micron commentary, holiday sell-through data, and ex-dividend Nov 12 (−$0.27 mechanical)** can all hit intraday. The plan monitors these *daily* but does not give the trader an intraday response rule.

**Mitigation:** Add **"headline kill-switch: on any adverse memory-cost headline intraday, cancel all working orders and flatten longs immediately; do not re-enter the same day without a fresh 5-min base."** Note the ex-div date is irrelevant for Nov 4 but will create a ~$0.27 mechanical open adjustment on Nov 12 — **do not read it as a "gap."**

### 5.3 Macro/election overhang and the new AI-agent 10-K risk
A Democratic sweep raises *regulatory* scrutiny (App Store, AI). The 10-K's new "AI agents acting unintentionally or unpredictably" risk factor is a **latent litigation/regulatory headline source** with no expiry. Either can override any technical setup.

**Mitigation:** Treat these as **regime modifiers, not tradable events** — they raise the required confidence for any long and are a reason to keep the day-trade flat-by-close discipline absolute.

---

## 6. MODEL / DATA RISK

| # | Risk | Severity