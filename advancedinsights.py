import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#creating new coloumn
df =pd.read_csv('PS_dataset.csv')
df['acidity_ratio'] = df['fixed acidity']/df['volatile acidity']
print(f"mean value of acitdity ratio coloum is {df['acidity_ratio'].mean()}")

#violinplot
sns.violinplot(x=df['quality'],y=df['alcohol'])
plt.show()

#pairplot
sns.pairplot(df,markers='.')
plt.show()

#heatmap
sns.heatmap(df.corr(numeric_only=True))
plt.show()
print("a lot can be conculed about the corealation of each attribute to another for expample pH decreases at a fast rate as fixed acidity inc (as color is black)")

#boxplot
sns.boxplot(x=df['quality'],y=df['chlorides'])
plt.show()
print("as seen from boxplot wines with quality score of 5 have unsually high chloride values")