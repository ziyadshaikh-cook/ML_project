# Student Math Score Predictor

A machine learning project that predicts a student's math score based on their personal background and other exam scores.

**Live Demo**: [https://student-performance-prediction-026p.onrender.com](https://student-performance-prediction-026p.onrender.com)

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
- **Docker** — containerization
- **Render** — cloud deployment (live hosting)

---

## Project Structure

```
├── src/ML_project/
│   ├── components/
│   │   ├── data_ingestion.py       # Reads and splits the raw data
│   │   ├── data_transformation.py  # Cleans and encodes the data
│   │   ├── model_trainer.py        # Trains and picks the best model
│   │   └── model_monitoring.py     # Detects if new data has drifted
│   ├── pipelines/
│   │   ├── training_pipelines.py   # Runs the full training flow
│   │   └── prediction_pipelines.py # Loads model and predicts on new input
│   ├── exception.py                # Custom error handling
│   ├── logger.py                   # Logging setup
│   └── utils.py                    # Shared helper functions
├── templates/
│   ├── index.html                  # Home page
│   └── home.html                   # Prediction form
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb   # Exploratory data analysis
│   └── 2. MODEL TRAINING.ipynb            # Model experiments
├── app.py                          # Flask web app
├── main.py                         # Run training pipeline
├── Dockerfile                      # Container setup
└── requirements.txt                # Python dependencies
```

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/ziyadshaikh-cook/Student-Performance-Prediction.git
cd Student-Performance-Prediction
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
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

## Run with Docker

```bash
docker build -t student-performance-prediction .
docker run -p 5000:5000 student-performance-prediction
```
Open your browser and go to `http://localhost:5000`

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

## Deployment

The app is containerized with Docker and deployed on **Render**.

Every push to the `main` branch automatically triggers a redeployment.

**Live URL**: [https://student-performance-prediction-026p.onrender.com](https://student-performance-prediction-026p.onrender.com)

---

## Author

**Ziyad Shaikh**  