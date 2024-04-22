import sys
import pandas as pd

path = sys.argv[1]
df = pd.read_csv(path)

def total_precip(df):
    return df[df['parameterId'] == 'precip_past10min']['value'].sum()

print(total_precip(df))