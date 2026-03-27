import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd

def plot_seasonal_heatmap(df, date_col='Date', target_col='Close'):
    """Creates a heatmap showing average price by Month and Year."""
    df_copy = df.copy()
    df_copy[date_col] = pd.to_datetime(df_copy[date_col])
    df_copy['Year'] = df_copy[date_col].dt.year
    df_copy['Month'] = df_copy[date_col].dt.month
    
    # Create pivot table
    pivot = df_copy.pivot_table(values=target_col, index='Month', columns='Year', aggfunc='mean')
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap='YlGnBu')
    plt.title(f"Seasonal Heatmap: {target_col}")
    plt.ylabel("Month (1-12)")
    plt.savefig("seasonal_heatmap.png")
    plt.show() # Adding .show() so it appears in the notebook too
    plt.close()

def plot_pacf_acf(series):
    """Plots Autocorrelation and Partial Autocorrelation."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
    plot_acf(series.dropna(), ax=ax1, lags=40)
    plot_pacf(series.dropna(), ax=ax2, lags=40)
    plt.savefig("acf_pacf_plots.png")
    plt.show()
    plt.close()

def plot_rolling_stats(df, column='Close', window=30):
    """Plots original data vs rolling mean."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df[column], label='Original', alpha=0.5)
    plt.plot(df['Date'], df[column].rolling(window).mean(), label=f'{window}-Day Mean', color='red')
    plt.title("Rolling Statistics")
    plt.legend()
    plt.savefig("rolling_stats.png")
    plt.show()
    plt.close()