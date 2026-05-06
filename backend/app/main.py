from fastapi import FastAPI
from app.services.portfolio_service import PortfolioService

app = FastAPI(title="Trading Intelligence Platform")

portfolio_service = PortfolioService()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/portfolio")
def portfolio():
    return portfolio_service.get_portfolio()