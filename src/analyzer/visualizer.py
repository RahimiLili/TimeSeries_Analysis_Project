"""
Visualizer Module for Time Series Analysis.
This class handles plotting for the project.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd

class TimeSeriesVisualizer:
    """
    A class to generate  plots for Time Series data.
    """

    def __init__(self, df, date_col='Date', target_col='Close'):
        self.df = df.copy()
        self.date_col = date_col
        self.target_col = target_col
        # Ensure date is datetime for plotting
        self.df[self.date_col] = pd.to_datetime(self.df[self.date_col])

    def plot_data(self):
        """Plot data """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df[self.date_col], self.df[self.target_col], label='Data')
        plt.title(f"Time Series: {self.target_col}")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig("TimeseriesData.png")
        plt.show()
        plt.close()
    

    def plot_seasonal_heatmap(self):
        """Creates a heatmap showing average price by Month and Year."""
        df_copy = self.df.copy()
        df_copy['Year'] = df_copy[self.date_col].dt.year
        df_copy['Month'] = df_copy[self.date_col].dt.month
        
        pivot = df_copy.pivot_table(
            values=self.target_col, 
            index='Month', 
            columns='Year', 
            aggfunc='mean'
        )
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot, cmap='YlGnBu')
        plt.title(f"Seasonal Heatmap: {self.target_col}")
        plt.ylabel("Month (1-12)")
        plt.savefig("seasonal_heatmap.png")
        plt.show()
        plt.close()

    def plot_pacf_acf(self, lags=40):
        """Plots Autocorrelation and Partial Autocorrelation."""
        series = self.df[self.target_col].dropna()
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
        
        plot_acf(series, ax=ax1, lags=lags)
        plot_pacf(series, ax=ax2, lags=lags)
        
        plt.suptitle(f"ACF and PACF for {self.target_col}")
        plt.savefig("acf_pacf_plots.png")
        plt.show()
        plt.close()

    def plot_rolling_stats(self, window=30):
        """Plots original data vs a rolling mean for trend smoothing."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.df[self.date_col], self.df[self.target_col], label='Original', alpha=0.4)
        
        rolling_mean = self.df[self.target_col].rolling(window=window).mean()
        plt.plot(self.df[self.date_col], rolling_mean, label=f'{window}-Day Moving Average', color='red')
        
        plt.title(f"Rolling Statistics: {self.target_col}")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig("rolling_stats.png")
        plt.show()
        plt.close()
    
    def plot_decomposition(self, decomposition_result):
        """Plots the 4 components: Observed, Trend, Seasonal, and Residual."""
       # plt.figure(figsize=(10, 6))
        fig = decomposition_result.plot()
        fig.set_size_inches(12, 10)
        plt.suptitle('Time Series Decomposition', fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        plt.savefig("decomposition_plot.png")
        plt.show()
        plt.close()




    def plot_daily_returns_distribution(self,daily_returns):
        plt.figure(figsize=(10, 6))
        
        #  Create histogram with probability density
        plt.hist(daily_returns, bins=100, color='skyblue', edgecolor='black', alpha=0.7, density=True)
        
        #  Statistical markers (Mean and Median)
        mu, median = daily_returns.mean(), daily_returns.median()
        plt.axvline(mu, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {mu:.4%}')
        plt.axvline(median, color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {median:.4%}')
        
        #  Formatting
        plt.title('Distribution of Daily Returns for  Price', fontsize=14)
        plt.xlabel('Daily Return (Percentage Change)', fontsize=12)
        plt.ylabel('Density', fontsize=12)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.savefig('daily_returns_dist.png')
        plt.show()
        plt.close()
    