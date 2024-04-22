
# Chunking

## In pandas

```python

import pandas as pd

n = 100 # The number of rows to load in at a time

# An iterator over the entire csv which returns data frames
dataframes = pd.read_csv('path.csv', chunksize=n)
# the dataframes doesn't know how long it is.

# The iterator will reset after each loop

for df in dataframes:
	print(df)

for df in dataframes:
	print(df) # same output in the same sequence as before



```

## In pyarrow parquet

```python
import pyarrow.parquet as pq

parquet_datafile = pq.ParquetFile("path.parquet")

parquet_datafile.num_row_groups # -> the number of groups, which might all have variable lenght

# Convert a group to pandas

dataframe = parquet_datafile.read_row_group(0).to_pandas()
```

# Memory mapping

![[Pasted image 20240417140730.png]]

## in numpy 

```python
import numpy as np

# Instancite an array on the disk
array_on_disk = np.memmap('filename.raw', mode='w+', shape=(10,10), dtype='float64')

# Opperations on the array will change the file too
array_on_disk[0,0] = 2

# Read only array on the disk
array_readonly = np.memmap('readonly.raw', mode='r')

# ! Raises an error
array_readonly[0] += 2 # -> ValueError: assignment destination is read-only

# Read and Write

array_readandwrite = np.memmap('readandwrite.raw', mode='r+')
# Has a shape, but with garbage data, as we haven't filled in anything yet
# ! Thus we should always specify a shape and data type.
```

# Compressed format: Zarr

![[Pasted image 20240417141436.png]]

![[Pasted image 20240417142120.png]]
![[Pasted image 20240417142256.png]]

## Chunking in Zarr

```python
import zarr
empty = zarr.open('empty.zarr', mode='w', shape=(100,100), chunks=(20,20))
```

![[Pasted image 20240417142518.png]]

We can build a dataset in a folder like structure in Zarr.


### Indexing

![[Pasted image 20240417143836.png]]

![[Pasted image 20240417143910.png]]
