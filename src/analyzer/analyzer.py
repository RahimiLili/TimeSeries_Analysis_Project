from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd


class TimeSeriesAnalyzer:
#
    def __init__(self, df, column='Close', date_col='Date', period=365):
        self.df = df
        self.column = column
        self.date_col = date_col
        self.period = period

    def adf_test(self):
        """Augmented Dickey-Fuller test for Stationarity."""
        series = self.df[self.column].dropna()
        res = adfuller(series)
        return {
            'statistic': res[0],
            'p-value': res[1],
            'is_stationary': res[1] < 0.05
        }

    def kpss_test(self):
        """KPSS test (opposite of ADF)."""
        series = self.df[self.column].dropna()
        res = kpss(series, regression='c', nlags="auto")
        return {
            'statistic': res[0],
            'p-value': res[1],
            'is_stationary': res[1] > 0.05
        }

    def decompose_signal(self):
        """Splits data into Trend, Seasonal, and Resid."""
        df_idx = self.df.set_index(self.date_col)
        return seasonal_decompose(
            df_idx[self.column],
            model='additive',
            period=self.period
        )

    def get_volatility_stats(self):
        """Calculates rolling standard deviation as a proxy for risk."""
        returns = self.df[self.column].pct_change()
        return {
            'Daily Volatility': returns.std(),
            'Annual Volatility': returns.std() * (252 ** 0.5)
        }