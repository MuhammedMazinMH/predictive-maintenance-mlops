@"
# Predictive Maintenance MLOps

End-to-end MLOps pipeline for predicting engine remaining useful life (RUL).

## Tech Stack
- Python, Scikit-learn, XGBoost
- MLflow (experiment tracking)
- FastAPI (model serving)
- Docker (containerization)
- AWS EC2 (deployment)

## Project Structure
- `notebooks/` - EDA and model training
- `src/` - Source code (API, models, pipeline)
- `data/processed/` - Clean dataset
- `tests/` - Unit tests

## API Endpoints
- `POST /predict` - Predict RUL from sensor readings
- `GET /health` - Health check

## Run Locally
```bash
cd src/api
uvicorn main:app --reload

"@ | Out-File -Encoding utf8 README.md