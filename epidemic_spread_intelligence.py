import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta

# Step 1: Generate synthetic epidemic case counts (daily) with waves and interventions
np.random.seed(42)
days = 365
dates = pd.date_range(start="2023-01-01", periods=days, freq='D')

# Simulate multiple waves in infection counts
wave1 = 1000 * np.exp(-((dates.dayofyear - 90) / 30) ** 2)  # wave peak around day 90
wave2 = 1500 * np.exp(-((dates.dayofyear - 180) / 25) ** 2)  # wave peak around day 180
wave3 = 1200 * np.exp(-((dates.dayofyear - 300) / 40) ** 2)  # wave peak around day 300

base_noise = np.random.poisson(20, days)
cases = (wave1 + wave2 + wave3 + base_noise).astype(int)

# Simulate intervention effect: reduce cases by 40% starting day 200
cases_with_intervention = cases.values.copy()
cases_with_intervention[200:] = (cases.values[200:] * 0.6).astype(int)
cases_with_intervention = pd.Series(cases_with_intervention, index=dates)

data = pd.DataFrame({
    'date': dates,
    'cases': cases_with_intervention.values
})

# Save dataset
data.to_csv("synthetic_epidemic_cases.csv", index=False)
print("Synthetic epidemic case dataset saved as 'synthetic_epidemic_cases.csv'.")

# Step 2: Fit ARIMA model for forecasting
ts = data.set_index('date')['cases']
ts.index.freq = 'D'  # Explicitly set frequency to suppress warnings

# Simple ARIMA configuration; normally requires parameter tuning
model = ARIMA(ts, order=(2,1,2))
fit = model.fit()

forecast_period = 30

# --- User Input for forecasting start date ---
while True:
    input_date_str = input(f"\nEnter a date to start forecast (YYYY-MM-DD, between {ts.index.min().date()} and {ts.index.max().date()}): ")
    try:
        forecast_start_date = pd.to_datetime(input_date_str)
        if forecast_start_date < ts.index.min() or forecast_start_date > ts.index.max():
            print("Date out of range, please try again.")
            continue
        break
    except Exception:
        print("Invalid date format, please try again.")

# Subset time series from input date for forecasting
ts_sub = ts.loc[:forecast_start_date]

ts_sub.index.freq = 'D'  # Explicitly set frequency here too

if len(ts_sub) < 30:
    print(f"Warning: Only {len(ts_sub)} days of data available for forecasting from the chosen start date.")

# Fit model on subset
model_sub = ARIMA(ts_sub, order=(2,1,2))
fit_sub = model_sub.fit()

forecast = fit_sub.get_forecast(steps=forecast_period)
forecast_index = pd.date_range(ts_sub.index[-1] + timedelta(days=1), periods=forecast_period)
forecast_mean = forecast.predicted_mean
conf_int = forecast.conf_int()

# Step 3: Simplified intervention impact & policy recommendation logic
avg_forecast = forecast_mean.mean()
if avg_forecast > 1500:
    policy = "Strict social distancing required."
elif avg_forecast > 700:
    policy = "Moderate restrictions recommended."
else:
    policy = "Current policies appear sufficient."

# Output forecast and policy recommendation
print("\nForecasted cases for the next 30 days:")
print(forecast_mean)

print(f"\nPolicy recommendation based on forecast: {policy}")

# Step 4: Visualization
plt.figure(figsize=(14,7))
plt.plot(data['date'], data['cases'], label='Observed Cases')
plt.plot(forecast_index, forecast_mean, 'r--', label='Forecast')
plt.fill_between(forecast_index, conf_int.iloc[:,0], conf_int.iloc[:,1], color='pink', alpha=0.3)
plt.title('Epidemic Cases & 30-Day Forecast')
plt.xlabel('Date')
plt.ylabel('Daily Cases')
plt.legend()
plt.tight_layout()
plt.show()

sns.histplot(data['cases'], bins=30, kde=True)
plt.title('Histogram of Daily Cases')
plt.xlabel('Cases')
plt.tight_layout()
plt.show()
