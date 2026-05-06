from app.services.mock_data import get_mock_portfolio


class PortfolioService:
    def __init__(self):
        # later: inject API clients / DB here
        pass

    def get_portfolio(self):
        """
        Main entry point for portfolio data.

        Future sources:
        - Trading212 API
        - Database cache
        - Mock fallback
        """

        data = get_mock_portfolio()

        # safety guard (prevents KeyError later)
        stocks = data.get("stocks", [])

        # computed fields
        data["total_positions"] = len(stocks)

        data["total_value_estimate"] = self._estimate_value(stocks)

        return data

    def _estimate_value(self, stocks):
        """
        Simple placeholder valuation.
        Later replaced by:
        - real-time prices API
        """
        total = 0

        for stock in stocks:
            qty = stock.get("quantity", 0)
            avg_price = stock.get("avg_price", 0)
            total += qty * avg_price

        return round(total, 2)