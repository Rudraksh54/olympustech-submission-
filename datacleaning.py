import pandas as pd
import numpy as np

df = pd.read_csv('PS_dataset.csv')

#finding out How many null values there are in the citric acid column and Replaceing them with the median value of that column. 
ca=(df['citric acid'])
count=0
mca= ca.median()
ca = ca.tolist()
for i in range(len(ca)):
    if np.isnan(ca[i]) :
        count+=1
        ca[i]=mca
print(f"number of null values in citric acid coloum is {count}")
df['citric acid']=ca

    
#Removing all rows where the residual sugar column has null values.
df=df.dropna(subset=['residual sugar'])
    
#Normalizing the fixed acidity column to a range between 0 and 1.
df['fixed acidity']=df['fixed acidity']/df['fixed acidity'].abs().max()

#Removing any duplicate rows in the dataset.
df=df.drop_duplicates(keep=False)
