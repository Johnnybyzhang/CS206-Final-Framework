# Computational Scientist – Simulation & Data Products

This folder curates the code and datasets that reproduce the quantitative findings of the final proposal. The simulations focus on the repeated budget-constrained second-price auction introduced in Part 1 and extended in Part 2 of the report. Outputs feed directly into the figures in [`../visualizations`](../visualizations) and the narrative evidence in [`../docs/Report.md`](../docs/Report.md).

## Contents

```text
computational_scientist/
├── scripts/
│   └── auction_simulator.py      # Monte Carlo engine for budgeted second-price auctions
├── results/
│   ├── auction_rounds.csv        # Round-level panel with bids, winners, and budget updates
│   └── auction_summary.json      # Aggregated KPIs (revenue, efficiency, winner's-curse rate)
└── README.md
```

## Running the Simulation

```bash
python scripts/auction_simulator.py --rounds 40 --seed 42
```

The command prints a JSON summary and refreshes the artefacts under `results/`. Adjust `--common-value-weight` to switch between purely private values (`0.0`) and richer common-value exposure (`0.25` by default).

## Key Metrics Captured

| Metric | Description |
| --- | --- |
| `mean_revenue` | Average seller revenue across rounds, highlighting the budget squeeze over time. |
| `efficiency_rate` | Share of rounds in which the highest-value bidder wins despite budget constraints. |
| `winner_curse_frequency` | Frequency with which the bounded-optimist agent bids above realised value. |
| `final_budgets` | Remaining budgets for recent winners, used to diagnose exhaustion dynamics. |

The round-level CSV supports stratified analysis (e.g., rational vs. bounded agents), while the JSON summary powers dashboard-like quick checks in the README and report.

## Extending the Engine

- **Alternative mechanisms**: Swap out the pricing rule inside `auction_simulator.py` to explore first-price or all-pay variants.
- **Behavioural toggles**: Modify the `bid` methods to encode risk aversion, regret minimisation, or reinforcement-learning heuristics.
- **LLM integration**: Use the Monte Carlo scaffolding to replay the quadratic-voting transcripts as agent prompts for comparison with human-inspired heuristics.

For analytical derivations that motivate these simulations, see [`../economist/auction_game.md`](../economist/auction_game.md). For behavioural interpretation, consult [`../behavioral_scientist/triangulation.md`](../behavioral_scientist/triangulation.md).
