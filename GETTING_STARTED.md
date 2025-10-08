# Getting Started Guide

Welcome to the CS206 Final Research Proposal repository. Follow the steps below to reproduce the main results and explore the documentation.

## 1. Clone & Install

```bash
git clone https://github.com/Johnnybyzhang/CS206-Final-Framework.git
cd CS206-Final-Framework
pip install -r requirements.txt
```

## 2. Regenerate Core Results

```bash
# Recreate the auction simulation panel and summary
python computational_scientist/scripts/auction_simulator.py --rounds 40 --seed 42

# Refresh all figures and transcript summaries
python visualizations/generate_figures.py
```

Outputs write to `computational_scientist/results/` and `visualizations/`.

## 3. Read the Deliverables

- [`README.md`](README.md): Project overview, navigation, and SDG alignment.  
- [`docs/Report.md`](docs/Report.md): Full proposal integrating Parts 1–3.  
- [`docs/FieldTripReflection.md`](docs/FieldTripReflection.md): Links field insights to methodology.

## 4. Explore Supporting Modules

| Folder | Highlights |
| --- | --- |
| `economist/` | Strategic model specification and welfare commentary. |
| `computational_scientist/` | Monte Carlo engine (`scripts/auction_simulator.py`) and outputs. |
| `behavioral_scientist/` | Behavioural triangulation notes connecting simulations to transcripts. |
| `mechanism_design/` | Auction/voting artefacts, including UNSC quadratic voting transcripts. |
| `visualizations/` | Generated PNGs and JSON summaries used in the report. |

## 5. Extend the Project

- Adjust `--common-value-weight` in the simulator to explore private vs. common-value environments.  
- Modify `BidderState` strategies to test alternative behavioural assumptions.  
- Parse additional transcripts or add field data to `behavioral_scientist/triangulation.md`.

For questions or future collaborators, add issues or pull requests referencing the relevant module.
