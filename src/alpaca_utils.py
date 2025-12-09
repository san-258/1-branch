import os
from alpaca_trade_api.rest import REST

def get_alpaca_api(api_key=None, api_secret=None, base_url=None):
    """
    Initialize Alpaca REST API client using environment variables or arguments.
    """
    key = api_key or os.getenv('ALPACA_API_KEY')
    secret = api_secret or os.getenv('ALPACA_SECRET_KEY')
    url = base_url or os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')

    if not key or not secret:
        raise ValueError("Alpaca API credentials not found. Please set ALPACA_API_KEY and ALPACA_SECRET_KEY.")

    return REST(key, secret, base_url=url)
