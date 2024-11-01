import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

def main():
    df = pd.read_csv('PS_dataset.csv')
    x = df['alcohol']
    plt.style.use('dark_background')
    sns.histplot(x,bins=30,kde=True,color='skyblue',edgecolor='black')
    plt.ylabel("no of wines")
    plt.title("distribution of alcohol")
    plt.show()
main()