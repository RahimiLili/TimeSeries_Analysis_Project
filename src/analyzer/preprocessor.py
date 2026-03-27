"""
Preprocessing Module for Time Series Data.
This class cleans, reindexes, and handles outliers for the ADANIPORTS dataset.
"""

import pandas as pd
import numpy as np

class DataPreprocessor:
    """
    A class to clean and prepare time series data for analysis.
    """

    def __init__(self, df, date_col='Date', target_col='Close'):
        self.df = df.copy()
        self.date_col = date_col
        self.target_col = target_col

    def clean_headers(self):
        """Removes leading/trailing spaces from column names."""
        self.df.columns = self.df.columns.str.strip()
        return self.df

    def process_data(self):
        """
        The main pipeline: cleans headers, converts dates, 
        reindexes to daily frequency, and fills gaps.
        """
        self.clean_headers()
        
        # 1. Map column names (Case-insensitive)
        cols_map = {c.lower(): c for c in self.df.columns}
        if self.target_col.lower() in cols_map:
            actual_target = cols_map[self.target_col.lower()]
        else:
            raise KeyError(f"Column '{self.target_col}' not found.")
        
        # 2. Convert Date column
        self.df[self.date_col] = pd.to_datetime(self.df[self.date_col])
        
        # 3. Handle Duplicates and Aggregation
        # Groups by date and calculates mean for numbers, first for others
        self.df = self.df.groupby(self.date_col).agg({
            col: ('mean' if pd.api.types.is_numeric_dtype(self.df[col]) else 'first')
            for col in self.df.columns if col != self.date_col
        })
        
        # 4. Reindex to daily ('D') frequency to ensure no missing days
        self.df = self.df.asfreq('D')
        
        # 5. Fill numeric gaps with time-based interpolation
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_cols] = self.df[numeric_cols].interpolate(method='time')
        
        # 6. Fill categorical gaps (like Symbol) with Forward Fill
        self.df = self.df.ffill()
        
        # Reset index to put 'Date' back as a column
        self.df = self.df.reset_index()
        return self.df

    def handle_outliers(self, column=None):
        """
        Detects outliers using the IQR method and replaces them with the median.
        """
        # If no column is specified, use the main target column
        col_to_fix = column if column else self.target_col
        
        if col_to_fix not in self.df.columns:
            return self.df
            
        q1 = self.df[col_to_fix].quantile(0.25)
        q3 = self.df[col_to_fix].quantile(0.75)
        iqr = q3 - q1
        
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        median_val = self.df[col_to_fix].median()
        
        # Replace extreme values with the median
        self.df.loc[self.df[col_to_fix] > upper_bound, col_to_fix] = median_val
        self.df.loc[self.df[col_to_fix] < lower_bound, col_to_fix] = median_val
        
        return self.df