"""
Scenario Runner

Applies a shock scenario to a country's fragility profile,
recalculates UFIʳ and IFP, and reports deltas.

This is the main entry point for stress testing.
"""

from typing import Dict

from models.ufi.fragility_factors import calculate_ufi
from models.ufi.shock_absorption import apply_shock
from models.risk.ifp_calculation import calculate_ifp


def run_scenario(
    base_fragilities: Dict[str, float],
    fragility_weights: Dict[str, float],
    shock_profile: Dict[str, float],
    uli_score: float,
    delta_ufi: str,
    redundancy_score: float,
    substitutability_score: float,
) -> Dict[str, float]:
    """
    Run a single shock scenario.

    Returns updated UFIʳ and IFP.
    """

    # Apply shock to fragility components
    stressed_fragilities = apply_shock(base_fragilities, shock_profile)

    # Recalculate UFIʳ
    stressed_ufi = calculate_ufi(stressed_fragilities, fragility_weights)

    # Recalculate IFP
    stressed_ifp = calculate_ifp(
        ufi_score=stressed_ufi,
        delta_ufi=delta_ufi,
        uli_score=uli_score,
        redundancy_score=redundancy_score,
        substitutability_score=substitutability_score,
    )

    return {
        "UFI_after_shock": stressed_ufi,
        "IFP_after_shock": stressed_ifp,
    }


if __name__ == "__main__":
    # Example test run (placeholder values)

    base_fragility = {
        "IR": 60,
        "CF": 55,
        "DA": 65,
        "SAC": 40,
        "EMF": 50,
        "NB": 45,
        "TMR": 70,
    }

    fragility_weights = {
        "IR": 0.15,
        "CF": 0.15,
        "DA": 0.15,
        "SAC": 0.15,
        "EMF": 0.15,
        "NB": 0.10,
        "TMR": 0.15,
    }

    financial_shock = {
        "DA": 10,
        "CF": 5,
        "SAC": 15,
    }

    result = run_scenario(
        base_fragilities=base_fragility,
        fragility_weights=fragility_weights,
        shock_profile=financial_shock,
        uli_score=72.0,
        delta_ufi="up",
        redundancy_score=40.0,
        substitutability_score=65.0,
    )

    print("Scenario result:", result)
