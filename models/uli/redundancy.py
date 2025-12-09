"""
Redundancy Adjustment Module

Adjusts ULIʳ based on how many independent leverage pillars
support a country’s influence.

More redundancy = more resilient leverage.
Low redundancy = brittle overperformance.
"""

from typing import Dict


def adjust_for_redundancy(uli_score: float,
                          leverage_components: Dict[str, float],
                          threshold: float = 60.0) -> float:
    """
    Apply redundancy adjustment to ULIʳ.

    Parameters
    ----------
    uli_score : float
        Raw ULIʳ score (0–100)

    leverage_components : dict
        Individual leverage component scores (0–100)

    threshold : float
        Score above which a component counts as "strong"

    Returns
    -------
    float
        Adjusted ULIʳ score
    """

    strong_pillars = sum(
        1 for value in leverage_components.values() if value >= threshold
    )

    # Redundancy factor: more strong pillars → less brittleness
    if strong_pillars <= 2:
        multiplier = 0.85
    elif strong_pillars == 3:
        multiplier = 0.95
    else:
        multiplier = 1.0

    adjusted_score = uli_score * multiplier
    return round(adjusted_score, 2)


if __name__ == "__main__":
    example_components = {
        "NL": 80,
        "EF": 75,
        "CT": 70,
        "LAD": 85,
        "PAR": 40,
        "THE": 60,
        "RoL": 50,
        "ESI": 45,
    }

    raw_uli = 72.5
    adjusted_uli = adjust_for_redundancy(raw_uli, example_components)
    print(f"Adjusted ULIʳ: {adjusted_uli}")
