# v4 Full Rerun Summary

**Completed 26 November 2026, 8:57 PM PT**

Independent computational modeling note  
Caitlyn C. Randels

## Overview

The v4 full rerun of the discrete-time stochastic post-dissemination cascade model (with absorbent intermediary / sponge as a standard on/off toggle, public-data fits, optional layers, and the operational update sequence) completed successfully.

## Scale and consistency

- 3.82 million simulation runs
- Zero consistency failures (whole-versus-parts and observer checks)
- All 399 adaptive experimental setups reached the ±1-point precision target
- Update sequence (quick fix → UPDATE ALL → undo → Timestamp → do it again → syntax/autocorrect) ran on all 291 parameter updates and made no substantive corrections (pure validator)

## Key computational findings (internal to the model)

- Data fits matched the prior (v3) run exactly, including the 37.8 % dormant fraction versus the 36.1 % public-data target.
- Sponge on versus off (higher precision):
  - Visible tumors: 17.2 % → 13.3 %
  - Hidden-cell pool increased by approximately 11 points
  - Full elimination decreased by approximately 7 points
  - Median time to first overt lesion: month 62 versus 51
- New observations relative to v3:
  - Activating all optional layers (particularly the tissue-scaffold / ECM layer) worsened fit to public data, even with the sponge off.
  - Sponge size showed a small (~1-point) effect under heavy load; default size was near-optimal.
- Held from prior runs:
  - Elimination ceiling with sponge on remained in the 0.72–0.76 range.
  - Combined sponge membrane gating + elevated establishment threshold reached 0.988 full elimination.

## Status

Results and code reside in the local workspace under the v4 run directory. Speculative modeling only; no clinical claims.

---
*Added November 2026.*
