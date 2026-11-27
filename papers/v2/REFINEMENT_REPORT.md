# What the refinement pass changed vs. confirmed (raw per-run data only)
Input: 1,210,000 per-run rows, /workspace/oroboro-prevention-sim/data/raw_*.csv. Code: pipeline/refine.py, refine_addon.py.

## Mechanisms actually applied
- Levy weighting: recomputed for every run (1/7/2/14/4). 0 mismatches. Levy correlates r = 0.997 with cells shed (0.19 with dormant pool, 0.16 with colonies), so it carries no independent outcome information. Dropped from the paper.
- State reduction + chunking: each condition split into 10 seed blocks, processed independently and recombined by summation. The relay stub (`delta = Math.random()*0.1`, `coherent = delta < 0.2`) was replaced in the Python port with the real delta |recombined − whole|. Result: 0.0 for every condition. The repo's JS file was not modified.
- Delta reconciliation vs the earlier summaries: all 484 conditions match exactly (max diff 0).
- Mesh consensus: per run, 0 census/ledger/colony-record failures. Across blocks, full elimination exceeded the χ² 5% critical value in 12/422 conditions (21 expected) = no hidden heterogeneity. Any-colony exceeded it in 29/289 (14.4 expected), all at rare-event conditions where χ² is unreliable.
- Oasis salience gate (real oasis_core.salience_score; features = effect size, block consensus, precision, default tension 0.5): 416 COMMIT, 68 BUFFER, 0 RECYCLE. Buffered = default/small-effect conditions. The gate adds nothing beyond those statistics.

## Confirmed (unchanged)
Every point estimate in the previous report (baseline 21.7%, 10.38 dormant, 94.7% preferred organ; all dose-response, combination and timing numbers).

## Added or changed
1. 484 conditions = 454 unique settings. 30 conditions (75,000 runs) are exact replays, so 1,135,000 distinct runs.
2. Bootstrap CIs: baseline colonization 20.2–23.4% (Wilson was 20.1–23.4); dormant 10.25–10.51.
3. Switch points with CIs replace "first tested value":
   - Threshold: x50 0.799 (0.797–0.800), x90 0.854 (0.851–0.857). Old report: "transition between 0.70 and 0.85", target first met at 0.875.
   - Organ permissiveness: x50 ×0.297, x90 ×0.219 (old: tips between ×0.45 and ×0.2).
   - Dormant clearance: x50 ×25.8, x90 ×78.9 (75.0–83.0) (old: ×100 first meets target).
   - Shedding: x50 ×0.089, x90 ×0.025. The fit is imperfect; interpolated values are 0.107 / 0.018.
4. Configuration differences: prostate-like needs significantly stricter settings (threshold x90 0.872 vs 0.842 lung; organ ×0.176 vs ×0.303 melanoma; non-overlapping CIs). For shedding and dormant clearance, configuration CIs overlap, so those differences are NOT resolved (the old report implied prostate is hardest across the board).
5. Timing half-times (new): bundle 57.3 mo (55.9–58.7); threshold 0.80 15.6; organ ×0.4 17.3; shedding ×0.25 15.0; dormant clearance ×20 97.3.
6. Interactions: the old report said "about multiplicative, median 1.0". Median 0.997 and 74/98 pairs within ±10%, BUT the CI excludes 1 for 82/98 (47 below, 35 above): small deviations are real, mostly modest. Large ones confirmed with CIs: organ×preferred 0.21 (0.19–0.23); threshold 0.85 + organ ×0.4 0.37 (0.23–0.52); threshold 0.85 + circulating clearance 1.38–1.42 (1.22–1.65).
