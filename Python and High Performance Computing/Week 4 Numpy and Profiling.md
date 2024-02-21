
# Numpy

## Deconstructing the numpy array

![[Pasted image 20240221084225 1.png]]

### Strides
The strides tell us how many bytes we have to have to get the next element in the corresponding dimension.

The most **cache** **efficient** operations are the ones, which have to jump the least in the strides.

__Column jump__

![[Pasted image 20240221084409 1.png]]

__Row__

![[Pasted image 20240221084510 1.png]]

#### Indexing

![[Pasted image 20240221085422 1.png]]

##### Smart stride indexing

![[Pasted image 20240221085634 1.png]]

how does this look for non int32, then you have to look at how many bytes the data type is.

If possible we should work with views, because we don't have to spend operations on copying data.

> In traditional python arrays, they most likeli store pointers to everything, so we can still do striding
### Views vs Copys

![[Pasted image 20240221084744 1.png]]

Most reshapes can be done by changing the strides.
Transpose too. This makes these operations really fast, `O(1)`.

Views share memory.

#### Example of non possible view reshape

Going from a to b will make copy

![[Pasted image 20240221085059 1.png]]


#### Got ya!! for reshape

reshape might not maintain order.

### Broadcasting 

How it works numpy, torch, tf, jax.

Steps:

- Right align all shapes
- Left pad the shortest with ones until the shapes match in length
- If a dimension has shape one and the corresponding shape doesn't, then make the 1 have that length.
- If the elements now match, then we are good.

The reshaping here just changes the stride and doesn't copy any data.
##### To help us broadcast how we want to can None index to add dimensions

![[Pasted image 20240221091929 1.png]]

##### We can ask numpy to show us the broadcasted result

![[Pasted image 20240221092115 1.png]]

How do we visualize what it means the new strides?
> I suppose we can try indexing or striding.

Can we maintain optimal striding?
> No not in numpy, when we perform an opperation between the two, as numpy will allocate the full memory.
>> But there are other frameworks that do this and they work with lazy exectuion.

## The backend of numpy

![[Pasted image 20240221094506 1.png]]

The different backends impact the speed, but not that much

![[Pasted image 20240221094949 1.png]]
![[Pasted image 20240221095000 1.png]]

# Profiling - Measuring the time things take

## cProfile

### Function profiling

The command 

![[Pasted image 20240221095342 1.png]]

The output

![[Pasted image 20240221095632 1.png]]

### Line profiling

Call requires decorator.

![[Pasted image 20240221095941 1.png]]

Output

![[Pasted image 20240221095959 1.png]]
