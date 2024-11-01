import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

def main():
    df = pd.read_csv('PS_dataset.csv')
    q= df['quality']
    q= sorted(q)
    a=len(q)
    b = q[a-1] - q[0] +1
    qualityscores =count(q,b)
    quality = []
    for i in range(b):
        x = q[0] + i
        quality.append(x)
    #creation of bar plot and styling 
    plt.style.use('dark_background')
    plt.bar(quality,qualityscores,color='red',width=0.4,)
    plt.title("quality of diffrent wines")
    plt.xlabel(" rating of quality")
    plt.ylabel(" no of wines ")
    for i in range(b):
        plt.annotate(str(qualityscores[i]),xy=(quality[i],qualityscores[i]),ha='center',va='bottom')
    plt.show()
    
def count(q,b): 
    qs= []
    for i in range(b):
        c=0
        for j in q:
            if j == q[0]+ i:
               c += 1
        qs.append(c)
    
    return qs

main()