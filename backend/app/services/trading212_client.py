from backend.app.config import TRADING212_API_KEY

class Trading212Client:
    def __init__(self):
        self.api_key = TRADING212_API_KEY

    def get_portfolio(self):
        # for now still mock, but now "authenticated"
        if not self.api_key:
            raise Exception("Missing API key")

        return {
            "cash": 1000,
            "positions": [
                {"symbol": "AAPL", "quantity": 5, "avg_price": 170},
                {"symbol": "TSLA", "quantity": 2, "avg_price": 240}
            ]
        }