import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

def main():
    df= pd.read_csv('PS_dataset.csv')
    a= df['quality']
    b= df['residual sugar']
    sns.boxplot(x=a,y=b)
    plt.title("comparing the spread of residual sugar values grouped by quality score")
    plt.show()
main()