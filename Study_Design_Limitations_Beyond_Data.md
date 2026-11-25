# Additional Subsection: Limitations of the Study Design Itself (Beyond Data Application)

**Added November 2026**

Yes. Even setting aside every issue with how real-world data were chosen, mapped, or matched, the study itself has several structural and design limitations.

## Model structure (independent of the data used)

- Shedding continues at a constant rate for the full 120 months with no primary-tumor growth, treatment, or shut-off.
- There is no secondary seeding from established lesions, no lesion growth kinetics, and no clinical-detection threshold. An “overt lesion” is simply a successful colonization event.
- No spatial structure inside organs and no separate immune compartments; clearance is a single per-cell probability modulated by an immune-evasion draw.
- The ever-dormant fraction has a hard structural ceiling (~0.285) caused by checkpoint removal of arrested cells before seeding; this cannot be removed by parameter changes alone.
- The load-dependent elevation of the checkpoint threshold (activated above 40 live cells) is never triggered under the calibrated regime (maximum shed cells in any baseline run = 9), so that mechanistic branch remains untested.

## Fixed or uncalibrated constants

Many parameters that shape outcomes were held fixed and never varied:

- dormant clearance probability (0.01),
- checkpoint score weights and the 0.65 acceptance probability,
- colonization thresholds (0.30 / 0.42),
- dormancy-depth kinetics,
- the distributions of epigenetic state, fitness, and immune evasion,
- preferred-organ permissiveness locked at 0.95.

No sensitivity analysis was performed on these values.

## Experimental design

- All dose-response, combination, and onset-timing sweeps were run only under the single main (MSK-MET) parameter set. They were not repeated under the fixed-shedding solution, under registry organ weights, or at alternative values of the uncalibrated constants.
- Interaction (Bliss) ratios become unstable once expected event counts approach the Monte Carlo floor (~0.0004).
- Thresholds for “meeting the dual criterion” are grid-dependent and rest on arbitrary cut-offs (1 % overt, 10 % dormant).
- Pooled results weight the five tumor types equally rather than by incidence or prevalence.

## Scope

The work is a self-contained sensitivity study of one specific cascade implementation. It contains no comparison to other mathematical or agent-based metastasis models and no module that converts colonization events into clinically detectable lesions or time-to-detection distributions.

In short, even with perfect data the study would still be limited by its structural simplifications, the large set of unvaried constants, the restriction of the sensitivity analysis to a single parameter regime, and the absence of lesion growth or detection. These are limitations of the study design itself.

---

*This subsection was added to the combined peer-review document without altering any prior content.*
