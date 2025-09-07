import argparse
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import google.generativeai as genai

# -------------------
# Configure Gemini API
# -------------------
genai.configure(api_key="AIzaSyC2EVCSgC-DRWVunkKi7Ro0J1upoN3UglE")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------
# Helper: Risk Level
# -------------------
def risk_level(cases):
    avg_recent = np.mean(cases[-3:])  # average of last 3 points
    if avg_recent > 1000:
        return "High 🔴"
    elif avg_recent > 500:
        return "Medium 🟠"
    else:
        return "Low 🟢"

# -------------------
# Forecast Function
# -------------------
def epidemic_forecast(case_history):
    try:
        if len(case_history) < 5:
            print("❌ Error: Need at least 5 data points for forecasting.")
            return

        series = pd.Series(case_history)

        # Holt-Winters forecasting
        model_hw = ExponentialSmoothing(series, trend="add", seasonal=None)
        model_fit = model_hw.fit()
        forecast_values = model_fit.forecast(steps=5)

        trend = "increasing 📈" if np.mean(forecast_values) > np.mean(case_history) else "decreasing 📉"
        level = risk_level(case_history)

        # AI Prompt
        prompt = f"""
        You are an AI epidemiologist.
        Given the epidemic case history: {case_history}
        Forecasted next 5 case numbers: {list(forecast_values)}
        Trend: {trend}
        Current Risk Level: {level}

        Provide:
        1. Recommended interventions to control spread.
        2. Policy guidance for government/public health authorities.
        3. Short explanation why these actions are suitable.
        """
        response = model.generate_content(prompt)
        ai_text = response.text if response else "❌ No AI response"

        # Split AI output
        parts = ai_text.split("\n", 1)
        recommendation = parts[0].strip() if parts else "Not generated"
        explanation = parts[1].strip() if len(parts) > 1 else ai_text

        # Display
        print("\n🦠 Epidemic Spread Forecast & AI Insights")
        print("-" * 60)
        print(f"Next 5 Predicted Cases : {list(np.round(forecast_values,0))}")
        print(f"Trend                  : {trend}")
        print(f"Risk Level             : {level}\n")
        print("🤖 AI Recommended Interventions:")
        print(recommendation)
        print("\nAI Explanation:")
        print(explanation)

    except Exception as e:
        print(f"❌ Error: {e}")

# -------------------
# CLI Setup
# -------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🦠 Epidemic Spread Intelligence (Terminal Version)")
    parser.add_argument("--cases", type=str, help="Comma-separated epidemic case numbers (at least 5)")

    args = parser.parse_args()

    if args.cases:
        raw_input = args.cases
    else:
        raw_input = input("Enter epidemic case numbers (comma-separated, at least 5 values): ")

    case_history = [float(x.strip()) for x in raw_input.split(",") if x.strip()]
    epidemic_forecast(case_history)
