"""
UFI Calculation Module

Computes the Refined Unique Fragility Index (UFIʳ)
from explicit fragility components.

Design principles:
- transparent aggregation
- theory-first weighting
- emphasis on nonlinear failure risk
"""

from typing import Dict


def calculate_ufi(fragilities: Dict[str, float],
                  weights: Dict[str, float]) -> float:
    """
    Calculate Refined Unique Fragility Index (UFIʳ).

    Parameters
    ----------
    fragilities : dict
        Fragility component scores on 0–100 scale:
        {
            "IR": identity rigidity,
            "CF": coordination friction,
            "DA": dependence asymmetry,
            "SAC": shock absorption capacity (inverted),
            "EMF": elite–mass feedback weakness,
            "NB": narrative imbalance,
            "TMR": temporal mismatch risk
        }

    weights : dict
        Weight per fragility component (should sum to 1.0)

    Returns
    -------
    float
        UFIʳ score on 0–100 scale
    """

    score = 0.0

    for component, value in fragilities.items():
        weight = weights.get(component, 0.0)
        score += weight * value

    return round(score, 2)


if __name__ == "__main__":
    # Example usage with placeholder values

    example_fragilities = {
        "IR": 60.0,
        "CF": 55.0,
        "DA": 65.0,
        "SAC": 40.0,   # lower SAC → higher fragility
        "EMF": 50.0,
        "NB": 45.0,
        "TMR": 70.0,
    }

    example_weights = {
        "IR": 0.15,
        "CF": 0.15,
        "DA": 0.15,
        "SAC": 0.15,
        "EMF": 0.15,
        "NB": 0.10,
        "TMR": 0.15,
    }

    ufi_score = calculate_ufi(example_fragilities, example_weights)
    print(f"Example UFIʳ: {ufi_score}")
