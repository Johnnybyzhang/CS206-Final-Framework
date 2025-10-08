# Economist – Theoretical Foundations

This module captures the analytical groundwork that anchors the simulations and behavioural evidence. The centrepiece is the repeated budget-constrained second-price auction that threads through Parts 1 and 2 of the proposal.

## Key Files

| File | Purpose |
| --- | --- |
| [`auction_game.md`](auction_game.md) | Defines players, strategy spaces, equilibrium benchmarks, and welfare diagnostics. |
| [`../computational_scientist/results/auction_rounds.csv`](../computational_scientist/results/auction_rounds.csv) | Provides empirical checks for the theoretical predictions (efficiency, budgets, winner's-curse notes). |

## Highlights

- Formalises the SPNE benchmark where truthful bidding survives repeated interaction when budgets are slack.
- Identifies how bounded optimism introduces deviations consistent with the winner's curse, motivating mechanism tweaks.
- Supplies comparative statics (budget refresh, higher common-value weight) that inform the design recommendations in the final report.

For behavioural triangulation, continue to [`../behavioral_scientist/triangulation.md`](../behavioral_scientist/triangulation.md); for implementation details, see [`../computational_scientist/scripts/auction_simulator.py`](../computational_scientist/scripts/auction_simulator.py).
