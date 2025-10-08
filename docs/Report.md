# Play to Innovate: An Interdisciplinary Approach from Game Theory to Mechanism Design

**Author**: Boyan Zhang  
**Course**: COMSCI/ECON 206 – Computational Microeconomics (Autumn 2025)  
**Instructor**: Prof. Luyao Zhang  
**Submission Date**: 15 October 2025

> **Contribution to Sustainable Development Goals**: SDG 4 (Quality Education), SDG 9 (Industry, Innovation, and Infrastructure), SDG 16 (Peace, Justice, and Strong Institutions), SDG 17 (Partnerships for the Goals).
>
> **Acknowledgments**: I thank Prof. Luyao Zhang, my classmates for collaborative feedback, and open-source communities such as NashPy, QuantEcon, oTree, and the maintainers of pandas/matplotlib for their tooling support.
>
> **Disclaimer**: This project is the final research proposal submitted to STATS 201: Machine Learning for Social Science, instructed by Prof. Luyao Zhang at Duke Kunshan University in Autumn 2025.
>
> **Statement of Intellectual and Professional Growth**: Across PS1 and PS2 I deepened my command of equilibrium concepts, Monte Carlo experimentation, and mechanism design. Professionally I strengthened reproducible coding practices, interdisciplinary communication, and ethical reflection on algorithmic governance.

---

## Abstract

We investigate a repeated budget-constrained second-price auction that models digital advertising exchanges observed during the course field trip. Computational experiments compare rational, bounded-optimist, and cautious-conserver bidding heuristics to document winner's-curse deviations and liquidity shocks. The analysis informs an adaptive mechanism that replenishes budgets and introduces transparency dashboards. Building on Week 6 reflections, we design a quadratic-voting-inspired institutional prototype that encodes lessons from UNSC transcripts and participatory budgeting pilots.

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Part 1 – Strategic Game Foundations](#part-1--strategic-game-foundations)  
3. [Part 2 – Mechanism Design & Auctions](#part-2--mechanism-design--auctions)  
4. [Part 3 – Voting & Institutions](#part-3--voting--institutions)  
5. [Implementation & Reproducibility](#implementation--reproducibility)  
6. [Conclusion](#conclusion)  
7. [References](#references)

---

## Introduction

Digital marketplaces frequently ration scarce attention using auctions while constraining bidder budgets. Observations from Shanghai's fintech sandbox revealed revenue collapses once start-up credits depleted. This proposal formalises the environment, validates predictions via simulation, and extends the findings to institutional design challenges, linking computational microeconomics to sustainable development goals.

---

## Part 1 – Strategic Game Foundations

### Game Specification

- Strategic environment formalised in [`../economist/auction_game.md`](../economist/auction_game.md).  
- Three bidding types, shared common-value shock, repeated horizon of 40 rounds.  
- Equilibrium benchmark: truthful bidding remains subgame-perfect with ample budgets.

### Key Results

- Simulation output [`auction_rounds.csv`](../computational_scientist/results/auction_rounds.csv) records round-level allocations, confirming frequent binding budgets.  
- Mean revenue: 1.35 tokens; efficiency rate: 0.225 (`auction_summary.json`).  
- Winner's-curse events occur in 3 rounds (7.5%), matching the bounded optimism narrative from PS1 reflections.

### Visual Evidence

- Revenue decay visualised in `visualizations/auctions/revenue_by_round.png`.  
- Early-round deviations summarised in `visualizations/auctions/winners_curse_frequency.png`.

These findings mirror PS1 proofs while adding empirical realism through Monte Carlo evidence.

---

## Part 2 – Mechanism Design & Auctions

### Research Questions

1. How do bounded-rational heuristics affect revenue and efficiency under budget constraints?  
2. Can adaptive budget policies mitigate winner's-curse behaviour without sacrificing fairness?

### Methods

- Extended simulator supports counterfactuals: adjusting `--common-value-weight` and proposed budget refills.  
- LLM transcript analysis (via `visualizations/voting/decision_summary.json`) informs narrative comparisons with human-inspired strategies.  
- Field trip insights guide the design of transparency dashboards and trigger conditions for budget replenishment.

### Findings

- Higher common-value weight amplifies overbidding, draining optimist budgets by round 30.  
- Introducing a 20% budget top-up every ten rounds raises efficiency above 0.6 (experiments documented in code comments).  
- Seller revenue stabilises when transparency alerts prompt conservative bidding by the bounded type.

### Design Recommendations

- Publish real-time budget health indicators to discourage reckless bids.  
- Apply adaptive refills conditioned on aggregate liquidity to maintain competitive pressure.  
- Provide post-round explainability summaries to align with SDG 16 accountability goals.

---

## Part 3 – Voting & Institutions

### Motivation

Week 6 reflections and UNSC quadratic-voting transcripts exposed legitimacy gaps: high-credit delegates tend to veto while low-credit delegates abstain. Participatory budgeting labs emphasised the need for transparency and intensity expression.

### Proposed Mechanism

1. **Voice Credits**: Participants receive quadratic voice credits that replenish partially when engagement drops below a threshold.  
2. **Transparency Ledger**: Votes recorded on a permissioned blockchain with real-time dashboards summarising credit usage.  
3. **Issue Matching**: Participants opt into issue clusters; matching algorithms prioritise voters with expertise, echoing Shapley-Roth matching ideas.

### Expected Properties

- Relaxing independence of irrelevant alternatives allows intensity expression while respecting constitutional constraints (Buchanan & Tullock).  
- Transparency ledger mitigates Arrow-style legitimacy concerns by documenting trade-offs.  
- Field trip insights confirm stakeholders value explainability, aligning with SDG 16.

### Evidence

- Heatmap `visualizations/voting/credit_option_heatmap.png` shows high-credit veto clustering, motivating adaptive safeguards.  
- Transcript summary `decision_summary.json` reveals 23 of 53 approvals come from low-credit delegates, highlighting participation asymmetries.

---

## Implementation & Reproducibility

- **Simulation**: `python computational_scientist/scripts/auction_simulator.py --rounds 40 --seed 42`.  
- **Figures**: `python visualizations/generate_figures.py`.  
- **Transcripts**: Stored under `mechanism_design/implementations/llm_transcripts.md`.  
- **Behavioural Notes**: `behavioral_scientist/triangulation.md`.  
- **Field Trip Context**: `docs/FieldTripReflection.md`.

All commands were run on Python 3.12.10 with dependencies listed in `requirements.txt`.

---

## Conclusion

The proposal demonstrates how strategic analysis, simulation, and institutional design reinforce one another. Budget constraints and bounded rationality materially erode auction efficiency, but adaptive mechanisms informed by field evidence can restore performance. Extending the logic to voting institutions yields a credible blueprint for more legitimate decision-making processes aligned with global development goals.

---

## References

- Vickrey, W. (1961). Counterspeculation, Auctions, and Competitive Sealed Tenders. *Journal of Finance*, 16(1), 8–37.  
- Krishna, V. (2009). *Auction Theory* (2nd ed.). Academic Press.  
- Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press.  
- Knight, V. A., & Campbell, J. D. (2018). Nashpy: A Python library for the computation of equilibria of 2-player strategic games. *JOSS*, 3(24), 615.  
- Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree – An open-source platform for laboratory, online, and field experiments. *JBEF*, 9, 88–97.  
- Arrow, K. J. (1951). *Social Choice and Individual Values*.  
- Buchanan, J. M., & Tullock, G. (1962). *The Calculus of Consent*.  
- Hurwicz, L., Maskin, E., & Myerson, R. (2007). Nobel Lectures in Economic Sciences.  
- Shapley, L. S., & Roth, A. E. (2012). Nobel Lectures in Economic Sciences.  
- Acemoglu, D., & Robinson, J. A. (2012). *Why Nations Fail*.  
- UNESCO (2021). *Recommendation on the Ethics of Artificial Intelligence*.  
- National Institute of Standards and Technology (2023). *AI Risk Management Framework*.
