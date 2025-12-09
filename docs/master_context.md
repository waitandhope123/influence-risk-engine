We are working on a completed analytical framework and GitHub repository called:

"influence-risk-engine"

Purpose:
A theory-driven, data-constrained engine for analyzing how states gain, sustain, and lose global influence, with a focus on nonlinear failure risk rather than short-term event prediction.

Core Concept:
Global influence is decomposed into three distinct layers:

1) BIS — Baseline Influence Score
   - Structural capacity only (economy, population, military, geography, technology)
   - Slow-moving, conservative, non-predictive
   - Answers: “How influential should this state be on paper?”

2) ULIʳ — Refined Unique Leverage Index
   - Explains why states overperform or underperform relative to BIS
   - Includes narrative leverage, elite fungibility, contradiction tolerance,
     administrative depth, assimilation capacity, time-horizon elasticity,
     redundancy of leverage, and external substitutability
   - Overperformance increases exposure if leverage is non-redundant

3) UFIʳ — Refined Unique Fragility Index
   - Measures risk of nonlinear influence failure (not weakness)
   - Includes identity rigidity, coordination friction, dependence asymmetry,
     shock absorption capacity, elite–mass feedback, narrative balance,
     temporal mismatch risk
   - Fragility often rises before visible decline

4) IFP — Influence Failure Probability
   - Synthesizes UFIʳ, ΔUFI trend, ULIʳ, redundancy, and substitutability
   - Expressed as a 0–100% medium-term (≈10–20 year) early-warning probability
   - Directional and comparative, not a timing forecast

Key Structural Insight:
Power does not usually fail where it is weakest — it fails along hidden fault lines.
Influence can be overproduced, brittle, and collapse nonlinearly.

Calibration Status:
- Structurally and historically calibrated (patterns validated against major historical cases)
- Not statistically optimized or ML-driven by design
- Transparent, rule-based, explainable

Repository State:
The repo is complete at v0.1-alpha with:
- Full directory structure
- Python modules for BIS, ULI, UFI, IFP
- Trend (Δ) tracking
- Scenario simulation (financial, security, tech shocks)
- End-to-end pipeline script (run_engine.py)
- Country profile format
- Documentation: theory.md, methodology.md, limitations.md
- Designed for extensibility, not black-box prediction

Design Philosophy:
- Theory-first, data-constrained
- Explainability over precision
- Early warning over short-term forecasting
- Comparable across countries and time
- Explicit assumptions, no hidden optimization

Current Status:
The engine is DONE at v0.1.
Next possible steps (optional):
- Add real country profiles
- Backcast historical cases
- Light numeric calibration (scale only, not logic)
- Version v0.2 planning

Resume from here without re-explaining basics.
