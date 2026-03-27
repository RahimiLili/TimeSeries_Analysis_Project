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
3. **Professional Visualization:** Heatmaps, ACF/PACF plots, and rolling statistics.

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
Explore the data interactively:
```python
from analyzer.preprocessor import DataPreprocessor
# (See notebooks/analysis.ipynb for details)
```

---

## Modules

### 🛠 DataPreprocessor Module
1. **`process_data()`**: Performs header cleaning, duplicate handling, and ensures a continuous daily frequency using time-interpolation.
2. **`handle_outliers()`**: Identifies price anomalies using the IQR method and replaces them with median values.

**Example:**
```python
DataPreprocessor(df).process_data()
```

###  TimeSeriesAnalyzer Module
1. **`adf_test()` / `kpss_test()`**: Performs dual stationarity checks to determine if the series is predictable.
2. **`decompose_signal()`**: Breaks the data into **Trend**, **Seasonality**, and **Residuals**.
3. **`get_volatility_stats()`**: Calculates annualized risk based on daily returns.

**Example:**
```python
TimeSeriesAnalyzer(df).adf_test()
```

###  TimeSeriesVisualizer Module
1. **`plot_seasonal_heatmap()`**: Visualizes monthly price patterns over the years.
2. **`plot_pacf_acf()`**: Generates plots to help identify ARIMA model parameters.
3. **`plot_rolling_stats()`**: Shows the original data vs. a 30-day moving average.

**Example:**
```python
TimeSeriesVisualizer(df).plot_rolling_stats(window=30)
```

---
**Author:** Leila Rahimiyadkuri  
**Course:** Final Project - TU Dortmund  
**Deadline:** 31.03.2026
