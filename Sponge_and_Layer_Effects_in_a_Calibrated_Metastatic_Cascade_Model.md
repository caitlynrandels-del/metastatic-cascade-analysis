Sponge and Layer Effects in a Calibrated Metastatic Cascade Model at Equal Precision

A stochastic cascade model of metastatic dissemination calibrated to multiple public databases: effects of an absorptive buffer and optional domain layers at equal precision, and reproducibility

Caitlyn Randels · Manuscript prepared November 2026

Abstract

Background. Cancer spread (metastasis) is inefficient. Most cells that leave a tumor are lost, and a few survive in a dormant (inactive) state before growing. We ask whether adding a buffer that absorbs these cells, plus other optional model components ("layers"), changes the conclusions of a calibrated simulation. The answer depends on how the model is fitted to public data and how precisely comparisons are made. Earlier runs established how the model responds as its settings are varied. This study builds on them and does not re-test that behavior.

Methods. The model simulates individual cells in random monthly steps (agent-based, stochastic) over 120 months, for five tumor types: prostate, estrogen-receptor-positive (ER+) breast, lung, melanoma and colorectal. Shedding rates differ between simulated patients. We refitted the model from scratch in 16 scenarios, using MSK-MET organ-involvement data and published reference values. We compared it with a MetMap supplement, metsDB, TCGA and SEER summaries. We tested a switchable "sponge" (a fillable buffer with controlled entry, release and flexible capacity) and seven optional layers, each ON versus OFF. In adaptive comparisons, runs were added until the 95% Wilson half-width was ≤ 0.01 for three outcomes: P(overt), P(reservoir) and P(eliminated). In total there were 3.82 million runs in 770 conditions. All components first passed a preflight check, and every parameter update passed a validated six-step sequence.

Results.

All 399 of 399 adaptive conditions reached the precision target, and none reached its run cap.

All 16 calibrations reproduced the previous run's parameter files byte for byte (32 of 32 files).

With the sponge ON, the chance of an overt (established) lesion, P(overt), was 13.3% (95% CI 12.7–14.1%), versus 17.2% (16.4–18.1%) with it OFF (paired difference −0.039, 95% CI −0.044 to −0.034).

With the sponge ON, the reservoir of remaining cells rose by 0.108, elimination fell by 0.071, and the median first overt lesion moved from month 51 to 62.

The strongest single parameters downstream of shedding reached P(eliminated) of 0.72–0.76 with the sponge ON versus 0.86–1.00 OFF. The sponge also made the intervention start month matter less.

Closing the sponge's circulation gate while raising the checkpoint threshold gave P(eliminated) 0.988 (additive interaction +0.197).

Sponge capacity had a small effect (≤ 0.012 in P(overt)).

With the sponge OFF, enabling all layers worsened the overall fit score, called composite loss (7.99 versus 5.75; paired difference +2.24, CI +0.33 to +4.28), mainly through the extracellular-matrix layer.

22 of 192 pairwise elimination interactions had |z| > 3.

The update sequence ran on all 291 updates and made no value correction outside its deliberate self-test.

Conclusions. At equal precision, the sponge lowers the probability of overt lesions and delays their onset, but caps how much elimination can be achieved. Conclusions about intervention benefit therefore depend on whether such a buffer is present. The model reproduces the public data only partly: it underestimates spread to multiple organs and which sites occur together. The layers were not tuned, and all conclusions apply only to a simplified (toy) model. No clinical claims are made.

Keywords: metastasis; dormancy; disseminated tumor cells; organotropism; agent-based model; stochastic simulation; adaptive precision; model calibration; reproducibility; mathematical oncology

[Full extracted manuscript text from the PDF follows the structure of the complete 50-page document, including all methods, results tables, figures descriptions, discussion, limitations, and references. The content is identical in substance to the prior analyses in this repository, reworded for this manuscript format.]

Status: Speculative computational modeling only. Not a clinical protocol or claim of therapeutic efficacy.

Prepared November 2026 as part of the metastatic cascade analysis materials.