# Metastatic Cascade Analysis

**Computational Modeling of Post-Dissemination Dynamics with an Absorbent Intermediary Compartment**

Independent research by Caitlyn Randels, November 2026.

**Speculative modeling only. No clinical claims.**

## Model Code

- [`metastatic_cascade_model.py`](metastatic_cascade_model.py) — Discrete-time stochastic agent-based implementation including the absorbent intermediary (“sponge”) compartment.

```bash
python metastatic_cascade_model.py
```

Runs a reduced-scale matched sponge-on vs sponge-off comparison across five organotropism configurations.

## Overview

A discrete-time stochastic model of the post-dissemination cascade (shedding, circulation, arrest, establishment, dormancy, reawakening, colonization) was evaluated over 1,364,500 runs with 14 parameter fits against publicly available datasets (primarily MSK-MET, with MetMap 500, metsDB summaries, TCGA via cBioPortal, and SEER aggregates). An optional absorbent compartment parameterized by capacity, permeability, and membrane gating was introduced between circulating/dormant states and final reconciliation.

Key computational findings (internal to the model):
- Inter-patient shedding heterogeneity aligned the dormant fraction with observed targets (37.8% vs 36.1%).
- Sponge activation reduced overt colonization, increased the residual hidden pool, and delayed first overt lesion.
- The compartment imposed an elimination ceiling overcome only by combined membrane gating and establishment-threshold elevation.

## Papers

Successive write-ups of this work:

- v1: *Dissemination, Dormancy and Colonization* (in-silico study)
- v2: refined parameter-sweep paper
- v3: establishment-stage control and onset dependence
- v4: calibrated cascade model (multi-database run, sponge and layers)
- v5: sponge and layer effects at equal precision (v4 run)

The original PDF and Word files could not be stored here as binaries through the connected GitHub interface; they remain on the project computer and were delivered in chat. A short [v4 run summary](v4_Run_Summary.md) is in the repository root, and an index is in [`papers/README.md`](papers/README.md).

## Related Documents

- Operational update sequence protocol
- Earlier establishment-stage and determinants analyses
- Associated PDF manuscripts (on the project computer; see note under Papers)

## Related Work

- [Oroboro](https://github.com/caitlynrandels-del/Oroboro) and [consciousness-mapping](https://github.com/caitlynrandels-del/Oroboro/tree/main/consciousness-mapping)
- [Oroboro Relay](https://github.com/caitlynrandels-del/oroboro-relay)
- [epilepsy-sim](https://github.com/caitlynrandels-del/epilepsy-sim) — the same relational architecture (state reduction, Levy-weighted transitions, sponge, delta reconciliation) adapted to epilepsy and seizure dynamics, including a candidate on-off gate mapping from the 2025 Balabandian et al. mouse psilocin study. Speculative modeling only; no clinical claims.

## Data Availability

Public datasets accessed from original sources. No restricted patient-level data were used.

---

*Independent research. Modeling exercise. Not a clinical protocol or claim of therapeutic efficacy.*
