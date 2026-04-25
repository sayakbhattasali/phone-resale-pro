# 📱 Used Phone Price Predictor

A beginner-friendly Machine Learning project that predicts the **resale price of a used smartphone in INR** based on its specs and condition.

Built with **Python · pandas · scikit-learn · Streamlit**.

---
## 🌐 Live Demo
https://phone-resale-pro-hqpuqumrow8ujppd5rjcuz.streamlit.app/

## 🚀 Quick Start (3 steps)

### 1. Clone / download the project

```bash
git clone <your-repo-url>
cd used-phone-price-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app/streamlit_app.py
```

> **That's it!** The app auto-trains the model on first launch. No extra steps needed.

---

## 📁 Project Structure

```
used-phone-price-predictor/
│
├── data/
│   └── sample_phones.csv       # 80+ sample phone records
│
├── src/
│   ├── train_model.py          # Trains & saves the ML model
│   └── predict.py              # Loads model, runs predictions
│
├── app/
│   └── streamlit_app.py        # Web UI (run this!)
│
├── model/                      # Auto-created after first run
│   ├── model.pkl               # Saved Random Forest model
│   └── encoders.pkl            # Saved label encoders
│
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

| Step | What happens |
|------|-------------|
| 1 | User fills in phone details in the web form |
| 2 | App passes the inputs to `predict.py` |
| 3 | `predict.py` encodes the inputs and feeds them to the saved model |
| 4 | The **Random Forest Regressor** outputs an estimated price |
| 5 | App shows the price + a useful tip |

---

## 🎛️ Input Features

| Feature | Description |
|---------|-------------|
| Brand | Phone manufacturer (Samsung, Apple, OnePlus, etc.) |
| RAM | RAM in GB |
| Storage | Internal storage in GB |
| Age | How old the phone is (months) |
| Battery Health | Battery health percentage (50–100%) |
| Condition | Excellent / Good / Fair / Poor |

---

## 🔁 Retraining the Model

To retrain manually (e.g., after adding more data to the CSV):

```bash
python src/train_model.py
```

---

## 💡 Learning Concepts Covered

- **Data loading** with `pandas`
- **Label encoding** for categorical features
- **Train/test split** with `sklearn`
- **Random Forest Regression**
- **Model evaluation** (MAE, R²)
- **Model persistence** with `joblib`
- **Web UI** with `Streamlit`

---

## 📝 Notes

- The dataset is a sample (~80 records) for demonstration purposes.
- Predicted prices are estimates and should not be used for actual transactions.
- To improve accuracy, add more real-world data to `data/sample_phones.csv`.
