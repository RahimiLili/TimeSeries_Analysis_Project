"""
Main Entry Point: ADANIPORTS Time Series Analysis Pipeline
---------------------------------------------------------
 The analytical workflow:
1. Data Loading -> 2. Preprocessing -> 3. Statistical Analysis -> 4. Visualization
"""

import pandas as pd
import sys
from .preprocessor import DataPreprocessor
from .analyzer import TimeSeriesAnalyzer
from .visualizer import TimeSeriesVisualizer

def main():
    print("\n" + "="*50)
    print("      ADANIPORTS TIME SERIES ANALYSIS PROJECT      ")
    print("="*50)
    
    # --- STEP 1: DATA Loading ---
    # Path assumes execution from the project root
    file_path = "data/ADANIPORTS.csv"
    try:
        df_raw = pd.read_csv(file_path)
        print(f"[*] Success: Loaded {len(df_raw)} records from {file_path}")
    except FileNotFoundError:
        print(f"[!] Error: {file_path} not found. Ensure the data folder exists.")
        sys.exit(1)

    # --- STEP 2: PREPROCESSING ---
    print("\n[Step 1] Preprocessing: Cleaning and Handling missed...")
    preprocessor = DataPreprocessor(df_raw)
    
    # Chaining the processing steps for a cleaner flow
    df_clean = preprocessor.clean_headers()
    df_clean = preprocessor.process_data()
    df_clean = preprocessor.handle_outliers()
    print("[+] Data cleaned and outliers addressed.")

    # --- STEP 3: STATISTICAL ANALYSIS ---
    print("\n[Step 2] Analysis: Extracting Statistical Insights...")
    analyzer = TimeSeriesAnalyzer(df_clean)
    
    # Run Stationarity Test
    adf_res = analyzer.adf_test()
    status = "STATIONARY" if adf_res['is_stationary'] else "NON-STATIONARY"
    print(f"[*] ADF Test: {status} (p-value: {adf_res['p-value']:.4f})")
    import warnings
    from statsmodels.tools.sm_exceptions import InterpolationWarning
    # This line hides the address and the explanation warning
    warnings.filterwarnings("ignore", category=InterpolationWarning)
    kpss_res = analyzer.kpss_test()
    # status = "STATIONARY" if adf_res['is_stationary'] else "NON-STATIONARY"
    print(f"[*] KPSS Test: {status} (p-value: {kpss_res['p-value']:.4f})")
    

    # Calculate Volatility
    vol = analyzer.get_volatility_stats()
    print(f"[*] Annualized Volatility: {vol['Annual Volatility']:.2%}")

    # Prepare data for visualization
    daily_ret = analyzer.daily_returns()
    decomposition_results = analyzer.decompose_signal()

    # --- STEP 4: VISUALIZATION ---
    print("\n[Step 3] Visualization: Generating Insightful Plots...")
    viz = TimeSeriesVisualizer(df_clean)
    
    # Generate and save all plot artifacts
    viz.plot_data()
    viz.plot_decomposition(decomposition_results)
    viz.plot_seasonal_heatmap()
    viz.plot_pacf_acf()
    viz.plot_daily_returns_distribution(daily_ret)
    viz.plot_rolling_stats(window=30)

    print("\n" + "="*50)
    print("   ANALYSIS COMPLETE: Files saved to Result_Pics folder.   ")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()