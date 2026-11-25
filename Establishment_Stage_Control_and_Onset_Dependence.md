# Establishment-Stage Control and Onset Dependence in Metastatic Dissemination, Dormancy and Colonization

**Refined analysis of a 1.21-million-run parameter sweep across five organotropism configurations**

Caitlyn Randels · November 2026

## Abstract

**Background.** Metastatic spread is widely described as inefficient: most disseminated cells are lost, a minority persist in a dormant state, and few form overt lesions. Rare, slow, spatially distributed events like these are hard to dissect experimentally, leaving open which stages of the cascade most strongly shape its outcome.

**Methods.** An agent-based, discrete-time stochastic model of the post-dissemination cascade (shedding, circulation, arrest, establishment, dormancy, reawakening, overt colonization) was run over a 120-month horizon. The study covered 484 conditions (454 unique parameter settings) × 2,500 runs, five organotropism configurations and eight perturbed parameters. Only the stored per-run records (n = 1,210,000) were reanalysed. Condition estimates were recomputed in ten independent seed blocks and recombined, and the recombined values were checked against whole-condition computation. Uncertainty was quantified by cluster bootstrap over seeds (B = 2,000). Switch points were estimated by logistic regression, onset dependence by interpolated half-times, and pairwise interactions as observed/independent-action ratios.

**Results.** All 484 condition estimates were reproduced exactly from the raw records, and between-block heterogeneity in full elimination did not exceed chance (12 of 422 testable conditions at α = 0.05; 21 expected). Under default parameters, 21.7% of runs (bootstrap 95% CI 20.2–23.4%) developed an overt colony, 94.7% of colonies arose in the preferred organ, and a mean of 10.38 dormant cells (10.25–10.51) remained at month 120. The probability of full elimination (no colony and no dormant cell) rose steeply with the establishment threshold: 50% at 0.799 (0.797–0.800) and 90% at 0.854 (0.851–0.857). The 90% point for global organ permissiveness was a scaling of ×0.219 (0.217–0.221). The bone-tropic prostate-like configuration required significantly stricter settings than the lung-tropic configurations (90% threshold 0.872 versus 0.842; permissiveness ×0.176 versus ×0.281–0.303). The effect of a moderate multi-parameter perturbation halved when its onset was delayed to month 57 (55.9–58.7). For single upstream perturbations this happened by month 15–17, whereas dormant-cell clearance stayed effective until month 97. Most pairwise interactions were near independent action (74 of 98 within ±10%), with a few large exceptions: global with preferred-organ permissiveness (ratio 0.21) and establishment threshold with circulating clearance (1.38–1.42).

**Conclusions.** The outcome is controlled mainly at establishment in the distant organ and by organ permissiveness. Suppressing overt colonies and clearing the dormant pool are separable outcomes, and perturbations acting upstream of dormancy lose effect within roughly 1.5 years of delayed onset. The estimates are precise with respect to Monte Carlo error.

---

*(Full methods, results tables, figures descriptions, discussion, and limitations follow the structure of the original analysis. Key quantitative results are summarized above. See the repository for the complete extracted text or request the original PDF.)*

**Data and code availability**  
Per-run records: referenced in original analysis. Reanalysis confirmed exact reproduction of all estimates with quantified uncertainty.
