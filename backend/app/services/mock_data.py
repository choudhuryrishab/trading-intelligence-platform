def get_mock_portfolio():
    return {
        "cash": 1200,
        "stocks": [
            {"ticker": "AAPL", "quantity": 3, "avg_price": 170},
            {"ticker": "TSLA", "quantity": 2, "avg_price": 240},
            {"ticker": "MSFT", "quantity": 1, "avg_price": 380}
        ]
    }