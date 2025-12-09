"""
Shock Absorption Module

Applies stress from external shocks to fragility components.
Used by scenario simulations.

This does NOT change BIS.
It modifies UFIʳ drivers under stress.
"""

from typing import Dict


def apply_shock(fragilities: Dict[str, float],
                shock_profile: Dict[str, float]) -> Dict[str, float]:
    """
    Apply a shock profile to fragility components.

    Parameters
    ----------
    fragilities : dict
        Base fragility scores (0–100)

    shock_profile : dict
        Shock impact per component (positive = more fragile):
        {
            "IR": +5,
            "CF": +10,
            ...
        }

    Returns
    -------
    dict
        Updated fragility scores, capped at 100
    """

    stressed = {}

    for component, base_value in fragilities.items():
        delta = shock_profile.get(component, 0.0)
        stressed_value = min(100.0, base_value + delta)
        stressed[component] = round(stressed_value, 2)

    return stressed


if __name__ == "__main__":
    base_fragility = {
        "IR": 60,
        "CF": 55,
        "DA": 65,
        "SAC": 40,
        "EMF": 50,
        "NB": 45,
        "TMR": 70,
    }

    financial_shock = {
        "DA": 10,
        "CF": 5,
        "SAC": 15,
        "EMF": 5,
    }

    stressed = apply_shock(base_fragility, financial_shock)
    print("Stressed fragilities:", stressed)
