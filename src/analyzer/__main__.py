"""
Entry point for the Time Series Analysis project.
Executes the full pipeline: Load -> Clean -> Analyze -> Visualize.
"""

import pandas as pd
from .preprocessor import DataPreprocessor
from .analyzer import TimeSeriesAnalyzer
from .visualizer import TimeSeriesVisualizer

def main():
    print("--- ADANIPORTS Time Series Analysis Starting ---")
    
    # 1. Load Data
    # Path assumes we are running from the root of the project
    try:
        df_raw = pd.read_csv("data/ADANIPORTS.csv")
    except FileNotFoundError:
        print("Error: ADANIPORTS.csv not found in data/ folder.")
        return

    # 2. Preprocess
    print(":::::Step1::::: Cleaning data and handling gaps...")
    preprocessor = DataPreprocessor(df_raw)
    df_clean = preprocessor.process_data()
    df_clean = preprocessor.handle_outliers()

    # 3. Analyze
    print("::::Step2::::: Running statistical tests (ADF, Volatility,..)...")
    analyzer = TimeSeriesAnalyzer(df_clean)
    
    adf_res = analyzer.adf_test()
    print(f"ADF Test Stationary: {adf_res['is_stationary']} (p={adf_res['p-value']:.4f})")
    
    vol = analyzer.get_volatility_stats()
    print(f"Annualized Volatility: {vol['Annual Volatility']:.2%}")

    # 4. Visualize
    print("::::::Step3::::: Generating plots...")
    viz = TimeSeriesVisualizer(df_clean)
    
    # This will save 'rolling_stats.png' and show the plot
    viz.plot_rolling_stats(window=30)
    
    # This will save 'seasonal_heatmap.png'
    viz.plot_seasonal_heatmap()
    
    # Decompose and show
    decomp = analyzer.decompose_signal()
    
    fig = decomp.plot()
    fig.savefig("decomposition_plot.png")
    

    viz.plot_decomposition(decomp)


    print("--- Analysis Complete! Files saved to root directory. ---")

if __name__ == "__main__":
    main()