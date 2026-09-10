# NBA Game Outcome Modeling

An exploratory machine-learning project for predicting NBA game outcomes from historical team performance. The project combines an Elo rating system with rolling team statistics and compares several classification models.

## What this project demonstrates

- Feature engineering over historical, time-ordered sports data
- A custom Elo implementation that updates team strength after each game
- Recent-form features calculated from rolling team performance
- Scikit-learn pipelines for preprocessing, dimensionality reduction, and classification
- Model comparison using accuracy and F1 score

## Repository structure

```text
.
├── NBA_Prediction_Model.ipynb   # Main analysis and model experiments
├── data/                        # Historical datasets used by the notebook
├── notebooks/
│   ├── eloUtils.py              # Elo calculation helpers
│   ├── FiveThirtyEightScraper.py
│   └── make_betting_dataset.py  # Legacy exploratory data preparation
└── requirements.txt
```

## Inspect locally

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
PYTHONPATH=notebooks jupyter notebook NBA_Prediction_Model.ipynb
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "notebooks"
jupyter notebook NBA_Prediction_Model.ipynb
```

The notebook currently preserves the original exploratory work and saved outputs. It is not yet intended to execute cleanly from top to bottom; reproducible execution is part of the next modeling revision.

## Evaluation status

The saved notebook contains exploratory model results, but the current evaluation uses a random train/test split without a fixed seed. Because games are time-ordered observations, those numbers should not be treated as final or directly reproducible.

The next modeling revision will:

1. Use a chronological holdout to better represent predictions on future games.
2. Fix random seeds for deterministic comparisons.
3. Compare each classifier against a simple Elo baseline.
4. Report accuracy, precision, recall, F1, and calibration on the same holdout period.

## Data note

The repository contains snapshots of historical datasets used during the original analysis. Their provenance and redistribution terms should be verified before the data is reused or republished. A future cleanup will replace undocumented files with reproducible download instructions where possible.

## Current limitations

- The notebook combines feature engineering, training, evaluation, and legacy experiments in one file.
- Dataset provenance is not yet documented consistently.
- There is no automated test suite for the Elo and feature-generation logic.
- The existing evaluation is not time-aware.

These limitations are documented to keep the results honest while the project is reorganized into a reproducible portfolio example.
