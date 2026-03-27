import pandas as pd
import numpy as np

def clean_headers(df):
    """Cleans all column names (removes spaces, fixes casing)."""
    df.columns = df.columns.str.strip()
    return df

def fill_gaps(df, date_col='Date', target_col='Close'):
    """Ensures daily frequency while keeping all numeric columns."""
    df = clean_headers(df)
    
    # 1. Case-insensitive check (find 'Close' even if it's 'close')
    cols_map = {c.lower(): c for c in df.columns}
    if target_col.lower() in cols_map:
        target_col = cols_map[target_col.lower()]
    else:
        raise KeyError(f"Column '{target_col}' not found. Available: {list(df.columns)}")
    
    # 2. Convert Date
    df[date_col] = pd.to_datetime(df[date_col])
    
    # 3. Handle Duplicates safely (keeps all numeric columns)
    # We group by Date and take the mean of numbers, and first of objects
    df = df.groupby(date_col).agg({
        col: ('mean' if pd.api.types.is_numeric_dtype(df[col]) else 'first')
        for col in df.columns if col != date_col
    })
    
    # 4. Reindex to daily frequency
    df = df.asfreq('D')
    
    # 5. Fill the gaps using interpolation for numbers
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].interpolate(method='time')
    
    # 6. Fill non-numeric gaps (like 'Symbol') with the previous value
    df = df.ffill()
    
    return df.reset_index()

def handle_outliers(df, column='Close'):
    """Replaces extreme outliers with the median of that column."""
    df = df.copy()
    if column not in df.columns:
        return df
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    df.loc[df[column] > (q3 + 1.5 * iqr), column] = df[column].median()
    df.loc[df[column] < (q1 - 1.5 * iqr), column] = df[column].median()
    return df