# AI and Wage Inequality in the United States, 2010–2024

This repository contains a reproducible Python analysis of how artificial intelligence adoption relates to wage inequality in the United States from 2010 to 2024. The project was developed as part of an independent economics research paper under the guidance of Professor Dirk Mateer at The University of Texas at Austin.

## Project Overview

Artificial intelligence is often expected to increase wage polarization by replacing routine middle-skill jobs and raising demand for high-skill labor. This project examines whether that pattern appears in U.S. wage data over the 2010–2024 period.

Using Bureau of Labor Statistics wage data and a composite AI adoption index, the analysis tracks changes in the wage distribution and tests whether rising AI adoption is associated with a wider or narrower wage gap.

## Research Question

Does rising AI adoption widen the U.S. wage gap, or do labor-market and institutional forces compress wages even during rapid AI diffusion?

## Main Finding

In this descriptive analysis, AI adoption rises while the 90/10 wage gap narrows. The relationship is negative in both current-year and lagged specifications, suggesting that other structural forces may have outweighed AI’s polarizing effects during this period.

## Why This Matters

Task-based economic theory predicts that AI should disproportionately affect routine middle-skill work, potentially increasing wage inequality. However, this project suggests that the real-world outcome between 2010 and 2024 was more complicated.

Instead of a simple hollowing-out story, the data show that low-wage workers experienced strong wage growth, middle-skill wages also rose meaningfully, and the wage distribution compressed overall. That makes this a useful case study in how policy, labor markets, and technology interact.

## Data Sources

This project uses:
- U.S. Bureau of Labor Statistics Occupational Employment and Wage Statistics (OEWS).
- OECD AI Policy Tracker.
- Stanford AI Index.

## Methodology

The project uses four main steps:

1. Build a 2010–2024 panel dataset.
2. Track the 90/10 wage gap over time.
3. Estimate simple ordinary least squares regressions.
4. Run a one-year lag robustness check.

The analysis is descriptive, not causal. It documents co-movement between AI adoption and wage inequality, but it does not claim that AI alone caused the wage changes.

## Repository Contents

- `analysis.py`: Builds the dataset and runs the regressions.
- `requirements.txt`: Lists Python packages needed to run the project.
- `data/`: Contains the cleaned datasets used in the analysis.
- `figures/`: Contains the generated charts.
- `output/`: Contains reproducible outputs from the script.

## How to Run the Project

### 1. Install Python packages
```bash
pip install -r requirements.txt
```

### 2. Run the analysis
```bash
python analysis.py
```

### 3. Check the output
After running the script, look in the `output/` folder for:
- `ai_wage_inequality_panel.csv`
- `ai_wage_regression_results.csv`
- `ai_wage_figure_data.csv`

## Key Outputs

The project produces:
- a cleaned panel dataset,
- regression results,
- a figure-ready dataset,
- a time-series chart,
- and a scatter plot showing the relationship between AI adoption and wage gaps.

## Interpretation

The evidence in this project suggests that AI adoption and wage inequality moved in opposite directions during the study period. That does not prove causation, but it does suggest that wage compression may have been driven by additional forces such as minimum wage policy, labor shortages, and post-pandemic market tightness.

## Limitations

This project is intentionally simple and descriptive. It does not include a full causal identification strategy, and it uses a national-level panel rather than state-level or occupation-level causal variation.

Future work could improve the design by:
- adding controls,
- using state-level variation,
- testing sector-specific effects,
- and expanding the time series beyond 2024.

## Author

**Sreesh Manayakar**  
Panther Creek High School  
Research conducted under guidance from Professor Dirk Mateer, The University of Texas at Austin

## Contact

For questions, contact: **sreeshkmanayakar@gmail.com**

## License

This project is licensed under the MIT License.
