import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df=pd.read_csv('PS_dataset.csv')
    sns.heatmap(df.corr(numeric_only=True))
    plt.show()

main()