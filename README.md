# NBA Game Prediction Model

This project implements a machine learning model to predict NBA game outcomes using historical game data, team statistics, and betting odds. The model utilizes ELO ratings and various features to make predictions.

## Project Structure

```
NBA-Prediction-Model/
├── data/                    # Data files
│   ├── 538_probs.csv
│   ├── all_moneylines_sbr.csv
│   ├── games.csv
│   ├── games_details.csv
│   ├── players.csv
│   ├── ranking.csv
│   └── teams.csv
├── notebooks/               # Jupyter notebooks
│   ├── BettingWithClassifiers.ipynb
│   └── eloUtils.py
└── README.md                # This file
```

## Data Sources

- **NBA Game Data**: Historical game data including scores, teams, and player statistics.
- **Betting Odds**: Moneyline data from various sportsbooks.
- **538 Predictions**: Game predictions from FiveThirtyEight's NBA model.

## Key Features

- ELO rating system implementation for team strength estimation
- Feature engineering for game predictions
- Machine learning models for outcome prediction
- Performance evaluation metrics

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- jupyter

## Usage

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/BettingWithClassifiers.ipynb
   ```

## Model Performance

The model's performance is evaluated using various metrics including accuracy, precision, recall, and ROC-AUC. Detailed performance analysis can be found in the notebook.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
