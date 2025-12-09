# Influence Risk Engine — Theoretical Overview

## 1. Core Question

The Influence Risk Engine is built to answer a specific question:

> Why do some states lose world influence suddenly, despite still
> looking powerful on paper, while others degrade slowly or remain
> stable?

To do that, the model separates:

- **Structural power** (what a state *should* be able to do)
- **Unique leverage** (why it punches above or below its weight)
- **Fragility** (where and how that influence can break)

---

## 2. Three Main Indices

### 2.1 BIS — Baseline Influence Score

BIS estimates how influential a state would be **based only on
structural factors**:

- economic scale
- population & human capital
- military capacity and projection
- geography and strategic position
- technology and industrial base

It answers:

> “How influential would this country be if everything else were neutral?”

BIS changes slowly and is intentionally conservative.

---

### 2.2 ULIʳ — Refined Unique Leverage Index

ULIʳ measures how much a state’s **actual influence** exceeds (or falls
short of) what BIS would predict.

It captures things like:

- narrative leverage (ideology, story, cultural pull)
- elite fungibility (replaceable, competent leadership)
- contradiction tolerance (ability to operate with hypocrisy)
- legibility and administrative depth (state capacity)
- assimilation rate at the periphery (how fast outsiders become insiders)
- time-horizon elasticity (willingness to think in decades)
- redundancy of leverage (multiple independent pillars of influence)
- external substitutability (how easy it is to be replaced)

ULIʳ answers:

> “What is this country’s unique ‘influence bonus’ above its baseline?”

---

### 2.3 UFIʳ — Refined Unique Fragility Index

UFIʳ measures the risk that a state’s influence will **fail abruptly**
rather than erode slowly.

It is not about weakness, but **breakpoints**.

It considers:

- identity rigidity
- coordination friction and veto players
- dependence asymmetry (overreliance on narrow exports, routes, patrons)
- shock absorption capacity
- elite–mass feedback quality
- narrative balance (coherence vs polarization)
- temporal mismatch risk (institutions lagging change)

UFIʳ answers:

> “How likely is it that this country’s influence fails in a *nonlinear*
> way if pressure rises?”

---

## 3. IFP — Influence Failure Probability

The model combines UFIʳ, its **trend** (ΔUFI), ULIʳ, redundancy, and
substitutability into a single synthetic indicator:

- **IFP (0–100%)** — the probability of a sharp loss of influence within
  a roughly 10–20 year horizon.

High BIS can delay failure, but it does not eliminate high IFP.

---

## 4. Change and Trends

Static scores are not enough.

The engine tracks:

- **ΔULI** — whether unique leverage is strengthening, flat, or eroding
- **ΔUFI** — whether fragility is rising, flat, or falling

Influence collapses in history are almost always preceded by:

- rising UFIʳ
- rising ΔUFI
- often with still-high ULIʳ

The model is designed to flag this pattern early.

---

## 5. Shocks and Stress Testing

The engine does not only compute scores; it also applies **stress** via
scenarios (e.g. financial, security, technological shocks).

Shocks:

- do not change BIS
- do change the internal fragility components
- can push high-UFIʳ states over critical thresholds

This allows the same country to be evaluated under:
- normal conditions, and
- stressed conditions

using the same logic.

---

## 6. Design Philosophy

- **Theory-first, data-constrained**  
  The model uses data as input and constraint, not as a black box.

- **Comparative and directional, not precise**  
  It is meant to rank and warn, not to time exact events.

- **Historically grounded**  
  Patterns are checked against major historical rises and declines.

- **Transparent**  
  All assumptions are explicit in code and documentation.

---

## 7. Intended Use

The Influence Risk Engine is designed for:

- researchers and analysts interested in structural geopolitics
- scenario planners and risk assessments
- comparative studies across states and time

It does **not** predict specific wars, elections, or crises.
It provides a structured way to reason about **where and how influence
is most likely to break**.
