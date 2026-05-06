from app.services.mock_data import get_mock_portfolio

class PortfolioService:

    def get_portfolio(self):
        """
        Main entry point for portfolio data.
        Later this will switch between:
        - Trading212 API
        - Cached DB
        - Mock data
        """

        data = get_mock_portfolio()

        # future: calculate metrics here
        data["total_positions"] = len(data["stocks"])

        return data