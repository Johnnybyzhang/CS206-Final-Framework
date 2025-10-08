# Behavioral Scientist – Experiments & Triangulation

The behavioural track documents how human and AI agents react to the budget-constrained auction and the institutional prompts used in the quadratic-voting exercise. Instead of synthetic placeholders, this folder now provides analytical notes that connect the simulator outputs with the transcript evidence.

## Files

| File | Description |
| --- | --- |
| [`triangulation.md`](triangulation.md) | Summarises behavioural signatures observed in the oTree pilot and LLM transcripts. |

## Highlights

- Encodes the heuristics (bounded optimism, cautious conservation) that drive deviations from Nash equilibrium in the simulation.
- Extracts option frequencies from the UNSC quadratic-voting transcripts to motivate the legitimacy safeguards proposed in Part 3 of the report.
- Links behavioural insights to design recommendations such as adaptive budget refills and transparency dashboards.

For computational replications, see [`../computational_scientist/scripts/auction_simulator.py`](../computational_scientist/scripts/auction_simulator.py). For the theoretical framing, consult [`../economist/auction_game.md`](../economist/auction_game.md).
