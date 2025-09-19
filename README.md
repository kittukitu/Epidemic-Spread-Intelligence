Epidemic Case Forecasting and Policy Recommendation
This project simulates daily epidemic case counts over one year with multiple infection waves and intervention impacts. It fits an ARIMA time series model to forecast future case numbers, provides tentative policy recommendations, and visualizes observed and forecasted epidemic progression.

Features
Synthetic dataset generation of daily case counts featuring three epidemic waves and intervention effect (40% case reduction starting day 200).

ARIMA(2,1,2) forecasting model with user-specified forecast start date.

30-day case forecast with confidence intervals.

Simple policy recommendation logic based on forecasted case averages.

Visualizations of observed cases, forecast with confidence bands, and case distribution histogram.

Requirements
Python 3.x

pandas

numpy

matplotlib

seaborn

statsmodels

Install dependencies with:

bash
pip install pandas numpy matplotlib seaborn statsmodels
Usage
Run the script
The script generates synthetic_epidemic_cases.csv containing daily case counts with interventions simulated.

Input forecast start date
Enter a date (YYYY-MM-DD) within the dataset range to start forecasting (including historical data up to that date).

Output

Displays forecasted daily cases for 30 days following the input date.

Provides a policy recommendation based on forecasted average cases:

Above 1500: "Strict social distancing required."

Above 700: "Moderate restrictions recommended."

Otherwise: "Current policies appear sufficient."

Visualizations

Time series plot showing observed cases plus forecast with confidence intervals.

Histogram of daily case counts distribution.

Files
synthetic_epidemic_cases.csv: Generated synthetic epidemic case counts dataset.

Script file: Python code for data generation, forecasting, policy logic, and visualization.

Notes
ARIMA parameters are fixed (2,1,2) for simplicity; tuning for real data is recommended.

Forecast uses all data up to user-defined date; shorter series forecast warning shown if less than 30 days.

Visualizations require graphical display support.