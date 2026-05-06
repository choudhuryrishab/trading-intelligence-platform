import os
from dotenv import load_dotenv

load_dotenv()

TRADING212_API_KEY = os.getenv("TRADING212_API_KEY")
TRADING212_API_SECRET = os.getenv("TRADING212_API_SECRET")