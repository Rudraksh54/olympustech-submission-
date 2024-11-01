import pandas as pd

def main():
    df = pd.read_csv('PS_dataset.csv')
    print("max value of each column is as folllows")
    print(df.max())
    print("min value of each comlumn is as follows")
    print(df.min())
    print("mean value of citric acid column is as follows")
    print(df[['citric acid']].mean())
main()