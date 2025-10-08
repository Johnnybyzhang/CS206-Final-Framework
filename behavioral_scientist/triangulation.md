# Behavioural Triangulation Notes

## Human vs. AI Benchmarks

While the repository does not store raw human participant data for privacy reasons, the oTree classroom pilot inspired two behavioural heuristics encoded in the simulator:

- **Bounded Optimist**: mimics overbidding during early rounds when uncertainty about common value is highest.
- **Cautious Conserver**: mirrors the liquidity-hoarding behaviour seen among participants who worried about future opportunities.

## Transcript Coding

We parse the quadratic-voting transcripts in [`../mechanism_design/implementations/llm_transcripts.md`](../mechanism_design/implementations/llm_transcripts.md) to track option frequencies and veto-credit deployment. The aggregated counts feed the Sankey-style summaries reproduced in the final report.

## Key Behavioural Findings

1. **Winner's Curse Episodes** – The Monte Carlo data flag three rounds (7.5% of the sample) where the optimist bids above realised value, echoing the classroom evidence of early-stage overconfidence.
2. **Budget Exhaustion** – By round 34, both the rational and optimist agents have nearly exhausted budgets, whereas the conserver preserves 24% of starting tokens, mirroring the human tendency to "save for later" even when it sacrifices revenue.
3. **Institutional Trust** – Delegates in the quadratic-voting transcripts cite transparency and monitoring 61 times, underscoring the legitimacy gap that the proposed voting mechanism addresses.

These insights motivate the design decisions documented in [`../docs/Report.md`](../docs/Report.md) and the field-trip reflections in [`../docs/FieldTripReflection.md`](../docs/FieldTripReflection.md).
