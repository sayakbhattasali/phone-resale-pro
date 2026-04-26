````md
# 📱 Phone Resale Pro

> AI-powered smartphone resale valuation platform that estimates the fair market price of used phones in INR based on specifications, condition, battery health, and age.

Built with **Python • pandas • scikit-learn • Streamlit**

---
## 🌐 Live Demo
https://phone-resale-pro-hqpuqumrow8ujppd5rjcuz.streamlit.app/

## ✨ Overview

Phone Resale Pro helps users estimate the resale value of used smartphones using Machine Learning.  
Instead of guessing prices manually, the app analyzes multiple real-world factors and generates an intelligent market estimate instantly.

### Key Highlights

- 📊 Smart resale price prediction
- 📱 Supports multiple brands & models
- 🔋 Battery health + age based valuation
- 📈 Lifecycle depreciation forecast
- 🎯 Clean premium web interface
- ⚡ Instant predictions with Streamlit

---

## 🚀 Live Features

- Fair market value estimate  
- Suggested listing price range  
- Retention percentage vs launch price  
- Future depreciation forecast chart  
- Mobile responsive UI  
- Real product image fetching  

---

## 🧠 How It Works

```text
User Input → Data Processing → ML Model Prediction → Price Estimate → Insights Dashboard
````

### Prediction Factors Used

| Factor           | Description                    |
| ---------------- | ------------------------------ |
| Brand            | Apple, Samsung, Xiaomi, etc.   |
| Model            | Specific smartphone model      |
| RAM              | Device RAM in GB               |
| Storage          | Internal storage               |
| Age              | Phone age in months            |
| Battery Health   | Current battery condition      |
| Visual Condition | Excellent / Good / Fair / Poor |
| Launch Price     | Original retail price          |

---

## 🛠 Tech Stack

| Category      | Tools                   |
| ------------- | ----------------------- |
| Language      | Python                  |
| Data Handling | pandas                  |
| ML Model      | scikit-learn            |
| UI            | Streamlit               |
| Charts        | Plotly                  |
| Deployment    | Streamlit Cloud / Local |

---

## 📂 Project Structure

```text
Phone-Resale-Pro/
│
├── data/
│   └── used_phones_clean.csv
│
├── model/
│   ├── model.pkl
│   └── encoders.pkl
│
├── predict.py
├── train_model.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## ⚡ Installation & Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sayakbhattasali/phone-resale-pro.git
cd phone-resale-pro
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch App

```bash
streamlit run streamlit_app.py
```

---

## 📈 Model Pipeline

```text
Dataset → Cleaning → Encoding → Train/Test Split →
Random Forest Regressor → Evaluation → Deployment
```

### Evaluation Metrics

* MAE (Mean Absolute Error)
* R² Score
* Prediction Stability

---

## 🔁 Retrain Model

If dataset is updated:

```bash
python train_model.py
```

---

## 📸 Screenshots

> Add screenshots here for better GitHub presentation.

```md
![Homepage](images/homepage.png)
![Prediction Result](images/result.png)
```

---

## 💡 Future Improvements

* Live OLX / Cashify market scraping
* Confidence score prediction
* User login & saved history
* Compare two phones resale value
* Explainable AI pricing breakdown

---

## ⚠ Disclaimer

Predicted prices are estimated values based on available training data and should be used for informational purposes only.

---

## 👨‍💻 Author

**Sayak Bhattasali**

* GitHub: [https://github.com/sayakbhattasali](https://github.com/sayakbhattasali)

---

## ⭐ Support

If you liked this project, consider starring the repository.

```
```
