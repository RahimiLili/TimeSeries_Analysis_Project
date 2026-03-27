"""
Core Analysis Module for Time Series Data.
This module provides statistical tests (ADF, KPSS) and signal 
decomposition specifically tuned for financial datasets like ADANIPORTS.
"""

from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

class TimeSeriesAnalyzer:
    """
    A tool to automate the statistical evaluation of time series data.
    """

    def __init__(self, df, column='Close', date_col='Date', period=252):
        # I use 252 because that's the approximate number of trading days in a year instead of 365
        self.df = df.copy()
        self.column = column
        self.date_col = date_col
        self.period = period
        
        # Ensure the date column is actually a datetime object for the decomposition
        self.df[self.date_col] = pd.to_datetime(self.df[self.date_col])

    def adf_test(self):
        """
        Augmented Dickey-Fuller test for Stationarity.
        If p-value < 0.05, the data is stationary.
        """
        series = self.df[self.column].dropna()
        res = adfuller(series)
        return {
            'statistic': res[0],
            'p-value': res[1],
            'is_stationary': res[1] < 0.05
        }

    def kpss_test(self):
        """
        KPSS test (opposite of ADF).
        If p-value > 0.05, the data is stationary.
        """
        series = self.df[self.column].dropna()
        res = kpss(series, regression='c', nlags="auto")
        return {
            'statistic': res[0],
            'p-value': res[1],
            'is_stationary': res[1] > 0.05
        }

    def decompose_signal(self):
        """
        Splits data into Trend, Seasonal, and Residuals.
        Uses an additive model suitable for price data.
        """
        # Set the date as index specifically for the decomposition tool
        df_idx = self.df.set_index(self.date_col)
        return seasonal_decompose(
            df_idx[self.column],
            model='additive',
            period=self.period
        )

    def get_volatility_stats(self):
        """
        Calculates daily and annual volatility using percentage changes.
        Annualized volatility = daily_std * sqrt(252 trading days).
        """
        returns = self.df[self.column].pct_change().dropna()
        daily_vol = returns.std()
        return {
            'Daily Volatility': daily_vol,
            'Annual Volatility': daily_vol * (252 ** 0.5)
        }
    def daily_returns(self):
        """
        Calculates daily returns from a price series
        """
        return self.df[self.column].pct_change().dropna()
 