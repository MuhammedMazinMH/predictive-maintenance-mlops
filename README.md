# 🔧 Predictive Maintenance MLOps

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)](https://mlflow.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)

> End-to-end MLOps pipeline for predicting aircraft engine Remaining Useful Life (RUL) using NASA Turbofan Engine Degradation dataset.

## 🎯 Problem Statement

Aircraft engines degrade over time. Unexpected failures cause:
- **₹3-5 lakhs/hour** downtime cost
- Delayed orders, safety risks
- Emergency repairs cost **3x more** than planned maintenance

**Solution:** Predict engine failure **before it happens** using sensor data and MLOps.

## 🏗️ Architecture
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   NASA      │────▶│   MLflow    │────▶│   FastAPI   │
│   Dataset   │     │   Tracking  │     │   Serving   │
└─────────────┘     └─────────────┘     └──────┬──────┘
│
┌──────▼──────┐
│    Docker   │
│  Container  │
└──────┬──────┘
│
┌──────▼──────┐
│  AWS EC2    │
│  (Deployed) │
└─────────────┘
plain


## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **ML** | Scikit-learn, XGBoost | Model training & prediction |
| **Tracking** | MLflow | Experiment tracking, model registry |
| **API** | FastAPI | Real-time model serving |
| **Container** | Docker | Portable deployment |
| **Cloud** | AWS EC2 | Production hosting |
| **CI/CD** | GitHub Actions | Auto-deploy on push |
| **Monitoring** | CloudWatch | Log aggregation |

## 📊 Dataset

- **Source:** NASA Turbofan Engine Degradation (public)
- **Engines:** 100 aircraft engines
- **Sensors:** 21 sensor readings per cycle
- **Target:** Remaining Useful Life (RUL) in cycles
- **Size:** 20,631 readings

## 🚀 Deployment (Previously Live on AWS)

> ⚠️ AWS EC2 instance terminated to stay within free tier limits. Full deployment was live and tested.

**What was deployed:**
- FastAPI serving predictions at `http://<EC2_IP>:8000`
- Interactive Swagger docs at `/docs`
- Docker container running on Amazon Linux 2023
- Auto-deployment via GitHub Actions on every push

**Screenshots of live deployment:** Available in repo issues

## 📈 Model Performance

| Model | RMSE | MAE | Status |
|-------|------|-----|--------|
| Random Forest | 35.33 | 25.88 | ✅ Production |
| XGBoost | 35.54 | 25.91 | Candidate |

## 🔥 Key Features

- ✅ **MLflow experiment tracking** — compare models, register best
- ✅ **FastAPI auto-docs** — interactive Swagger UI at `/docs`
- ✅ **Docker containerization** — runs anywhere
- ✅ **GitHub Actions CI/CD** — push code → auto-deploy to EC2
- ✅ **CloudWatch logging** — monitor predictions in real-time
- ✅ **Risk classification** — normal / high / critical alerts

## 🧪 Run Locally

```bash
# Clone repo
git clone https://github.com/MuhammedMazinMH/predictive-maintenance-mlops.git
cd predictive-maintenance-mlops

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start API
cd src/api
uvicorn main:app --reload

API will be live at: http://localhost:8000/docs

🧪 Example Prediction

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sensor_1": -0.0007,
    "sensor_2": -0.0004,
    "sensor_5": 641.82,
    "sensor_6": 1589.70,
    "sensor_7": 1400.60,
    "sensor_9": 14.62,
    "sensor_10": 21.61,
    "sensor_11": 554.36,
    "sensor_12": 2388.06,
    "sensor_14": 8138.62,
    "sensor_15": 8.4195,
    "sensor_16": 0.03,
    "sensor_17": 392,
    "sensor_18": 2388,
    "sensor_20": 47.47,
    "setting_2": 39.06,
    "setting_3": 23.42
  }'

Response:

JSON
{
  "rul": 84.71,
  "risk_level": "normal"
}

📁 Project Structure

predictive-maintenance-mlops/
├── 📁 notebooks/
│   ├── 01_eda.ipynb              # Exploratory data analysis
│   └── 02_model_training.ipynb   # MLflow tracking & model comparison
├── 📁 src/
│   ├── 📁 api/
│   │   ├── main.py               # FastAPI application
│   │   └── schemas.py            # Pydantic request/response models
│   ├── 📁 models/
│   │   ├── model.pkl             # Trained Random Forest model
│   │   └── features.pkl          # Feature names
│   └── 📁 pipeline/
│       └── preprocess.py         # Data preprocessing
├── 📁 data/
│   └── processed/
│       └── train_clean.csv       # Clean dataset
├── 📁 .github/
│   └── workflows/
│       └── deploy.yml            # CI/CD pipeline for AWS EC2
├── Dockerfile                    # Docker image definition
├── requirements.txt              # Python dependencies
└── README.md
                     # This file
🔄 CI/CD Pipeline

on: push to main
jobs:
  1. Checkout code
  2. SSH to AWS EC2
  3. Pull latest code
  4. Stop old container
  5. Build new Docker image
  6. Start new container
  7. API live in ~20 seconds

🎓 What I Learned
Building production ML pipelines end-to-end
Docker containerization for ML models
AWS EC2 deployment with security groups
GitHub Actions for automated deployment
MLflow for experiment tracking and model registry
FastAPI for high-performance model serving

📬 Contact
Muhammed Mazin MH