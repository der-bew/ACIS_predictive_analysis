#!/usr/bin/env python3

import pandas as pd 
import numpy as np

class Handler():
    def __init__(self, df):
        self.df = df
    
    def data_overview(self):
        print(f"Number of rows: {len(self.df)}")
        print(f"Number of columns: {len(self.df.columns)}")
        print("\nData Types:")
        self.df.dtypes
        print("\nDescriptive Statistics:")
        self.df.describe()
    
    def check_duplicate(self):
        # Identify and report duplicated values
        duplicates = self.df.duplicated()
        print("\nDuplicated values:")
        print(duplicates.sum(), "duplicated rows") 
    
    def calculate_missing_percentage(self):
        # Calculate and return the percentage of missing values in each column
        
        missing_values = self.df.isnull().sum()
        total_rows = len(self.df)
        
        # Correctly calculate the percentage for each column
        missing_values_percentage = (missing_values / total_rows) * 100
        
        # Convert the percentages to string format with 2 decimal places
        missing_values_percentage_str = missing_values_percentage.apply(lambda x: f'{x:.2f}%')
        
        # Concatenate the original missing values counts with their corresponding percentages
        new_df = pd.DataFrame({'Missing Values': missing_values, 'Percentage Missing': missing_values_percentage_str})
        
        print(new_df)


