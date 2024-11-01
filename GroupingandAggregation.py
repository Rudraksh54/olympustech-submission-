import pandas as pd

def main():
    df = pd.read_csv('PS_dataset.csv')
    b=df.groupby(['quality']).median()
    df['indexquality']=df['quality']
    a= df.groupby(['quality']).mean().sort_values('alcohol',ascending=False)
    print(f"quality score of {int(a.iloc[0].indexquality)} has the highest average alcohol content")
    a=a.drop(columns=['indexquality'])
    print("mean values of all columns is ")
    print(a)
    print("median values of all columns is ")
    print(b)
    
main()