
# Excessive I/O

If you have a lot of output, the `-o, -e` are slow.

We can avoid this by manually redirecting the standard in and out.

![[Pasted image 20240501093451.png]]

One caveat is that it depends on the file system:
	For some fast systems it might not be an issue, but in general you should not print, but pipe the output into files.

# Duplicate I/O

![[Pasted image 20240501093759.png]]

tee prints to screen and writes to file, which is redundant for the hpc as we are already writting to a file.

Moral of the store only log one place.

# Spamming bjobs or bstat

![[Pasted image 20240501094000.png]]

# Too many files in one folder

If you have thousands of files this can cause slowdowns

Solution: create sub-folders

Example of slowdown

![[Pasted image 20240501094158.png]]

The slow down depends on the OS'es file system.

# Multi-threading/processing

Flavors:

	Too many threads

	Too few threads

## Example too many threads

![[Pasted image 20240501094643.png]]

![[Pasted image 20240501094651.png]]

The package might not respect the amount of cores, we have been allocated, we might also multiprocess on top of multiprocessing, thus will spawn out be careful

Solution:

![[Pasted image 20240501094804.png]]

__Alarm bell adding more cores doesn't yield speed up.__

## Too few threads

![[Pasted image 20240501094943.png]]

In numpy

![[Pasted image 20240501094959.png]]

