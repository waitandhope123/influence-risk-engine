# influence-risk-engine

A theory-driven, data-constrained framework for analyzing how and why states gain, sustain, and lose world influence.

This project models three core components for each country:

- **BIS (Baseline Influence Score)** – structural power from economy, population, military projection, geography, and technology.
- **ULIʳ (Refined Unique Leverage Index)** – how much a state’s influence exceeds its structural baseline due to narrative leverage, elite fungibility, contradiction tolerance, institutional legibility, assimilation capacity, time-horizon elasticity, redundancy of leverage, and low external substitutability.
- **UFIʳ (Refined Unique Fragility Index)** – how likely a state’s influence is to break nonlinearly, based on identity rigidity, coordination friction, dependence asymmetry, shock absorption capacity, elite–mass feedback quality, narrative balance, and temporal mismatch risk.

On top of these scores, the engine tracks **trends** and computes an:

- **IFP (Influence Failure Probability)** – a directional estimate of the chance that a country will suffer a sharp loss of global influence within a ≈20-year horizon.

## Core Ideas

1. **Structural power is not the whole story.**  
   GDP, population, and military capacity explain why some states *can* be influential, but not why some *actually are* more or less influential than expected.

2. **Influence rests on unique levers.**  
   Narrative, institutional depth, elite turnover, and the ability to live with internal contradictions can give a country an influence “bonus” over its baseline.

3. **Failure comes from fragility, not weakness.**  
   States rarely lose influence where they are obviously weak. They break along hidden fault lines: non-redundant advantages, rigid identities, bad feedback, or time-mismatch.

4. **Risk is about *change*, not levels.**  
   The model tracks not only where countries are (BIS, ULIʳ, UFIʳ) but also how fast their leverage and fragility are changing (ΔULI, ΔUFI).

## What this repo will contain

- A clear specification of the model (theory + methodology)
- Python code to:
  - compute BIS, ULIʳ, UFIʳ from structured inputs
  - derive IFP and related indicators
  - run simple shock scenarios (financial, security, technological)
- Example country profiles and comparative analyses

## Status

Early stage (**v0.1** design).  
The first goal is to get a transparent, reproducible scoring pipeline working for a small set of countries, then iteratively calibrate against historical cases.

## License

See `LICENSE`.

For full design context and historical intent, see `docs/master_context.md`.
