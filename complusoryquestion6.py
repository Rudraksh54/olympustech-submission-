import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


def main():
    df = pd.read_csv('PS_dataset.csv')
    df= df.sort_values('total sulfur dioxide')
    a=df['total sulfur dioxide']
    b=df['free sulfur dioxide']
    plt.style.use('dark_background')
    x, y = np.polyfit(a, b, 1)
    plt.plot(a,b,marker='.',markerfacecolor='blue',markeredgecolor='blue',color='skyblue',markersize='1',lw='0.5')
    plt.plot(a, x*a+y,color='white',lw='1')
    plt.xlabel('total sulfur dioxide')
    plt.ylabel('free sulfur dioxide')
    plt.title('the trend of total sulfur dioxide against free sulfur dioxide')
    plt.show()
main()