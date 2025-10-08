# Repository Structure Overview

## Visual Directory Tree

```
CS206-Final-Framework/
│
├── 📄 README.md                          # Main project overview and navigation
├── 📄 GETTING_STARTED.md                 # Step-by-step guide for students
├── 📄 requirements.txt                   # Python dependencies
├── 📄 .gitignore                         # Files to exclude from git
│
├── 📊 economist/                         # THEORETICAL ANALYSIS
│   ├── 📄 README.md                      # Guide to theoretical work
│   ├── 📁 models/                        # Game formalizations
│   ├── 📁 equilibria/                    # Equilibrium analyses
│   └── 📁 welfare/                       # Efficiency & fairness
│
├── 💻 computational_scientist/           # IMPLEMENTATION & SIMULATION
│   ├── 📄 README.md                      # Guide to computational work
│   ├── 📁 notebooks/                     # Jupyter notebooks
│   │   ├── equilibrium_analysis.ipynb
│   │   ├── simulation_experiments.ipynb
│   │   └── data_analysis.ipynb
│   ├── 📁 scripts/                       # Python scripts
│   │   ├── equilibrium_solver.py
│   │   ├── game_simulator.py
│   │   ├── llm_agent.py
│   │   └── utils.py
│   └── 📁 results/                       # Computation outputs
│       ├── equilibria/
│       ├── simulations/
│       └── comparisons/
│
├── 🧪 behavioral_scientist/              # EXPERIMENTS & DATA
│   ├── 📄 README.md                      # Guide to experimental work
│   ├── 📁 otree_apps/                    # oTree applications
│   │   ├── strategic_game/
│   │   ├── auction_experiment/
│   │   └── voting_mechanism/
│   ├── 📁 data/                          # Experimental data
│   │   ├── human_experiments/
│   │   │   ├── raw/
│   │   │   ├── processed/
│   │   │   └── codebook.md
│   │   └── ai_experiments/
│   │       ├── llm_transcripts/
│   │       └── ai_strategies.csv
│   ├── 📁 analysis/                      # Data analysis notebooks
│   │   ├── descriptive_stats.ipynb
│   │   ├── behavioral_patterns.ipynb
│   │   └── human_vs_ai.ipynb
│   └── 📁 protocols/                     # Experiment documentation
│       ├── experiment_protocol.md
│       ├── instructions.md
│       └── consent_form.md
│
├── ⚙️ mechanism_design/                   # MECHANISM INNOVATION
│   ├── 📄 README.md                      # Guide to mechanism design
│   ├── 📁 auctions/                      # Auction mechanisms
│   │   ├── first_price_auction.md
│   │   ├── vickrey_auction.md
│   │   ├── common_value_auction.md
│   │   ├── budgeted_mechanism.md
│   │   └── winners_curse_analysis.md
│   ├── 📁 voting/                        # Voting mechanisms
│   │   ├── classical_rules.md
│   │   ├── strategic_voting.md
│   │   ├── novel_mechanisms.md
│   │   └── blockchain_governance.md
│   ├── 📁 implementations/               # Mechanism code
│   │   ├── auction_simulator.py
│   │   ├── voting_system.py
│   │   └── mechanism_evaluator.py
│   └── 📁 case_studies/                  # Real-world connections
│       ├── field_trip_inspiration.md
│       ├── nobel_insights.md
│       └── practical_applications.md
│
├── 📈 visualizations/                     # FIGURES & CHARTS
│   ├── 📄 README.md                      # Guide to visualizations
│   ├── 📁 game_theory/                   # Game theory figures
│   │   ├── payoff_matrices/
│   │   ├── game_trees/
│   │   ├── equilibria/
│   │   └── best_response/
│   ├── 📁 auctions/                      # Auction visualizations
│   │   ├── bidding_strategies/
│   │   ├── revenue_comparison/
│   │   ├── winners_curse/
│   │   └── budget_effects/
│   ├── 📁 voting/                        # Voting visualizations
│   │   ├── preference_profiles/
│   │   ├── rule_comparisons/
│   │   ├── strategic_manipulation/
│   │   └── paradoxes/
│   ├── 📁 experiments/                   # Experimental results
│   │   ├── human_performance/
│   │   ├── ai_performance/
│   │   ├── comparisons/
│   │   └── learning_dynamics/
│   └── 📁 mechanisms/                    # Mechanism performance
│       ├── efficiency_plots/
│       ├── fairness_metrics/
│       └── revenue_analysis/
│
├── 📚 docs/                               # DOCUMENTATION
│   ├── 📄 README.md                      # Documentation guide
│   ├── 📄 Report.pdf                     # Final research report (to be created)
│   ├── 📄 Report_placeholder.md          # Instructions for report
│   └── 📄 FieldTripReflection.md         # Field trip reflection (template)
│
└── 📁 orig/                               # ORIGINAL COURSE MATERIALS
    └── cs206_week6_reflection_boyan_zhang.pdf
```

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         PROJECT WORKFLOW                         │
└─────────────────────────────────────────────────────────────────┘

Step 1: THEORY (economist/)
├── Formalize game
├── Define equilibria
└── Analyze welfare
    │
    ↓
Step 2: COMPUTATION (computational_scientist/)
├── Implement solvers
├── Run simulations
└── Generate data
    │
    ↓
Step 3: EXPERIMENTS (behavioral_scientist/)
├── Design oTree apps
├── Run human experiments
├── Run LLM experiments
└── Collect data
    │
    ↓
Step 4: MECHANISM DESIGN (mechanism_design/)
├── Design mechanisms
├── Analyze properties
└── Test implementations
    │
    ↓
Step 5: VISUALIZATION (visualizations/)
├── Create all figures
├── Generate charts
└── Export high-res images
    │
    ↓
Step 6: DOCUMENTATION (docs/)
├── Write report
└── Complete reflection
    │
    ↓
Step 7: INTEGRATION (README.md)
└── Update main README with project details
```

## Data Flow

```
┌──────────────┐
│  Theoretical │
│   Models     │ ────┐
└──────────────┘     │
                     │
┌──────────────┐     │     ┌──────────────┐
│ Computational│     ├────▶│Visualizations│
│   Solvers    │ ────┤     └──────────────┘
└──────────────┘     │              │
                     │              │
┌──────────────┐     │              │
│  Behavioral  │     │              ↓
│ Experiments  │ ────┘     ┌──────────────┐
└──────────────┘           │    Final     │
                           │    Report    │
┌──────────────┐           └──────────────┘
│  Mechanism   │                    ↑
│   Design     │ ───────────────────┘
└──────────────┘
```

## Integration Points

### 1. Economist ↔ Computational Scientist
- **Flow**: Theory → Implementation
- **Files**: Model definitions → Python code
- **Purpose**: Validate theoretical predictions computationally

### 2. Computational Scientist ↔ Behavioral Scientist
- **Flow**: Predictions → Experiments → Data
- **Files**: Equilibrium outputs → oTree apps → Experimental results
- **Purpose**: Compare theory to human/AI behavior

### 3. Behavioral Scientist ↔ Mechanism Designer
- **Flow**: Behavioral insights → Mechanism improvements
- **Files**: Bias patterns → Mechanism adjustments
- **Purpose**: Design better mechanisms based on real behavior

### 4. All Components ↔ Visualizations
- **Flow**: Results → Figures
- **Files**: Data/outputs → PNG/PDF images
- **Purpose**: Visual communication of findings

### 5. All Components ↔ Documentation
- **Flow**: All work → Report
- **Files**: Everything → docs/Report.pdf
- **Purpose**: Synthesize complete project narrative

## Part Structure (from PDF)

### Part 1: Strategic Game Foundations (PS1)
- **Primary Folders**: `economist/`, `computational_scientist/`, `behavioral_scientist/`
- **Key Outputs**: Equilibrium analysis, computational validation, human vs AI comparison

### Part 2: Mechanism Design & Auctions (PS2)
- **Primary Folders**: `mechanism_design/auctions/`, `behavioral_scientist/`
- **Key Outputs**: Auction experiments, winner's curse analysis, LLM comparisons

### Part 3: Voting & Institutions (Week 6)
- **Primary Folders**: `mechanism_design/voting/`, `docs/FieldTripReflection.md`
- **Key Outputs**: Novel voting mechanisms, field trip connections, Nobel insights

## Roles and Responsibilities

If working in teams, you can divide roles:

```
┌──────────────────┬─────────────────────────────────────┐
│      Role        │        Primary Folders              │
├──────────────────┼─────────────────────────────────────┤
│ Economist        │ economist/                          │
│                  │ mechanism_design/ (theory)          │
├──────────────────┼─────────────────────────────────────┤
│ Computational    │ computational_scientist/            │
│ Scientist        │ visualizations/                     │
├──────────────────┼─────────────────────────────────────┤
│ Behavioral       │ behavioral_scientist/               │
│ Scientist        │ mechanism_design/ (experiments)     │
├──────────────────┼─────────────────────────────────────┤
│ Mechanism        │ mechanism_design/                   │
│ Designer         │ All folders (integration)           │
├──────────────────┼─────────────────────────────────────┤
│ All Team Members │ docs/ (everyone contributes)        │
└──────────────────┴─────────────────────────────────────┘
```

## File Naming Conventions

### Python Scripts
- `snake_case.py`
- Example: `equilibrium_solver.py`, `game_simulator.py`

### Jupyter Notebooks
- `descriptive_name.ipynb`
- Example: `equilibrium_analysis.ipynb`, `human_vs_ai_comparison.ipynb`

### Markdown Files
- `PascalCase.md` or `snake_case.md`
- Example: `FieldTripReflection.md`, `experiment_protocol.md`

### Visualizations
- `category_description_version.png`
- Example: `game_theory_prisoners_dilemma_v1.png`

### Data Files
- `descriptive_name.csv` or `.json`
- Example: `human_experiment_round1.csv`, `llm_responses.json`

## Version Control Best Practices

```bash
# Commit frequently with descriptive messages
git add .
git commit -m "Implement Nash equilibrium solver"

# Push regularly to backup work
git push origin main

# Use branches for major features
git checkout -b feature/voting-mechanism
# ... work on feature ...
git commit -m "Add quadratic voting mechanism"
git checkout main
git merge feature/voting-mechanism
```

## Key Deliverables Summary

1. ✅ **Repository Structure**: Complete (you are here!)
2. 📝 **Code & Analysis**: To be completed by student
3. 🔬 **Experiments**: To be completed by student
4. 📊 **Visualizations**: To be generated from results
5. 📄 **Report**: To be written
6. 💭 **Reflection**: To be completed

---

*This repository structure is based on the COMSCI/ECON 206 Final Research Proposal requirements as specified in the course PDF.*
