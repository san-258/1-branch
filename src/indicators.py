import pandas as pd
import ta

def calculate_ema(series, window):
    """
    Calculate Exponential Moving Average (EMA).
    """
    return ta.trend.ema_indicator(close=series, window=window)

def calculate_macd(df, close_col='close', window_slow=26, window_fast=12, window_sign=9):
    """
    Calculate MACD, MACD Signal, and MACD Histogram.
    Returns the dataframe with new columns: MACD, MACD_signal, MACD_hist.
    """
    macd = ta.trend.MACD(close=df[close_col], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign)
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['MACD_hist'] = macd.macd_diff()
    return df

def is_bullish_crossover(short_term_series, long_term_series, idx):
    """
    Check for a bullish crossover at a specific index.
    (Short term crosses above Long term).
    """
    if idx < 1:
        return False
    return (short_term_series.iloc[idx-1] <= long_term_series.iloc[idx-1]) and \
           (short_term_series.iloc[idx] > long_term_series.iloc[idx])
