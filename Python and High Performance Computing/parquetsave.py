from pyarrow import csv
from pyarrow import parquet
import sys

path = sys.argv[1]
def pyarrow_load(path):
    return csv.read_csv(path)#.to_pandas()
# %%

def pyarrow_save(table, path):
    parquet.write_table(table, path)

table = pyarrow_load(path)
pyarrow_save(table, path[:-4] + '.parquet')
