# Student Math Score Predictor

A machine learning project that predicts a student's math score based on their personal background and other exam scores.

---

## What Does This Project Do?

Given information about a student — their gender, race/ethnicity, parental education level, lunch type, whether they completed a test preparation course, and their reading and writing scores — this project predicts what their **math score** will be.

It was built end-to-end: from raw data all the way to a working web app where anyone can enter student details and get a prediction instantly.

---

## How It Works (Simple Version)

1. The project looks at **1000 past students** where we already know all their details and their actual math score
2. It learns the pattern between those details and the math score
3. When you enter a new student's details, it uses that learned pattern to predict their math score

---

## Tech Stack

- **Python** — core language
- **scikit-learn** — machine learning models and preprocessing
- **XGBoost / CatBoost** — advanced ML models
- **MLflow + DagsHub** — experiment tracking (logs which model performed best)
- **Flask** — web framework for the prediction form
- **pandas / numpy** — data handling
- **Docker** — containerization for deployment

---

## Project Structure
├── src/ML_project/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ ├── model_trainer.py
│ │ └── model_monitoring.py
│ ├── pipelines/
│ │ ├── training_pipelines.py
│ │ └── prediction_pipelines.py
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
├── templates/
│ ├── index.html
│ └── home.html
├── notebook/
│ ├── 1. EDA STUDENT PERFORMANCE.ipynb
│ └── 2. MODEL TRAINING.ipynb
├── app.py
├── main.py
├── Dockerfile
└── requirements.txt

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/ziyadshaikh-cook/ML_project.git
cd ML_project
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**3. Train the model**
```bash
python main.py
```
This will generate `artifacts/model.pkl` and `artifacts/preprocessor.pkl`

**4. Run the web app**
```bash
python app.py
```
Open your browser and go to `http://127.0.0.1:5000`

---

## Models Trained

The project trains and compares 7 models, then automatically picks the best one:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- CatBoost
- AdaBoost

Best model is selected based on R² score on the test set. Current best: **Linear Regression (R² ≈ 0.88)**

---

## Author

**Ziyad Shaikh**  
Integrated MSc in Data Science — Goa Business School, Goa University