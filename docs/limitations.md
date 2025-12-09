# Limitations of the Influence Risk Engine

No model is universal. This one is designed to be **honest** about what
it does well and what it does not attempt to do.

---

## 1. Not a Prediction Machine

The engine produces:

- BIS — structural capacity
- ULIʳ — unique leverage
- UFIʳ — unique fragility
- IFP — influence failure probability

These are **directional risk indicators**, not exact forecasts.

The model does **not**:
- predict specific events (wars, coups, elections)
- provide precise timelines for influence loss
- quantify market moves or asset prices

---

## 2. Limited Time Horizon

The engine is tuned for a **medium-term horizon**:

- roughly **10–20 years** for IFP
- shorter horizons for shock scenarios

It is not meant for:
- day-to-day political forecasting
- century-scale civilizational projections

---

## 3. Data Quality and Subjectivity

Some inputs (BIS components) can be grounded in hard data.
Others (ULIʳ and UFIʳ components) require:

- expert judgment
- qualitative assessment
- interpretation of trends

This introduces **subjectivity**.

To mitigate this:
- all assumptions should be documented
- weights and scores should be applied consistently
- historical analogs should be used for sanity checks

The model does not eliminate judgment.
It **structures** it.

---

## 4. No Hidden Machine Learning

By design:

- no machine learning
- no automatic weight fitting
- no opaque optimization

This means:
- the model will not “discover” new patterns on its own
- it will not adapt automatically to regime shifts

All structural changes require **explicit theoretical and code updates**.

---

## 5. Aggregation Risk

Composite indices (BIS, ULIʳ, UFIʳ, IFP) compress:

- many variables
- into a single number

This is powerful but risky:

- small changes in assumptions can shift scores
- conflicts between sub-components can be obscured
- scores may appear more precise than they truly are

Users should:
- inspect component scores
- not rely on final numbers alone
- treat IFP as a **signal**, not a verdict

---

## 6. System Level, Not Sub-State

The engine operates at the **nation-state level**.

It does not directly model:
- subnational regions
- non-state actors
- transnational networks (corporate, criminal, ideological)

These can strongly affect real-world outcomes, but are only captured
insofar as they affect the main indices indirectly.

---

## 7. Scenario Simplification

Shock scenarios (financial, security, technological):

- apply stylized stress profiles
- adjust fragility components in simple ways

They do **not** capture:
- complex multi-shock interactions
- precise contagion dynamics
- detailed economic or military modeling

They are intended as:
- **stress tests**, not full simulations

---

## 8. Dependence on Initial Calibration

The usefulness of the engine depends heavily on:

- initial score calibration
- reasonable bounds and weights
- thoughtful choice of example countries

Poor calibration will still produce consistent numbers,
but **badly aligned with reality**.

Calibration must be:
- iterative
- historically informed
- periodically revisited

---

## 9. Ethical and Interpretive Limits

The model:

- does not make moral judgments
- does not prescribe policy
- does not measure human welfare or justice

A state can have:
- high BIS, ULIʳ, and low IFP
- and still be harmful to many people

The engine focuses narrowly on:
> **the structure and risk of geopolitical influence**  
not on whether that influence is good.

---

## 10. Bottom Line

This engine is best understood as:

> A structured, explainable framework for reasoning about
> state power, leverage, and fragility over time.

It is:
- useful for **ranking, comparison, and early warning**
- not suitable for **precise event prediction** or
  **fine-grained tactical analysis**

Used within these limits, it can be a powerful tool.
Outside them, it should be treated with caution.
