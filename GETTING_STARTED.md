# Getting Started Guide

Welcome to the CS206 Final Research Proposal Framework! This guide will help you navigate the repository and understand how to complete your project.

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Johnnybyzhang/CS206-Final-Framework.git
cd CS206-Final-Framework

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python -c "import nashpy, quantecon; print('Libraries installed successfully!')"
```

### 2. Understand the Structure

```
CS206-Final-Framework/
├── economist/                  # Your theoretical game theory work goes here
├── computational_scientist/    # Your Python code and Jupyter notebooks
├── behavioral_scientist/       # Your oTree experiments and data
├── mechanism_design/           # Your auction/voting mechanism designs
├── visualizations/            # Generated figures and charts
├── docs/                      # Final report, poster, and reflection
└── README.md                  # Main project overview (you are here!)
```

### 3. Work Through the Project

Follow these steps in order:

#### Phase 1: Strategic Game Foundations (PS1)
1. Go to `economist/` folder
2. Define your game formally (players, strategies, payoffs)
3. Go to `computational_scientist/` folder
4. Implement equilibrium solver
5. Go to `behavioral_scientist/` folder
6. Run experiments with classmates
7. Compare results

#### Phase 2: Mechanism Design (PS2)
1. Go to `mechanism_design/` folder
2. Choose auction format
3. Design experiment
4. Implement in oTree (`behavioral_scientist/otree_apps/`)
5. Run simulations with LLMs
6. Analyze winner's curse

#### Phase 3: Voting & Institutions
1. Review field trip notes
2. Design innovative voting mechanism
3. Connect to Nobel Prize insights
4. Implement and test
5. Write up findings

#### Phase 4: Documentation
1. Generate all visualizations (`visualizations/`)
2. Complete field trip reflection (`docs/FieldTripReflection.md`)
3. Write final report (`docs/Report.pdf`)
4. Create poster (`docs/Poster.pdf`)
5. Update main README with your specific details

## Detailed Workflow

### For Economists (Theoretical Analysis)

**Location**: `economist/` folder

**Tasks**:
1. Formalize the game
   - Define player set N
   - Define strategy spaces S_i for each player
   - Define payoff functions u_i
2. Identify equilibrium concepts
   - Nash equilibrium (pure and mixed)
   - Subgame perfect equilibrium (if sequential)
   - Bayes-Nash equilibrium (if incomplete information)
3. Analyze welfare properties
   - Pareto efficiency
   - Social welfare
   - Fairness metrics

**Output**: Markdown files or LaTeX documents in `economist/models/`, `economist/equilibria/`, `economist/welfare/`

### For Computational Scientists (Implementation)

**Location**: `computational_scientist/` folder

**Tasks**:
1. Set up environment
   ```bash
   cd computational_scientist
   jupyter lab  # Start Jupyter
   ```
2. Implement equilibrium solvers
   - Use NashPy for 2-player games
   - Use QuantEcon for more complex games
3. Run simulations
   - Monte Carlo for strategy testing
   - Agent-based modeling
4. Generate visualizations
   - All figures go to `../visualizations/`

**Example Code**:
```python
import nashpy as nash
import numpy as np

# Define game
A = np.array([[3, 0], [5, 1]])
B = np.array([[3, 5], [0, 1]])
game = nash.Game(A, B)

# Find equilibria
equilibria = game.support_enumeration()
for eq in equilibria:
    print(f"Nash equilibrium: {eq}")
```

**Output**: Python scripts, Jupyter notebooks, results files

### For Behavioral Scientists (Experiments)

**Location**: `behavioral_scientist/` folder

**Tasks**:
1. Install oTree
   ```bash
   pip install otree
   ```
2. Create experiment apps
   ```bash
   cd behavioral_scientist/otree_apps
   otree startapp my_game
   ```
3. Design treatments
4. Run with classmates
5. Collect LLM data
6. Analyze results

**Output**: oTree apps, experimental data, analysis notebooks

### For Mechanism Designers (Innovation)

**Location**: `mechanism_design/` folder

**Tasks**:
1. Choose mechanism type (auction or voting)
2. Design rules and procedures
3. Prove properties (if possible)
4. Implement computationally
5. Test experimentally
6. Compare to theoretical predictions

**Output**: Mechanism descriptions, implementation code, evaluation results

## Key Milestones

- [ ] **Week 1**: Repository setup, game formalization
- [ ] **Week 2**: Equilibrium computation, initial experiments
- [ ] **Week 3**: Mechanism design, LLM experiments
- [ ] **Week 4**: Data analysis, visualization generation
- [ ] **Week 5**: Report writing, poster creation
- [ ] **Week 6**: Final revisions, symposium preparation

## Common Tasks

### Creating a New Analysis Notebook

```bash
cd computational_scientist/notebooks
jupyter lab
# Create new notebook
# Save as descriptive_name.ipynb
```

### Running an oTree Experiment

```bash
cd behavioral_scientist/otree_apps
otree devserver
# Open browser to http://localhost:8000
```

### Generating Visualizations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Your plotting code here
plt.savefig('../visualizations/category/filename.png', dpi=300, bbox_inches='tight')
```

### Updating Documentation

```bash
# Edit the relevant README or markdown file
nano economist/README.md

# Or use your preferred editor
code docs/FieldTripReflection.md
```

## Tips for Success

1. **Start Early**: This is a comprehensive project
2. **Work Incrementally**: Complete one part before moving to next
3. **Document Everything**: Future you will thank present you
4. **Test Frequently**: Run code often to catch errors early
5. **Visualize Results**: Pictures are worth a thousand equations
6. **Ask Questions**: Use office hours, discussion board
7. **Collaborate**: Learn from classmates (but cite properly)
8. **Connect to Course**: Reference specific lectures and readings

## Troubleshooting

### Problem: NashPy installation fails
```bash
# Try upgrading pip first
pip install --upgrade pip
pip install nashpy
```

### Problem: oTree won't start
```bash
# Reset database
otree resetdb
# Try again
otree devserver
```

### Problem: Can't import libraries in Jupyter
```bash
# Install in the same environment
pip install ipykernel
python -m ipykernel install --user --name=venv
# Then select this kernel in Jupyter
```

### Problem: Visualizations don't appear
```python
# Add this at the top of notebook
%matplotlib inline
import matplotlib.pyplot as plt
```

## Resources

### Course Materials
- Problem Set 1 (PS1): [Johnnybyzhang/budgeted-vickrey](https://github.com/Johnnybyzhang/budgeted-vickrey)
- Problem Set 2 (PS2): Same repository
- Week 6 Reflection: See `orig/` folder

### Documentation
- [NashPy Docs](https://nashpy.readthedocs.io/)
- [QuantEcon Docs](https://quantecon.org/)
- [oTree Docs](https://otree.readthedocs.io/)
- [Game Theory Explorer](http://www.gametheoryexplorer.org/)

### Textbooks
- Osborne & Rubinstein: A Course in Game Theory
- Fudenberg & Tirole: Game Theory
- Krishna: Auction Theory
- Taylor: Social Choice and the Mathematics of Manipulation

### Nobel Prize Lectures (relevant to project)
- Arrow (1972): Social Choice
- Buchanan (1986): Constitutional Economics
- Hurwicz, Maskin, Myerson (2007): Mechanism Design
- Shapley, Roth (2012): Matching Theory
- Acemoglu, Johnson, Robinson (2024): Institutions

## Getting Help

1. **README Files**: Each folder has detailed guidance
2. **Office Hours**: Prof. Zhang and TAs
3. **Discussion Board**: Ask and answer questions
4. **Classmates**: Form study groups
5. **Online Communities**: Stack Overflow, Reddit, Discord

## Final Checklist

Before submission, ensure:

- [ ] All code runs without errors
- [ ] All visualizations are generated
- [ ] README.md is updated with your project specifics
- [ ] All folder READMEs are relevant to your work
- [ ] Field trip reflection is complete and thoughtful
- [ ] Report includes all required sections
- [ ] Poster is print-ready
- [ ] GitHub repository is public and accessible
- [ ] All teammates are credited appropriately
- [ ] SDG contributions are clearly stated
- [ ] Acknowledgments are complete
- [ ] Disclaimer is present and accurate

## Contact

**Instructor**: Prof. Luyao Zhang  
**Course**: COMSCI/ECON 206  
**Institution**: Duke Kunshan University  
**Term**: Autumn 2025

---

Good luck with your final project! Remember: the goal is to bridge theory and practice, connecting game theory to real-world applications while developing your computational and analytical skills.

*Last Updated: October 2025*
