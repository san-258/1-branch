# Algorithmic Trading Strategies

This repository contains a collection of algorithmic trading strategies and experiments using the [Alpaca API](https://alpaca.markets).

## Structure

*   `notebooks/`: Jupyter notebooks containing strategy logic, backtests, and experiments.
    *   `qqq_3min.ipynb`: A 3-minute timeframe strategy for QQQ (likely using EMA crossovers).
    *   `alpaca_auto_trade.ipynb`: General automated trading script.
    *   `pullback_21_ema.ipynb`: Scanner for pullbacks to the 21 EMA.
    *   `crypto_trading_basic.ipynb`: Basic crypto trading example.
*   `src/`: Reusable Python modules.
    *   `indicators.py`: Helper functions for calculating technical indicators (EMA, MACD).
    *   `alpaca_utils.py`: Helper functions for connecting to the Alpaca API.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Create a `.env` file or export your Alpaca API credentials:
    ```bash
    export ALPACA_API_KEY="your_key_id"
    export ALPACA_SECRET_KEY="your_secret_key"
    export ALPACA_BASE_URL="https://paper-api.alpaca.markets" # or live url
    ```

## Usage

You can run the notebooks directly to see the strategies in action or import the modules from `src/` to build custom bots.

Example usage of `src` modules:

```python
from src.alpaca_utils import get_alpaca_api
from src.indicators import calculate_ema
import pandas as pd

# Connect to API
api = get_alpaca_api()

# ... fetch data ...
# df = ...

# Calculate Indicators
df['EMA_9'] = calculate_ema(df['close'], 9)
```
