
from fastapi import FastAPI

app = FastAPI(
    title="QuantLab API",
    description="Quantitative Research and Backtesting Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to QuantLab!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/v1/status")
def api_status():
    return {
        "application": "QuantLab",
        "version": "1.0.0",
        "status": "operational"
    }
