# Computational Scientist - Implementation & Simulation

This folder contains all computational implementations, Python scripts, Jupyter notebooks, and solver outputs for game theory and mechanism design analysis.

## Contents

### Equilibrium Solvers
- Nash equilibrium computation using NashPy and QuantEcon
- Support enumeration algorithms
- Lemke-Howson algorithm implementation
- Bayesian game solvers

### Simulation Tools
- Monte Carlo simulations for strategy testing
- Agent-based modeling frameworks
- LLM integration for AI player behavior
- Comparative analysis tools

### Data Analysis
- Experimental data processing
- Statistical analysis of outcomes
- Visualization generation
- Results validation

## File Structure

```
computational_scientist/
├── notebooks/
│   ├── equilibrium_analysis.ipynb      # Interactive equilibrium computation
│   ├── simulation_experiments.ipynb    # Simulation design and execution
│   └── data_analysis.ipynb             # Results analysis and visualization
├── scripts/
│   ├── equilibrium_solver.py           # Nash/SPNE/Bayes-Nash solvers
│   ├── game_simulator.py               # Game simulation framework
│   ├── llm_agent.py                    # LLM player implementation
│   └── utils.py                        # Utility functions
├── results/
│   ├── equilibria/                     # Computed equilibrium outputs
│   ├── simulations/                    # Simulation results
│   └── comparisons/                    # Human vs AI comparisons
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## Setup and Installation

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install numpy pandas matplotlib scipy
pip install nashpy quantecon
pip install jupyter jupyterlab
pip install networkx  # For game tree visualization
pip install openai    # For LLM integration (if applicable)
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Computing Nash Equilibria

```python
from scripts.equilibrium_solver import NashSolver
import numpy as np

# Define payoff matrices
payoff_A = np.array([[3, 0], [5, 1]])
payoff_B = np.array([[3, 5], [0, 1]])

# Solve for Nash equilibria
solver = NashSolver(payoff_A, payoff_B)
equilibria = solver.find_all_equilibria()
print(f"Nash equilibria: {equilibria}")
```

### Running Simulations

```python
from scripts.game_simulator import GameSimulator

# Initialize simulator
sim = GameSimulator(game_type="prisoner_dilemma")

# Run simulations
results = sim.run(num_rounds=1000, player_types=["rational", "llm"])

# Analyze results
sim.analyze_results(results)
```

### Using Jupyter Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Open notebooks/equilibrium_analysis.ipynb
# Follow the interactive analysis workflow
```

## Methodology

### Equilibrium Computation
1. **Support Enumeration**: Systematically check all possible strategy supports
2. **Lemke-Howson**: Efficient algorithm for two-player games
3. **Best Response Dynamics**: Iterative convergence to equilibrium
4. **Backward Induction**: For extensive-form games

### Simulation Protocol
1. Define game parameters and player types
2. Initialize agents (human, rational AI, LLM-based)
3. Run repeated games with various treatments
4. Record decisions and outcomes
5. Compare to theoretical predictions

### LLM Integration
- Use GPT-4 or similar models as strategic players
- Prompt engineering for game-theoretic reasoning
- Compare LLM strategies to Nash equilibria
- Analyze bounded rationality patterns

## Key Results

### Equilibrium Analysis
- All computed Nash equilibria (pure and mixed)
- Comparison with analytical solutions
- Convergence analysis

### Simulation Outcomes
- Frequency of equilibrium play
- Deviations from theoretical predictions
- Learning and adaptation patterns

### Human vs AI Performance
- Strategy distribution comparisons
- Payoff differential analysis
- Behavioral patterns and biases

## Integration with Other Components

- **Economist**: Implements theoretical models computationally
- **Behavioral Scientist**: Provides data for validation against experiments
- **Mechanism Designer**: Simulates proposed mechanisms
- **Visualizations**: Generates all figures and diagrams

## Tools and Libraries

### Core Libraries
- **NumPy**: Numerical computation
- **NashPy**: Game theory and Nash equilibrium computation
- **QuantEcon**: Economic modeling and dynamic programming
- **NetworkX**: Game tree visualization

### Experimental Tools
- **Game Theory Explorer (GTE)**: Extensive-form analysis
- **Gambit**: Game theory analysis software (optional)

### AI Integration
- **OpenAI API**: LLM-based agents
- **Transformers**: Local LLM deployment (optional)

## References

- [NashPy Documentation](https://nashpy.readthedocs.io/)
- [QuantEcon Documentation](https://quantecon.org/)
- [Game Theory Explorer](http://www.gametheoryexplorer.org/)

---

*For theoretical foundations, see [`../economist/`](../economist/)*  
*For experimental validation, see [`../behavioral_scientist/`](../behavioral_scientist/)*
