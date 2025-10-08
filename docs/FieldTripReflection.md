# Field Trip Reflection – Innovation Hubs & Mechanism Design

**Author**: Boyan Zhang  
**Course**: COMSCI/ECON 206 – Computational Microeconomics  
**Instructor**: Prof. Luyao Zhang  
**Date**: October 2025

---

## Executive Summary

The cohort visited three innovation hubs in Shanghai and Suzhou: a fintech sandbox devoted to digital payments, a civic technology lab prototyping participatory budgeting tools, and a startup accelerator experimenting with AI governance. Each stop highlighted the importance of incentive alignment, transparency, and responsible data use—principles that now permeate my final research proposal on budget-constrained auctions and quadratic voting.

---

## Field Trip Overview

### 1. Pudong Fintech Sandbox (Shanghai)
- **Date**: 12 September 2025  
- **Focus**: Digital payment infrastructure and auction-based advertising exchanges.  
- **Key Speakers**: Dr. Lin Qiu (Lead Economist), Ms. Yan Li (Platform Engineer).

**Observation**: The sandbox operates a continuous auction for ad placements where start-ups bid using limited marketing credits. Engineers described how budget exhaustion triggers sharp drops in market liquidity.

**Connection to Course Material**:
- Mirrors the strategic foundations of repeated second-price auctions.  
- Reinforced the need to model budget constraints explicitly, motivating the SPNE analysis in [`../mechanism_design/auctions`](../mechanism_design/auctions).  
- Demonstrated how fairness metrics (exposure equity) parallel the envy diagnostics in [`../economist/auction_game.md`](../economist/auction_game.md).

### 2. Suzhou Civic Tech Lab
- **Date**: 19 September 2025  
- **Focus**: Participatory budgeting for neighbourhood improvements.  
- **Key Speakers**: Ms. Hui Zhang (Program Director), Prof. Marco Rossi (Visiting Scholar).

**Observation**: Citizens received “voice credits” to allocate across proposals. Staff emphasised the challenge of eliciting intensity without overwhelming voters.

**Connection to Course Material**:
- Inspired the hybrid quadratic voting mechanism formalised in Part 3 of [`Report.md`](Report.md).  
- Provided empirical grounding for the transparency dashboard highlighted in the report.
- Highlighted SDG 16 by showing how inclusive institutions cultivate trust.

### 3. Kunshan AI Governance Accelerator
- **Date**: 26 September 2025  
- **Focus**: LLM safety audits and automated contract enforcement.  
- **Key Speakers**: Dr. Meilin Chen (Policy Lead), Mr. Raj Patel (Product Manager).

**Observation**: Teams compared human oversight with AI agents when auditing smart contracts. Budgeted time slots for reviewers resembled scarce credits in auctions.

**Connection to Course Material**:
- Motivated the bounded-optimist and cautious-conserver heuristics described in [`../behavioral_scientist/triangulation.md`](../behavioral_scientist/triangulation.md).  
- Reinforced SDG 9 (innovation) and SDG 17 (cross-disciplinary collaboration).

---

## Methodological Insights

1. **Liquidity Frictions** – The fintech sandbox confirmed that liquidity droughts occur abruptly. I therefore modelled budget exhaustion explicitly in the simulator and reported the 22.5% efficiency rate documented in [`../computational_scientist/results/auction_summary.json`](../computational_scientist/results/auction_summary.json).
2. **Voice Credit Calibration** – Civic technologists recommended gradual budget refills to maintain engagement, inspiring the adaptive refill experiment proposed in Part 2.
3. **Explainability** – AI governance practitioners insisted on audit trails, motivating the blockchain audit layer in the voting mechanism prototype.

---

## Societal Impact & SDGs

- **SDG 4 (Quality Education)**: Translating field experiences into reproducible code and visualisations created open resources for future cohorts.  
- **SDG 9 (Industry, Innovation, and Infrastructure)**: The simulation engine now mirrors real fintech constraints, enabling startups to benchmark mechanism tweaks.  
- **SDG 16 (Peace, Justice, and Strong Institutions)**: The voting mechanism explicitly tackles legitimacy gaps observed in participatory budgeting.  
- **SDG 17 (Partnerships for the Goals)**: Collaboration with lab staff and classmates shaped both the simulation parameters and the ethical framing of the report.

---

## Personal Growth

- **Technical**: Improved my ability to translate qualitative observations into parameterised simulations and data visualisations.  
- **Analytical**: Learned to triangulate between theory, behavioural evidence, and policy context.  
- **Professional**: Practiced stakeholder interviews, ethical reflection, and collaborative documentation workflows—all reflected in the reproducibility assets of this repository.

These lessons ensured the final proposal is not only theoretically rigorous but also anchored in the real institutional challenges highlighted during the field trip.
