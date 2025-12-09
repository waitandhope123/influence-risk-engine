"""
BIS Calculation Module

This module computes the Baseline Influence Score (BIS) for a country
using normalized structural inputs.

The design philosophy is:
- transparent
- theory-first
- no machine learning
- no hidden optimization
"""

from typing import Dict


def normalize(value: float, min_value: float, max_value: float) -> float:
    """
    Normalize a raw value to a 0–100 scale.
    """
    if max_value == min_value:
        return 0.0
    return 100.0 * (value - min_value) / (max_value - min_value)


def calculate_bis(structural_inputs: Dict[str, float],
                  bounds: Dict[str, Dict[str, float]],
                  weights: Dict[str, float]) -> float:
    """
    Calculate Baseline Influence Score (BIS).

    Parameters
    ----------
    structural_inputs : dict
        Raw structural metrics for a country, keyed by component:
        {
            "ES": economic scale,
            "PH": population & human capital,
            "MP": military projection,
            "GS": geography & strategic position,
            "TI": technology & industrial base
        }

    bounds : dict
        Min/max bounds used for normalization per component:
        {
            "ES": {"min": x, "max": y},
            ...
        }

    weights : dict
        Weight per component (should sum to 1.0).

    Returns
    -------
    float
        BIS score on 0–100 scale.
    """

    score = 0.0

    for component, raw_value in structural_inputs.items():
        component_bounds = bounds.get(component)
        weight = weights.get(component, 0.0)

        if component_bounds is None:
            continue

        normalized_value = normalize(
            raw_value,
            component_bounds["min"],
            component_bounds["max"]
        )

        score += weight * normalized_value

    return round(score, 2)


if __name__ == "__main__":
    # Example usage with placeholder values

    example_inputs = {
        "ES": 75.0,
        "PH": 65.0,
        "MP": 90.0,
        "GS": 80.0,
        "TI": 85.0,
    }

    example_bounds = {
        "ES": {"min": 0.0, "max": 100.0},
        "PH": {"min": 0.0, "max": 100.0},
        "MP": {"min": 0.0, "max": 100.0},
        "GS": {"min": 0.0, "max": 100.0},
        "TI": {"min": 0.0, "max": 100.0},
    }

    example_weights = {
        "ES": 0.25,
        "PH": 0.20,
        "MP": 0.25,
        "GS": 0.15,
        "TI": 0.15,
    }

    bis_score = calculate_bis(example_inputs, example_bounds, example_weights)
    print(f"Example BIS: {bis_score}")
