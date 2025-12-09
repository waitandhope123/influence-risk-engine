"""
Example Country Profile

This file defines all model inputs for a single country.
It contains NO logic — only structured inputs.
"""

COUNTRY_NAME = "Exampleland"

# -----------------
# BIS INPUTS
# -----------------

BIS_INPUTS = {
    "ES": 75.0,  # economic scale
    "PH": 65.0,  # population & human capital
    "MP": 80.0,  # military projection
    "GS": 70.0,  # geography & strategic position
    "TI": 85.0,  # technology & industry
}

BIS_BOUNDS = {
    "ES": {"min": 0, "max": 100},
    "PH": {"min": 0, "max": 100},
    "MP": {"min": 0, "max": 100},
    "GS": {"min": 0, "max": 100},
    "TI": {"min": 0, "max": 100},
}

BIS_WEIGHTS = {
    "ES": 0.25,
    "PH": 0.20,
    "MP": 0.25,
    "GS": 0.15,
    "TI": 0.15,
}

# -----------------
# ULI INPUTS
# -----------------

ULI_LEVERAGES = {
    "NL": 75.0,
    "EF": 70.0,
    "CT": 65.0,
    "LAD": 80.0,
    "PAR": 60.0,
    "THE": 75.0,
    "RoL": 55.0,
    "ESI": 45.0,  # lower = harder to substitute
}

ULI_WEIGHTS = {
    "NL": 0.15,
    "EF": 0.15,
    "CT": 0.10,
    "LAD": 0.15,
    "PAR": 0.10,
    "THE": 0.15,
    "RoL": 0.10,
    "ESI": 0.10,
}

REDUNDANCY_SCORE = 55.0
SUBSTITUTABILITY_SCORE = 45.0

# -----------------
# UFI INPUTS
# -----------------

UFI_FRAGILITIES = {
    "IR": 55.0,
    "CF": 50.0,
    "DA": 60.0,
    "SAC": 40.0,
    "EMF": 45.0,
    "NB": 50.0,
    "TMR": 65.0,
}

UFI_WEIGHTS = {
    "IR": 0.15,
    "CF": 0.15,
    "DA": 0.15,
    "SAC": 0.15,
    "EMF": 0.15,
    "NB": 0.10,
    "TMR": 0.15,
}

# -----------------
# TRENDS
# -----------------

DELTA_ULI = "flat"   # "up", "flat", "down"
DELTA_UFI = "up"     # "up", "flat", "down"
