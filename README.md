# TimeSeries_Analysis_Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

---

## Overview
The `analyzer` package provides a modular pipeline for **Time Series Analysis**, specifically designed for financial datasets like ADANIPORTS. It automates the process of transforming raw CSV data into meaningful statistical insights and visualizations.

This package focuses on:
1. **Data Preprocessing:** Handling missing dates, frequency reindexing, and outlier removal.
2. **Statistical Analysis:** Stationarity testing (ADF/KPSS) and signal decomposition.
3. **Visualization:** Heatmaps, ACF/PACF plots, and rolling statistics.

---

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/RahimiLili/TimeSeries_Analysis_Project.git
   cd TimeSeries_Analysis_Project
   ```

2. **Install with uv**
   ```bash
   uv pip install -e .
   ```

---

## Usage
### CLI Execution
Run the full analysis pipeline with one command:
```bash
uv run -m analyzer
```

### Notebook Example
See notebooks/Timeseri_analysis.ipynb for details

---

## Modules

###  Preprocessor Module
This module cleans and prepares time series data for analysis.
1. **`clean_headers() `**: Removes leading/trailing spaces from column names
2. **`process_data()`**: Duplicate handling, and ensures a continuous daily frequency using time-interpolation.
3. **`handle_outliers()`**: Identifies price anomalies using the IQR method and replaces them with median values.



###  Analyzer Module
This module provides statistical tests (ADF, KPSS) and signal 
decomposition specifically tuned for financial datasets like ADANIPORTS.
1. **`adf_test()` / `kpss_test()`**: Performs dual stationarity checks to determine if the series is predictable.
2. **`decompose_signal()`**: Breaks the data into **Trend**, **Seasonality**, and **Residuals**.
3. **`get_volatility_stats()`**: Calculates annualized risk based on daily returns.
4. **`daily_returns() `** : Calculates daily returns from a price series



###  Visualizer Module
Visualizer Module for Time Series Analysis with plotting for the project.
1. **`plot_data()`**: Plot time series data
2. **`plot_seasonal_heatmap()`**: Visualizes heatmap of average price by Month and Year.
3. **`plot_pacf_acf()`**: Generates plots of autocorrelation and partial autocorrelatio to help identify ARIMA model parameters.
4. **`plot_rolling_stats()`**: Shows the original data vs. a 30-day moving average.
5. **`plot_decomposition()`**: Plots the 4 components: Observed, Trend, Seasonal, and Residual.
6. **`plot_daily_returns_distribution()`**: Plot distribustion of daily returns


---
**Author:** Leila Rahimiyadkuri  
**Course:** Introduction to Python, WS25/26 - TU Dortmund  

