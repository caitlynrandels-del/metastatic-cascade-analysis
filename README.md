# Metastatic Cascade Analysis

**Computational Modeling of Post-Dissemination Dynamics with an Absorbent Intermediary Compartment**

Independent research by Caitlyn Randels, November 2026.

**Speculative modeling only. No clinical claims.**

## Status (27 Nov 2026)
`metastatic_cascade_model.py` is **superseded**: it has the sponge compartment but no Oroboro loop. That means no polarity mesh, consensus, Levy feedback, deterministic reconciliation or PrinciplesGate. It is kept for history. The native model, with every Oroboro component in one loop, is [Oroboro/research/metastasis-native](https://github.com/caitlynrandels-del/Oroboro/tree/main/research/metastasis-native). The v1 and v2 papers below predate that pipeline.

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

Page-image views are now in the repo: [v1](papers/v1/view.html), [v2](papers/v2/view.html), [v3](papers/v3/view.html), [v4](papers/v4/view.html) and [v5](papers/v5/view.html), with SVG pages (and, for v1–v2, plain-text extractions and build scripts). The PDF and Word binaries for v1–v5 remain on the project computer, because the connected GitHub interface stores text only. A short [v4 run summary](v4_Run_Summary.md) is in the repository root, and an index is in [`papers/README.md`](papers/README.md).

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
