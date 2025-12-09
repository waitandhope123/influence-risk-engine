"""
IFP Calculation Module

Computes Influence Failure Probability (IFP) from:
- current fragility (UFIʳ)
- fragility trend (ΔUFI)
- unique leverage (ULIʳ)
- redundancy and substitutability modifiers

This is a RULE-BASED, NOT STATISTICAL, model.
"""

from typing import Literal


Trend = Literal["up", "flat", "down"]


def trend_multiplier(delta_ufi: Trend) -> float:
    """
    Map ΔUFI trend into a risk multiplier.
    """
    if delta_ufi == "up":
        return 1.25  # fragility rising → amplify risk
    if delta_ufi == "down":
        return 0.85  # fragility falling → dampen risk
    return 1.0       # stable


def leverage_exposure_factor(uli_score: float) -> float:
    """
    Higher ULIʳ means more to lose if things break.
    This acts as a modest amplifier on top of UFIʳ.
    """
    if uli_score >= 75:
        return 1.20
    if uli_score >= 60:
        return 1.10
    if uli_score >= 40:
        return 1.00
    return 0.90  # low leverage → less dramatic failure


def redundancy_modifier(redundancy_score: float) -> float:
    """
    Redundancy reduces failure risk by providing alternate pillars.

    redundancy_score is 0–100, where:
    - higher = more redundant leverage, more paths to sustain influence.
    """
    if redundancy_score >= 70:
        return 0.8
    if redundancy_score >= 50:
        return 0.9
    if redundancy_score >= 30:
        return 1.0
    return 1.1  # very low redundancy → more brittle


def substitutability_modifier(substitutability_score: float) -> float:
    """
    External substitutability:
    - 0 = almost impossible to replace
    - 100 = trivially replaceable

    More substitutable → higher failure risk.
    """
    if substitutability_score <= 20:
        return 0.85
    if substitutability_score <= 40:
        return 0.95
    if substitutability_score <= 60:
        return 1.0
    if substitutability_score <= 80:
        return 1.1
    return 1.2


def clamp(value: float, min_value: float = 0.0, max_value: float = 100.0) -> float:
    """
    Clamp value to [min_value, max_value].
    """
    return max(min_value, min(max_value, value))


def calculate_ifp(
    ufi_score: float,
    delta_ufi: Trend,
    uli_score: float,
    redundancy_score: float,
    substitutability_score: float,
) -> float:
    """
    Compute Influence Failure Probability (IFP) as a 0–100% value.

    Parameters
    ----------
    ufi_score : float
        Refined Unique Fragility Index (0–100)

    delta_ufi : {"up", "flat", "down"}
        Direction of fragility change

    uli_score : float
        Refined Unique Leverage Index (0–100)

    redundancy_score : float
        Overall redundancy of influence levers (0–100)

    substitutability_score : float
        External substitutability (0–100)

    Returns
    -------
    float
        IFP as a percentage on 0–100 scale.
    """

    base_risk = ufi_score  # starting point: fragility level

    # Apply multipliers
    base_risk *= trend_multiplier(delta_ufi)
    base_risk *= leverage_exposure_factor(uli_score)
    base_risk *= redundancy_modifier(redundancy_score)
    base_risk *= substitutability_modifier(substitutability_score)

    # Normalize roughly back into 0–100 band
    # The divisors here act as a manual calibration factor
    normalized = base_risk / 1.5

    return round(clamp(normalized), 2)


if __name__ == "__main__":
    # Example with placeholder values (roughly like a high-risk state)

    example_ufi = 68.0
    example_delta = "up"
    example_uli = 72.0
    example_redundancy = 40.0
    example_substitutability = 65.0

    ifp = calculate_ifp(
        ufi_score=example_ufi,
        delta_ufi=example_delta,
        uli_score=example_uli,
        redundancy_score=example_redundancy,
        substitutability_score=example_substitutability,
    )

    print(f"Example IFP: {ifp}%")
