# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import re

def preprocess_data(df):
    df = df[['Description', 'Amount']].dropna()
    df['Description'] = df['Description'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', x))
    df['Description'] = df['Description'].str.lower()
    return df

def plot_category_distribution(df):
    cluster_totals = df.groupby('Cluster')['Amount'].sum().sort_values()
    fig, ax = plt.subplots()
    cluster_totals.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_xlabel("Total Spending")
    ax.set_ylabel("Cluster")
    ax.set_title("Spending by Cluster")
    return fig
