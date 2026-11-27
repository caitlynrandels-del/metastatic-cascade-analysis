# Computational Modeling of Post-Dissemination Dynamics in Metastatic Cancer: Effects of an Absorbent Intermediary Compartment on Dormancy and Colonization

**A Discrete-Time Stochastic Simulation Study Informed by Public Metastatic Datasets**

Caitlyn C. Randels  
Independent Researcher  
November 2026

## Abstract

**Background.** Metastatic dissemination is inefficient: the majority of circulating tumor cells are lost, a minority persist in a dormant state, and few establish overt lesions. Computational models can systematically vary stages of the post-dissemination cascade to identify which parameters most strongly influence residual disease burden.

**Methods.** A discrete-time stochastic agent-based model of the cascade (shedding, circulation, arrest, establishment, dormancy, reawakening, and overt colonization) was evaluated over a 120-month horizon. The study comprised 1,364,500 simulation runs and 14 parameter fits against publicly available metastatic datasets (primarily MSK-MET, with supporting inputs from MetMap 500, metsDB summary statistics, TCGA via cBioPortal, and SEER aggregate tables). An optional absorbent intermediary compartment (“sponge”), parameterized by capacity, permeability, and membrane gating, was introduced between circulating/dormant states and final reconciliation. Uncertainty was quantified by cluster bootstrap; significance was defined by non-overlapping 95% intervals under matched random seeds.

**Results.** Incorporation of inter-patient heterogeneity in shedding rate, required for consistency with multi-organ patterns in MSK-MET, eliminated a prior systematic under-prediction of the dormant fraction (model 37.8% versus observed 36.1%). Activation of the sponge compartment reduced overt colonization from 17.1% to 13.5%, increased the residual hidden-cell pool from 21.7% to 32.4%, delayed median time to first overt lesion from 51 to 62 months, and lowered full elimination from 73.8% to 66.8% across five organotropism configurations. The sponge imposed an elimination ceiling of approximately 73–76% under the strongest single-parameter interventions; this ceiling was exceeded (reaching 98.6%) only when membrane gating was combined with elevation of the establishment threshold. No abrupt transition was observed at sponge saturation. Additional optional layers (immune exhaustion, secondary reseeding, tissue stiffness) produced measurable but configuration-dependent shifts.

**Conclusions.** Within this computational framework, residual disease burden is governed primarily by tissue-level establishment and organ permissiveness, with an absorbent intermediary able to buffer circulating and dormant cells and thereby alter both the probability and timing of overt colonization. The results are model-derived and do not constitute clinical evidence.

## 1. Introduction

The metastatic cascade comprises dissemination from the primary tumor, survival in the circulation, arrest and establishment in distant organs, a variable period of dormancy, and eventual outgrowth. Empirical descriptions consistently note three qualitative features: most circulating cells are eliminated, a subset can persist without proliferation for extended periods, and tumor types differ in preferred colonization sites (organotropism). Because the relevant events are rare and spatially distributed, experimental dissection of the relative contribution of each stage remains challenging.

Agent-based and discrete-time stochastic models permit systematic variation of individual stages at scale, allowing identification of parameters that most strongly shape the eventual burden of overt disease and residual dormant cells. The present study implements such a model, calibrates selected parameters against publicly available metastatic datasets, and evaluates the consequences of introducing an absorbent intermediary compartment that can sequester circulating or dormant cells prior to final reconciliation of the system state.

## 2. Methods

### 2.1 Model structure

Each simulation represents a single host over 120 monthly time steps. Cells are shed from a primary site (approximately 240 per run under default settings) and may be cleared in the circulation, arrest in an organ according to configuration-specific permissiveness weights, and then pass, fail, or be held at an establishment step. The establishment step compares a weighted multi-feature score against a threshold (default 0.65, dynamically increasing under high local cell density). Successfully established cells enter dormancy, may be cleared while dormant, and attempt exit from dormancy at a low rate. Exit may result in overt colonization or return to dormancy. Five organotropism configurations were examined: prostate-like and ER+ breast-like (bone-preferring), lung-like and melanoma-like (lung-preferring), and colorectal-like (liver-preferring).

### 2.2 Absorbent intermediary compartment

An optional absorbent compartment was placed between independent cellular processing and final state reconciliation. The compartment is characterized by a capacity limit (optionally bounded by a hard cap), a permeability parameter governing release rate, and a membrane gating term controlling entry. Cells held within the compartment are counted as part of the residual hidden pool until released or cleared. All sponge parameters were treated as free assumptions and were swept across ranges; no direct empirical measurements of the compartment were available.

### 2.3 Data sources and fitting

Publicly available datasets used for fitting or qualitative constraint included MSK-MET (metastatic site annotations and genomic features), MetMap 500 (cell-line metastatic potential by organ), metsDB summary counts, TCGA multi-omics via cBioPortal, and SEER aggregate incidence/survival tables. MetaTropismDB was unavailable at the time of analysis. Inter-patient heterogeneity in shedding rate was introduced to accommodate multi-organ patterns present in MSK-MET. Fourteen independent fits were performed; each terminated after a fixed number of optimization rounds followed by a final evaluation of the best parameter set.

### 2.4 Simulation design and statistics

The full study comprised 1,364,500 simulation runs distributed across baseline, single-parameter, timing, pairwise, sponge-saturation, sponge on/off, optional-layer, and establishment-checkpoint experiments. Optional layers examined included immune exhaustion, secondary reseeding, tissue stiffness, and niche effects. Uncertainty was quantified by cluster bootstrap over random seeds. A difference was considered significant when the 95% intervals of the compared conditions did not overlap under matched seeds. All model rates remain internal parameters; none is a direct clinical measurement.

## 3. Results

### 3.1 Calibration to public data

Inclusion of inter-patient variation in shedding rate, necessitated by the multi-organ structure of MSK-MET, removed a prior systematic under-prediction of the dormant fraction. The calibrated model produced a dormant share of 37.8% against an observed target of 36.1%. Without this heterogeneity the fit residual increased approximately six-fold. MetMap rankings, derived from murine xenograft experiments, systematically favored lung colonization and were therefore retained only as a comparative reference rather than a fitting target.

### 3.2 Effect of the absorbent compartment

Across 2,000 matched runs per organotropism configuration, activation of the sponge reduced the fraction of runs developing an overt colony from 17.1% to 13.5%, increased the residual hidden-cell pool (dormant or compartment-held) from 21.7% to 32.4%, delayed the median month of first overt lesion from 51 to 62, and lowered the probability of full elimination (no overt colony and no residual hidden cell at month 120) from 73.8% to 66.8%. These directional shifts were consistent across all five configurations. Organ preference rankings remained unchanged (lung > colorectal > melanoma > breast > prostate).

### 3.3 Elimination ceiling and combinatorial interventions

Under the strongest single-parameter settings the sponge imposed an elimination ceiling of approximately 73–76%, compared with nearly complete elimination when the compartment was absent. The ceiling was exceeded only by the combination of membrane gating (reducing entry) and elevation of the establishment threshold, which together produced 98.6% full elimination. Isolated membrane gating yielded 72.9% and isolated elevation of the establishment threshold yielded 72.5%. No discontinuous transition was detected when the compartment reached its hard capacity limit (observed in up to 66% of runs).

### 3.4 Optional biological and physical layers

Immune exhaustion increased clearance; secondary reseeding improved concordance with MSK-MET multi-organ patterns; tissue stiffness degraded organotropism concordance. Niche effects were small. Pure observational heat-trace recording produced no change in outcomes, as expected. When all optional layers were activated simultaneously with the sponge, overall fit quality deteriorated, driven primarily by the materials-property layer.

## 4. Discussion

The model reproduces the well-established qualitative features of metastatic inefficiency, residual dormancy, and organotropism while allowing quantitative examination of stage-specific control. The principal empirical constraint—inter-patient shedding heterogeneity required by MSK-MET—materially improved agreement with observed dormant fractions. Introduction of an absorbent intermediary demonstrates that a capacity-limited buffering step can decouple circulating-cell clearance from residual disease burden and can impose an upper bound on elimination achievable by upstream interventions alone.

Several limitations must be emphasized. All sponge parameters are unmeasured assumptions subjected to parameter sweeps; their biological counterparts, if any, remain undefined. The model contains no representation of specific molecular mechanisms, immune-cell dynamics beyond a simple exhaustion term, or spatial tissue architecture. Public datasets were used only at the level of aggregate site frequencies and summary statistics; no patient-level genomic or clinical covariates entered the fitting procedure beyond the shedding-heterogeneity term. Consequently, the numerical results are internal to the computational framework and do not support clinical inference, therapeutic recommendation, or claims of disease modification.

Future work could incorporate direct experimental measurements of circulating-cell sequestration, refine organ-specific permissiveness from additional public cohorts, and test whether the combinatorial advantage of establishment-threshold elevation plus membrane gating persists under alternative model structures.

## 5. Conclusions

In a large-scale discrete-time stochastic model of the post-dissemination cascade, residual metastatic burden is controlled primarily at the establishment step and by organ permissiveness. An absorbent intermediary compartment buffers circulating and dormant cells, reduces and delays overt colonization, and creates an elimination ceiling that is overcome only by combined gating and establishment interventions. The findings are strictly computational and require experimental validation before any biological or clinical interpretation.

## Data and Code Availability

Simulation code, parameter tables, and summary outputs are available in the associated repository. Public datasets were accessed from their original sources (MSK-MET via cBioPortal/Zenodo, MetMap via DepMap, TCGA via cBioPortal, SEER summary tables). No restricted or patient-level data requiring data-use agreements were downloaded.

## Competing Interests

The author declares no competing interests.

## Funding

This work received no external funding.

---

*Independent research. Speculative computational modeling only. Not a clinical protocol or claim of therapeutic efficacy.*
