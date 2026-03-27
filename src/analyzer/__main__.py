import sys
from .processor import load_and_clean, get_summary, create_plot

def main():
    # This allows the user to pass the CSV filename in the terminal
    # Example: uv run -m analyzer ADANIPORTS.csv
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "ADANIPORTS.csv"
    
    try:
        print(f"--- Loading and Cleaning: {csv_path} ---")
        df = load_and_clean(csv_path)
        
        print("\n--- Data Summary ---")
        print(get_summary(df))
        
        print("\n--- Generating Visualization ---")
        create_plot(df)
        
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")

if __name__ == "__main__":
    main()