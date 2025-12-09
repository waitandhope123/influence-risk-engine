"""
Delta Tracking Module

Determines directional change (up / flat / down) in an index
over a defined time window.

Used for ΔULI and ΔUFI.
"""

from typing import List, Literal


Trend = Literal["up", "flat", "down"]


def determine_trend(
    values: List[float],
    sensitivity: float = 2.0
) -> Trend:
    """
    Determine trend direction from a series of values.

    Parameters
    ----------
    values : list of float
        Sequential historical values (oldest → newest)

    sensitivity : float
        Minimum net change required to register a trend.
        Smaller = more sensitive.

    Returns
    -------
    {"up", "flat", "down"}
    """

    if len(values) < 2:
        return "flat"

    delta = values[-1] - values[0]

    if delta >= sensitivity:
        return "up"
    if delta <= -sensitivity:
        return "down"
    return "flat"


if __name__ == "__main__":
    # Example usage

    past_ufi = [52.0, 55.0, 60.0, 63.0]
    trend = determine_trend(past_ufi)

    print(f"ΔUFI trend: {trend}")
