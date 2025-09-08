# 🦠 Epidemic Spread Intelligence

An AI-powered epidemic forecasting and intervention tool.  
It predicts the **future number of cases** using **Holt-Winters Exponential Smoothing** and generates **AI-driven health policy recommendations** via the **Gemini API**.

---

## 📌 Features
- Forecasts the next **5 epidemic case numbers**.
- Detects spread **trend** (📈 increasing / 📉 decreasing).
- Classifies current **risk level**:
  - 🔴 High (avg last 3 > 1000 cases)
  - 🟠 Medium (avg last 3 > 500 cases)
  - 🟢 Low (avg last 3 ≤ 500 cases)
- AI-generated recommendations:
  - Intervention strategies.
  - Policy guidance for public health authorities.
  - Short explanations for chosen actions.
- Works via **Command Line Interface (CLI)** with interactive input support.

---

## 🛠 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/epidemic-forecast-ai.git
cd epidemic-forecast-ai
2. Install Dependencies
bash
Copy code
pip install pandas numpy statsmodels google-generativeai
3. Configure API Key
Replace the placeholder key in the script with your Gemini API key:

python
Copy code
genai.configure(api_key="YOUR_GEMINI_API_KEY")
🚀 Usage
CLI Mode
Run the script with past case numbers:

bash
Copy code
python epidemic_forecast.py --cases 100,200,350,400,600,800,1200
Interactive Mode
If no --cases are provided:

bash
Copy code
python epidemic_forecast.py
Then enter values when prompted:

java
Copy code
Enter epidemic case numbers (comma-separated, at least 5 values): 50,75,120,200,400,700
📊 Example Output
yaml
Copy code
🦠 Epidemic Spread Forecast & AI Insights
------------------------------------------------------------
Next 5 Predicted Cases : [830.  875.  920.  965. 1010.]
Trend                  : increasing 📈
Risk Level             : Medium 🟠

🤖 AI Recommended Interventions:
- Implement partial mobility restrictions, increase testing and contact tracing.

AI Explanation:
These measures help slow down transmission while avoiding a complete lockdown. 
Testing and tracing allow targeted containment, and public health communication ensures awareness.
🔮 Future Enhancements
Add visualization with matplotlib (historical + forecasted cases).

Export results and AI recommendations to CSV/JSON reports.

Add epidemic simulation with multiple parameters (R0, mortality, etc.).

Deploy as a Flask/Django web dashboard for policymakers.