# Play to Innovate: An Interdisciplinary Approach from Game Theory to Mechanism Design

## Abstract

This repository supports the final research proposal for COMSCI/ECON 206: Computational Microeconomics. The project synthesizes game theory foundations, mechanism design applications, and real-world institutional analysis to explore strategic interactions in economic systems. Building on Problem Set 1 (game theory foundations) and Problem Set 2 (mechanism design applications), this research frames original questions connecting economics and computation. The project formalizes strategic environments, implements computational tools (Python, NashPy, oTree), and compares theoretical predictions with human or AI-agent behavior, ultimately proposing innovative mechanisms that bridge classroom theory, Nobel frameworks, and experiential learning.

## Authors and Roles

- **[Author Name]** - Project Lead
  - **Economist**: Theoretical analysis, game theory modeling, welfare and fairness evaluation
  - **Computational Scientist**: Python implementation, equilibrium computation, simulation design
  - **Behavioral Scientist**: Experimental design, oTree implementation, human vs. AI comparison
  - **Mechanism Designer**: Auction/voting mechanism design, institutional innovation

## Disclaimer

This repository supports the final research proposal submitted to COMSCI/ECON 206: Computational Microeconomics, instructed by Prof. Luyao Zhang at Duke Kunshan University in Autumn 2025.

## Acknowledgments

We express our sincere gratitude to:
- **Prof. Luyao Zhang** for exceptional instruction and guidance throughout COMSCI/ECON 206
- **Classmates and Peers** for constructive feedback, collaborative learning experiences, and engaging discussions
- **Open-Source Communities**: NashPy, QuantEcon, Game Theory Explorer (GTE), oTree, and Python scientific computing ecosystem
- **AI Tools**: LLMs and computational assistants that supported research and development
- **Duke Kunshan University** for providing an inspiring interdisciplinary learning environment

## Statement of Intellectual and Professional Growth

This project represents a significant milestone in our intellectual and professional development. Through the integration of Problem Set 1 (game theory foundations) and Problem Set 2 (mechanism design applications), we have:

**Intellectual Growth:**
- Mastered equilibrium concepts (Nash, SPNE, Bayes-Nash) and their computational implementation
- Developed rigorous research design skills connecting theory to empirical validation
- Enhanced interdisciplinary thinking by bridging economics, computer science, and behavioral analysis
- Deepened understanding of mechanism design principles and their real-world applications

**Professional Growth:**
- Strengthened technical skills in Python, game theory libraries (NashPy, QuantEcon), and experimental platforms (oTree)
- Improved collaborative abilities through peer feedback and team-based learning
- Cultivated ethical reflection on the societal impacts of economic mechanisms
- Enhanced communication skills through written reports, visualizations, and presentation preparation

The field trip to innovation hubs provided invaluable real-world context, inspiring our research questions and grounding theoretical concepts in practical applications. This experience has prepared us to apply computational microeconomics principles to address contemporary challenges in auctions, voting, blockchain governance, and sustainability.

## Table of Contents

- [Project Overview](#play-to-innovate-an-interdisciplinary-approach-from-game-theory-to-mechanism-design)
- [Repository Structure](#repository-structure)
- [Navigation Instructions](#navigation-instructions)
- [Part 1: Strategic Game Foundations](#part-1-strategic-game-foundations)
- [Part 2: Mechanism Design & Auctions](#part-2-mechanism-design--auctions)
- [Part 3: Voting & Institutions](#part-3-voting--institutions)
- [Documentation](#documentation)
- [How to Use This Repository](#how-to-use-this-repository)
- [Media](#media)

## Repository Structure

```
CS206-Final-Framework/
├── economist/                      # Theoretical analysis (game theory, welfare, fairness)
│   └── README.md                   # Guide to theoretical models and analysis
├── computational_scientist/        # Python scripts, Jupyter notebooks, solver outputs
│   └── README.md                   # Guide to computational implementations
├── behavioral_scientist/           # oTree apps, human experiment results, LLM transcripts
│   └── README.md                   # Guide to behavioral experiments
├── mechanism_design/               # Auction/voting design
│   └── README.md                   # Guide to mechanism design proposals
├── visualizations/                 # Figures, payoff matrices, equilibrium diagrams, voting charts
│   └── README.md                   # Guide to visual outputs
├── docs/                           # Project documentation
│   ├── Report.pdf                  # Final research proposal report
│   ├── Poster.pdf                  # Symposium presentation poster
│   └── FieldTripReflection.md      # Reflection linking field experience to methodology
└── README.md                       # This file - project overview and navigation
```

## Navigation Instructions

### For Reviewers and Evaluators

1. **Start Here**: Read this README for project overview and context
2. **Theoretical Analysis**: Navigate to [`economist/`](./economist/) for game theory models and equilibrium analysis
3. **Computational Implementation**: Visit [`computational_scientist/`](./computational_scientist/) for Python code, notebooks, and solver outputs
4. **Behavioral Experiments**: Explore [`behavioral_scientist/`](./behavioral_scientist/) for oTree applications and experiment results
5. **Mechanism Design**: Review [`mechanism_design/`](./mechanism_design/) for auction/voting mechanism proposals
6. **Visual Results**: Check [`visualizations/`](./visualizations/) for figures, diagrams, and charts
7. **Final Documentation**: Access [`docs/`](./docs/) for the complete report, poster, and field trip reflection

### Key Files and Locations

- **Equilibria Computation**: `computational_scientist/equilibrium_solver.py` and related notebooks
- **Mechanism Design Code**: `mechanism_design/auction_simulator.py` and `mechanism_design/voting_system.py`
- **Simulation Outputs**: `computational_scientist/results/` and `behavioral_scientist/data/`
- **Visualizations**: `visualizations/*.png` and `visualizations/*.pdf`
- **Final Report**: `docs/Report.pdf`
- **Symposium Poster**: `docs/Poster.pdf`
- **Field Trip Reflection**: `docs/FieldTripReflection.md`

## Part 1: Strategic Game Foundations

**Objective**: Formalize a strategic game, identify equilibrium concepts (Nash, SPNE, Bayes-Nash, etc.), and evaluate efficiency and fairness.

**Methods**:
- Use NashPy/QuantEcon for equilibrium computation
- Deploy Game Theory Explorer (GTE) for extensive-form analysis
- Conduct oTree sessions with classmates and compare to LLM play

**Output**: Theoretical solutions, computational results, and comparative analysis of equilibrium predictions vs. human/AI outcomes.

**Location**: See [`economist/`](./economist/) for theoretical models and [`computational_scientist/`](./computational_scientist/) for implementations.

## Part 2: Mechanism Design & Auctions

**Objective**: Extend game-theoretic foundations into mechanism design by analyzing the winner's curse and testing human vs. AI strategies.

**Methods**:
- Select an auction format (first-price, common-value, etc.)
- Design treatments and controls to test bounded rationality
- Run simulations with LLMs and compare to theoretical predictions and behavioral evidence

**Output**: Revised and extended analysis from PS1, auction experiments, and mechanism design insights.

**Location**: See [`mechanism_design/`](./mechanism_design/) for auction designs and [`behavioral_scientist/`](./behavioral_scientist/) for experimental results.

## Part 3: Voting & Institutions

**Objective**: Connect theory to practice by designing a simplified voting issue inspired by real-world cases or field trip observations.

**Methods**:
- Apply Nobel insights: Arrow's impossibility, Buchanan on institutions, Hurwicz-Maskin-Myerson on mechanism design, Shapley-Roth on matching, and Acemoglu-Johnson-Robinson on legitimacy
- Propose an innovative or hybrid voting rule, integrating computation (e.g., blockchain consensus, reinforcement learning, algorithmic matching)
- Test designs through classroom simulations, coding, or prototype implementation

**Output**: Forward-looking mechanism design proposal, bridging classroom theory, Nobel frameworks, and experiential learning.

**Location**: See [`mechanism_design/voting/`](./mechanism_design/) for voting system proposals and [`docs/FieldTripReflection.md`](./docs/FieldTripReflection.md) for real-world connections.

## Documentation

All project documentation is located in the [`docs/`](./docs/) folder:

- **[Final Report](./docs/Report.pdf)**: Complete research proposal with theoretical analysis, computational results, and mechanism design proposals
- **[Symposium Poster](./docs/Poster.pdf)**: Visual summary of the project for presentation
- **[Field Trip Reflection](./docs/FieldTripReflection.md)**: Personal reflection connecting field experiences to research methodology and societal impacts

## How to Use This Repository

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Required packages
pip install numpy pandas matplotlib nashpy quantecon jupyterlab
```

### Running the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Johnnybyzhang/CS206-Final-Framework.git
   cd CS206-Final-Framework
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt  # If available
   ```

3. **Explore computational notebooks**:
   ```bash
   cd computational_scientist
   jupyter lab
   ```

4. **Run equilibrium solvers**:
   ```bash
   cd computational_scientist
   python equilibrium_solver.py
   ```

5. **Access oTree experiments**:
   ```bash
   cd behavioral_scientist
   otree devserver
   ```

### Reproducing Results

All results are reproducible by following the instructions in each subfolder's README. Key steps:

1. Review theoretical models in `economist/`
2. Run computational scripts in `computational_scientist/`
3. Analyze experimental data in `behavioral_scientist/`
4. Examine mechanism designs in `mechanism_design/`
5. View generated visualizations in `visualizations/`

## Media

### Project Poster

![Project Poster](./docs/Poster.pdf)

*Symposium poster summarizing the research project*

### Demo Video

[Demo Video - Coming Soon](#)

*Video demonstration of computational tools and experimental platforms*

---

## Contribution to Sustainable Development Goals (SDGs)

This research contributes to the following United Nations Sustainable Development Goals:

- **SDG 4: Quality Education** - Advancing educational methods through interactive game theory and mechanism design
- **SDG 9: Industry, Innovation, and Infrastructure** - Developing innovative computational tools for economic mechanism design
- **SDG 16: Peace, Justice, and Strong Institutions** - Improving institutional design through voting mechanisms and fair allocation systems
- **SDG 17: Partnerships for the Goals** - Fostering interdisciplinary collaboration between economics, computer science, and behavioral science

---

## License

This project is created for educational purposes as part of COMSCI/ECON 206 at Duke Kunshan University.

## Contact

For questions or collaborations, please contact [Author Email].

---

*Last Updated: October 2025*
