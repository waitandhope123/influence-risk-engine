"""
ULI Calculation Module

Computes the Refined Unique Leverage Index (ULIʳ) from
explicit leverage components.

Design principles:
- transparent aggregation
- theory-aligned weights
- no data fitting or optimization
"""

from typing import Dict


def calculate_uli(leverages: Dict[str, float],
                  weights: Dict[str, float]) -> float:
    """
    Calculate Refined Unique Leverage Index (ULIʳ).

    Parameters
    ----------
    leverages : dict
        Leverage component scores on 0–100 scale:
        {
            "NL": narrative leverage,
            "EF": elite fungibility,
            "CT": contradiction tolerance,
            "LAD": legibility & administrative depth,
            "PAR": peripheral assimilation rate,
            "THE": time-horizon elasticity,
            "RoL": redundancy of leverage,
            "ESI": external substitutability (inverted)
        }

    weights : dict
        Weight per leverage component (should sum to 1.0)

    Returns
    -------
    float
        ULIʳ score on 0–100 scale
    """

    score = 0.0

    for component, value in leverages.items():
        weight = weights.get(component, 0.0)
        score += weight * value

    return round(score, 2)


if __name__ == "__main__":
    # Example usage with placeholder values

    example_leverages = {
        "NL": 80.0,
        "EF": 75.0,
        "CT": 70.0,
        "LAD": 85.0,
        "PAR": 65.0,
        "THE": 75.0,
        "RoL": 80.0,
        "ESI": 70.0,
    }

    example_weights = {
        "NL": 0.15,
        "EF": 0.15,
        "CT": 0.10,
        "LAD": 0.15,
        "PAR": 0.10,
        "THE": 0.15,
        "RoL": 0.10,
        "ESI": 0.10,
    }

    uli_score = calculate_uli(example_leverages, example_weights)
    print(f"Example ULIʳ: {uli_score}")
