import os
import requests

class Trading212Client:
    def __init__(self):
        self.api_key = os.getenv("TRADING212_API_KEY")
        self.base_url = "https://api.trading212.com"  # placeholder

    def get_portfolio(self):
        """
        Fetch portfolio data from Trading212 API.
        (We will adjust endpoint once you confirm API access details)
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        # NOTE: endpoint may differ depending on Trading212 API version
        response = requests.get(
            f"{self.base_url}/equity/portfolio",
            headers=headers
        )

        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")

        return response.json()