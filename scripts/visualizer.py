#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_scatter(df, x_col, y_col):
    """Plots a scatter plot for the given variable(s)."""
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.title(f'Scatter Plot of {x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_histogram(df, col_name):
    """Plots a histogram for the given variable(s)."""
    sns.histplot(df[col_name], kde=True)
    plt.title(f'Histogram of {col_name}')
    plt.xlabel(col_name)
    plt.ylabel("Count")
    plt.show()

def plot_count(df, cat_col):
    """Plots a count plot for the given variable(s)."""
    sns.countplot(x=cat_col, data=df)
    plt.title(f'Count Plot of {cat_col}')
    plt.xlabel(cat_col)
    plt.ylabel("Count")
    plt.show()

def correlation_matrix(df):
    """"Plots a heatmap plot for the given dataframe."""
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplot(df, var_x, var_y=None, hue_var=None):
    """
    Plots a boxplot for the given variable(s).
    
    Parameters:
    - df: DataFrame containing the data.
    - var_x: Variable to plot on the x-axis.
    - var_y: Optional variable to plot on the y-axis for grouped boxplots.
    - hue_var: Optional variable to differentiate boxplots by hue.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))
    # Determine the type of boxplot based on the input parameters
    if var_y is None:
        # Simple boxplot
        sns.boxplot(x=var_x, data=df)
    else:
        # Grouped boxplot
        sns.boxplot(x=var_x, y=var_y, data=df)
        if hue_var is not None:
            # Boxplot with hue differentiation
            sns.boxplot(x=var_x, y=var_y, hue=hue_var, data=df)
    
    # Display the plot
    plt.title(f'Boxplot of {var_x}')
    plt.xlabel(var_x)
    if var_y is not None:
        plt.ylabel(var_y)
    plt.show()
