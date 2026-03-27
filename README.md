ADANIPORTS Time Series Analysis Package
A professional Python tool for cleaning, analyzing, and visualizing financial time series data. This project uses the ADANIPORTS dataset to demonstrate stationarity testing, signal decomposition, and volatility modeling.

 Installation
This project is managed with uv. To install the package in editable mode:

Bash
uv pip install -e .
 Usage
Command Line Interface
You can run the full analysis pipeline directly from your terminal:

Bash
uv run -m analyzer
Jupyter Notebook
For a detailed step-by-step walkthrough and interactive visualizations, explore the provided notebook:
notebooks/analysis.ipynb

 Core Analysis Features
1. Statistical Stationarity Testing
To ensure the data is suitable for forecasting models like ARIMA, the package performs a dual-check:

ADF Test (adf_test): A statistical "sanity check" to see if a time series is trend-dependent.

Goal: Determine if the data is Stationary (constant mean/variance).

Logic: If p-value < 0.05, we reject the null hypothesis; the data is likely stationary.

KPSS Test (kpss_test): The "double-check" to the ADF test.

Logic: It assumes the data is stationary as the null hypothesis.

Why use both? Using ADF and KPSS together identifies Trend Stationarity—where data looks non-stationary only because of an underlying trend.

2. Signal Decomposition (decompose_signal)
This function performs Classical Decomposition to strip the price data into its constituent parts:

Trend: The long-term progression (e.g., is the stock generally going up?).

Seasonal: Repeated cycles (e.g., higher trading volumes at the end of the fiscal year).

Residual (Noise): The random variations left over after Trend and Seasonality are removed.

3. Risk & Volatility Metrics (get_volatility_stats)
Measures investment risk by analyzing price "bounciness":

Daily Volatility: The standard deviation of daily percentage changes.

Annual Volatility: Scales daily risk to a yearly figure using the square root of time: