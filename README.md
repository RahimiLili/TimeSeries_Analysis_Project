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
   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)
   cd TimeSeries_Analysis_Project
2.**Install with uv**
    ```bash
    uv pip install -e .
3.**Usage**
    **CLI Execution**
    Run the full analysis pipeline with one command:
    ```bash
    uv run -m analyzer

    **Notebook Example**
    Explore the data interactively:
    ```bash
    from analyzer.preprocessor import DataPreprocessor
    # (See notebooks/analysis.ipynb for details)