import numpy as np
import seaborn as sns
import ppscore as pps
import matplotlib.pyplot as plt


def pps_matrix(df):
    # Calculate pps
    pps_matrix = pps.matrix(df)
    # Prepare data to pivot table
    pps_pivot = pps_matrix.pivot('x', 'y', 'ppscore')
    pps_pivot.index.name, pps_pivot.columns.name = None, None
    # Plot
    plt.figure(figsize=(10, 4))
    sns.heatmap(pps_pivot, annot=True, cmap='YlGn')
    plt.title('Predictive Power Score Matrix', fontsize=16);
    plt.show()


def missing_vals(df):
    sns.heatmap(df.isnull(), yticklabels=False, cbar=False)
    plt.title('Missing values', fontsize=16)
    plt.show()