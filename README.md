# Metastatic Cascade Analysis

**Identifiability Limits of Stage-Specific Control in a Calibrated Stochastic Metastatic Cascade Model**

Stage-specific dose-response, interaction and onset-timing analysis of a model calibrated to public cohort data. Independent research by Caitlyn Randels, November 2026.

**Author:** Caitlyn Randels · November 2026  
**Independent Researcher**

## Overview

An agent-based, discrete-time stochastic cascade model (shedding, circulation, arrest, establishment, dormancy, reawakening, colonization; 120 monthly steps) was calibrated to published cohort and experimental data for five tumor types (prostate, ER+ breast, lung, melanoma, colorectal). Targets included 10-year or 5-year cumulative incidence of distant disease, bone-marrow disseminated-tumor-cell prevalence, circulation loss, and organ-involvement shares.

Eight model parameters were perturbed singly and in combination across 484 conditions × 2,500 runs (1,210,000 runs total). The work contrasts a data-calibrated sparse-shedding regime (~2.55 cells per run) with an earlier hand-set parameterization (~240 cells) and a fixed-shedding sensitivity solution, highlighting that cumulative-incidence data constrain overall outcomes but leave stage-specific rates unresolved.

**Key points from the calibrated analysis:**
- Incidence targets reproduced within stated ranges; breast bone-marrow prevalence matched; ever-dormant fraction not reached (structural ceiling ~0.285).
- In the calibrated regime, establishment-checkpoint threshold and upstream parameters (shedding, global organ permissiveness) produced the largest effects on residual-free probability.
- Post-seeding parameters separate overt and dormant outcomes.
- Pairwise interactions centered near independence; benefit of every perturbation decreased with later onset.
- Cumulative-incidence data alone leave stage-specific decomposition unresolved.

## Papers and Documents

- **[Establishment-Stage Control and Onset Dependence](Establishment_Stage_Control_and_Onset_Dependence.md)** — Earlier refined analysis.
- **[Determinants of Metastatic Dissemination, Dormancy, and Colonization](Determinants_of_Metastatic_Dissemination_Dormancy_and_Colonization.md)** — Polished summary.
- **[Study Design Limitations Beyond Data Application](Study_Design_Limitations_Beyond_Data.md)** — Additional subsection covering structural simplifications, uncalibrated constants, experimental design constraints, and scope (added November 2026).
- Full manuscript (original title: “Calibration of a stochastic cascade model…”) + peer-review synthesis + limitations subsection is available as a combined PDF (contact author or see related Oroboro repositories for the latest version).

## Related Work

This analysis applies and extends the Oroboro state-reduction and relational simulation framework to metastatic biology. See:
- [Oroboro](https://github.com/caitlynrandels-del/Oroboro) (main framework)
- [Oroboro Relay](https://github.com/caitlynrandels-del/oroboro-relay) (practical application)

## Data and Code Availability

Calibrated parameter files, provenance tables, reference tables, per-condition summaries, and model source (SHA-256 available) are held by the author and available on request. MSK-MET data from cBioPortal under CC BY-NC-ND 4.0.

## Limitations

See the dedicated [Study Design Limitations Beyond Data Application](Study_Design_Limitations_Beyond_Data.md) for constraints that remain even with perfect data, plus the manuscript’s own Limitations section for target-mapping and identifiability issues.

---

*Independent research. Modeling exercise. Not a clinical protocol or claim of therapeutic efficacy.*
