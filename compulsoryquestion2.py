import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def main():
    df = pd.read_csv('PS_dataset.csv')
    x = df['alcohol']
    y = df['pH']
    c=np.corrcoef(x,y)
    if any(np.isnan(list(c))):
        print(c)
    plt.style.use('dark_background')
    plt.scatter(x,y,s=1,marker='.')
    plt.xlabel("alcohol")
    plt.ylabel("pH")
    plt.title("alcohol vs pH scatter plot")
    plt.show()

main()  