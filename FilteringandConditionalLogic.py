import pandas as pd 

def main():
    df = pd.read_csv('PS_dataset.csv')
    q=df.loc[(df['pH']>3.5) & (df['alcohol']>10)]
    q=q['quality']
    avg = sum(q)/len(q)
    print(f"the avg value of quality for wines with a pH greater than 3.5 and alcohol content greater than 10 is {avg}")
main()