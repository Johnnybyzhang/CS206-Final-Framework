# Behavioral Scientist - Experimental Design & Analysis

This folder contains all behavioral experiments, oTree applications, human experiment results, and LLM interaction transcripts.

## Contents

### Experimental Design
- oTree applications for interactive games
- Treatment and control group specifications
- Participant instructions and protocols
- Consent forms and ethical approvals

### Human Experiments
- Classroom experiment data
- Online experiment results
- Participant responses and strategies
- Demographic and background information

### AI Agent Experiments
- LLM player transcripts
- AI strategy analysis
- Prompt engineering documentation
- Comparative human-AI performance

## File Structure

```
behavioral_scientist/
├── otree_apps/
│   ├── strategic_game/              # PS1-based strategic game app
│   ├── auction_experiment/          # PS2-based auction app
│   ├── voting_mechanism/            # Voting experiment app
│   └── settings.py                  # oTree configuration
├── data/
│   ├── human_experiments/           # Human participant data
│   │   ├── raw/                     # Raw experimental data
│   │   ├── processed/               # Cleaned and processed data
│   │   └── codebook.md              # Data dictionary
│   └── ai_experiments/              # AI agent data
│       ├── llm_transcripts/         # LLM interaction logs
│       └── ai_strategies.csv        # AI decision records
├── analysis/
│   ├── descriptive_stats.ipynb      # Summary statistics
│   ├── behavioral_patterns.ipynb    # Pattern analysis
│   └── human_vs_ai.ipynb            # Comparative analysis
├── protocols/
│   ├── experiment_protocol.md       # Detailed experimental procedures
│   ├── instructions.md              # Participant instructions
│   └── consent_form.md              # Informed consent template
└── README.md                         # This file
```

## Setup and Installation

### oTree Setup

```bash
# Install oTree
pip install otree

# Navigate to otree_apps folder
cd otree_apps

# Create a new oTree project (if needed)
otree startproject my_experiment

# Run the development server
otree devserver
```

### Database Configuration

```bash
# Reset database (for fresh start)
otree resetdb

# Create sessions
otree create_session strategic_game 6  # 6 participants
```

## Experimental Protocol

### Phase 1: Classroom Experiments (Human)
1. **Recruitment**: Classmates from COMSCI/ECON 206
2. **Instructions**: Clear explanation of game rules and payoffs
3. **Practice Rounds**: Familiarization with interface
4. **Experimental Rounds**: 10-20 rounds of strategic interaction
5. **Post-Experiment Survey**: Demographics, strategies, reflections

### Phase 2: LLM Experiments (AI Agents)
1. **Model Selection**: GPT-4, Claude, or other LLMs
2. **Prompt Engineering**: Design prompts for strategic reasoning
3. **Automated Play**: Run multiple iterations with AI agents
4. **Logging**: Record all decisions and reasoning
5. **Analysis**: Compare AI strategies to human baseline

### Phase 3: Comparative Analysis
1. **Equilibrium Comparison**: How do results compare to Nash predictions?
2. **Human vs AI**: Differences in strategy and outcomes
3. **Bounded Rationality**: Evidence of cognitive biases
4. **Learning Dynamics**: Do players converge to equilibrium?

## Data Collection

### Human Experiment Data
- **Session Data**: Timestamps, round numbers, treatments
- **Decision Data**: Choices, strategies, reaction times
- **Outcome Data**: Payoffs, rankings, efficiency metrics
- **Survey Data**: Post-experiment questionnaires

### AI Experiment Data
- **Prompt Logs**: All prompts sent to LLMs
- **Response Logs**: Complete LLM responses
- **Decision Records**: Extracted strategic choices
- **Reasoning Analysis**: Natural language explanations

## Analysis Methods

### Descriptive Statistics
- Strategy frequency distributions
- Average payoffs by player type
- Equilibrium convergence rates

### Behavioral Patterns
- Identification of common biases (winner's curse, overbidding, etc.)
- Learning curves and adaptation
- Cooperation and defection patterns

### Comparative Analysis
- Human vs theoretical predictions
- AI vs theoretical predictions  
- Human vs AI performance
- Statistical significance tests

## Key Findings

### Human Behavior
- Deviations from Nash equilibrium
- Evidence of bounded rationality
- Social preferences and fairness concerns
- Learning and adaptation over time

### AI Behavior
- LLM strategic reasoning capabilities
- Comparison to optimal play
- Consistency across trials
- Explanation quality and coherence

### Insights
- Which player type performs better?
- What drives deviations from theory?
- How can mechanisms be improved?

## Integration with Other Components

- **Economist**: Tests theoretical predictions
- **Computational Scientist**: Provides computational benchmarks
- **Mechanism Designer**: Informs mechanism improvements
- **Visualizations**: Generates behavioral charts and graphs

## Tools and Platforms

### Experimental Platform
- **oTree**: Browser-based experiments
- **Qualtrics**: Surveys and questionnaires (if applicable)

### Data Analysis
- **Pandas**: Data manipulation
- **Statsmodels**: Statistical analysis
- **Seaborn/Matplotlib**: Visualization

### AI Integration
- **OpenAI API**: GPT models
- **Anthropic API**: Claude models
- **LangChain**: LLM orchestration (optional)

## Ethical Considerations

- **Informed Consent**: All participants provide consent
- **Anonymity**: Data is anonymized for analysis
- **Debriefing**: Participants informed of study purpose
- **Data Security**: Secure storage of participant information

## References

- [oTree Documentation](https://otree.readthedocs.io/)
- Behavioral Game Theory (Camerer, 2003)
- Experimental Economics (Kagel & Roth, 1995)

---

*For theoretical foundations, see [`../economist/`](../economist/)*  
*For computational implementations, see [`../computational_scientist/`](../computational_scientist/)*
