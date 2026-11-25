# Metastatic Cascade Analysis

**Establishment-Stage Control and Onset Dependence in Metastatic Dissemination, Dormancy and Colonization**

Refined analysis of a 1.21-million-run parameter sweep across five organotropism configurations.

**Author:** Caitlyn Randels · November 2026  
**Independent Researcher**

## Overview

Metastatic spread is widely described as inefficient: most disseminated cells are lost, a minority persist in a dormant state, and few form overt lesions. This study uses an agent-based, discrete-time stochastic model of the post-dissemination cascade (shedding, circulation, arrest, establishment, dormancy, reawakening, overt colonization) run over a 120-month horizon.

The analysis covers 484 conditions (454 unique parameter settings) × 2,500 runs across five organotropism configurations (prostate-like, ER+ breast-like, lung-like, melanoma-like, colorectal-like) and eight perturbed parameters.

**Key findings:**
- Under default parameters, 21.7% of runs developed an overt colony (95% CI 20.2–23.4%), with 94.7% of colonies in the preferred organ.
- Mean of 10.38 dormant cells remained at month 120.
- The establishment threshold is the dominant lever: full elimination rises steeply, reaching 50% at 0.799 and 90% at 0.854.
- Global organ permissiveness and dormant-cell clearance are also critical, but with different onset dependence.
- Suppressing overt colonies and clearing the dormant pool are separable outcomes.
- Upstream perturbations lose half their effect within ~15–17 months of delayed onset; direct dormant-cell clearance remains effective until ~month 97.

All 1,210,000 per-run records were reanalysed for integrity, with cluster bootstrap uncertainty (B=2,000) and exact reproduction of prior estimates.

## Papers

- **[Establishment-Stage Control and Onset Dependence](Establishment_Stage_Control_and_Onset_Dependence.md)** — Full refined analysis (Caitlyn Randels).
- **[Determinants of Metastatic Dissemination, Dormancy, and Colonization](Determinants_of_Metastatic_Dissemination_Dormancy_and_Colonization.md)** — Polished summary prepared for Caitlyn Connor Randels (Pip Window).

## Related Work

This analysis applies and extends the Oroboro state-reduction and relational simulation framework to metastatic biology. See:
- [Oroboro](https://github.com/caitlynrandels-del/Oroboro) (main framework, including consciousness-mapping and Metastasis_HeatTrace_CaseStudy)
- [Oroboro Relay](https://github.com/caitlynrandels-del/oroboro-relay) (practical application and metastasis-sim)

## Data and Code Availability

Per-run records and reanalysis pipeline referenced in the papers. No external data were used; rates were calibrated to qualitative patterns.

## Limitations

Rates set by hand to qualitative patterns; parameters are abstract; bootstrap captures Monte Carlo error only; no secondary seeding, immune compartments, or spatial structure.

---

*Independent research. Modeling exercise. Not a clinical protocol or claim of therapeutic efficacy.*
