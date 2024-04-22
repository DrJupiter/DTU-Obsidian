# %%
import pandas as pd

df = pd.read_csv('/home/kjb/Desktop/DTU Semester 8/DTU-8-HPC-PYTHON/data/dmi/2023_01.csv.zip')
print(df)
# %%

def df_memsize(df):
    return df.memory_usage(deep=True).sum()

def summarize_columns(df):
    print(pd.DataFrame([
    (
    c,
    df[c].dtype,
    len(df[c].unique()),
    df[c].memory_usage(deep=True) // (1024**2)
    ) for c in df.columns
    ], columns=['name', 'dtype', 'unique', 'size (MB)']))
    print('Total size:', df.memory_usage(deep=True).sum() / 1024**2, 'MB')
# %%

def reduce_dmi_df(df):
    df["observed"] = pd.to_datetime(df["observed"])
    df["created"] = pd.to_datetime(df["created"], format='mixed')
    df['coordsx'] = df['coordsx'].astype('float16')
    df['coordsy'] = df['coordsy'].astype('float16')
    df['value'] = df['value'].astype('float32')
    df['stationId'] = df['stationId'].astype('int16')
    df['parameterId'] = df['parameterId'].astype('category')
    return df
# %%

from pyarrow import csv
from pyarrow import parquet
def pyarrow_load(path):
    return csv.read_csv(path)#.to_pandas()
# %%

def pyarrow_save(table, path):
    parquet.write_table(table, path)

table = pyarrow_load('/dtu/projects/02613_2024/data/dmi/2023_01.csv.zip')
pyarrow_save(table, '/dtu/projects/02613_2024/data/dmi/2023_01.parquet')

def total_precip(df):
    return df[df['parameterId'] == 'precip_past10min']['value'].sum()

print(total_precip(df))