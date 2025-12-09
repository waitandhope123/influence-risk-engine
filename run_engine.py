"""
Influence Risk Engine — End-to-End Runner

Loads a country profile and computes:
BIS → ULIʳ → UFIʳ → Δ → IFP

This is the main execution entry point.
"""

from data.processed.country_profiles.example_country import (
    COUNTRY_NAME,
    BIS_INPUTS,
    BIS_BOUNDS,
    BIS_WEIGHTS,
    ULI_LEVERAGES,
    ULI_WEIGHTS,
    REDUNDANCY_SCORE,
    SUBSTITUTABILITY_SCORE,
    UFI_FRAGILITIES,
    UFI_WEIGHTS,
    DELTA_UFI,
)

from models.bis.bis_calculation import calculate_bis
from models.uli.uli_weights import calculate_uli
from models.uli.redundancy import adjust_for_redundancy
from models.ufi.fragility_factors import calculate_ufi
from models.risk.ifp_calculation import calculate_ifp


def run():
    print(f"\nRunning Influence Risk Engine for {COUNTRY_NAME}\n")

    # -----------------
    # BIS
    # -----------------
    bis = calculate_bis(
        structural_inputs=BIS_INPUTS,
        bounds=BIS_BOUNDS,
        weights=BIS_WEIGHTS,
    )

    # -----------------
    # ULIʳ
    # -----------------
    raw_uli = calculate_uli(
        leverages=ULI_LEVERAGES,
        weights=ULI_WEIGHTS,
    )

    uli = adjust_for_redundancy(
        uli_score=raw_uli,
        leverage_components=ULI_LEVERAGES,
    )

    # -----------------
    # UFIʳ
    # -----------------
    ufi = calculate_ufi(
        fragilities=UFI_FRAGILITIES,
        weights=UFI_WEIGHTS,
    )

    # -----------------
    # IFP
    # -----------------
    ifp = calculate_ifp(
        ufi_score=ufi,
        delta_ufi=DELTA_UFI,
        uli_score=uli,
        redundancy_score=REDUNDANCY_SCORE,
        substitutability_score=SUBSTITUTABILITY_SCORE,
    )

    # -----------------
    # OUTPUT
    # -----------------
    print("RESULTS")
    print("-------")
    print(f"BIS : {bis}")
    print(f"ULIʳ: {uli}")
    print(f"UFIʳ: {ufi}")
    print(f"IFP : {ifp}%\n")


if __name__ == "__main__":
    run()
