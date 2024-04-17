
# Single Job Script

![[Pasted image 20240417083507.png]]
We will revise this job script


# Job Arrays

![[Pasted image 20240417084012.png]]

![[Pasted image 20240417084041.png]]

![[Pasted image 20240417084227.png]]

> The job indices can't start from 0.

![[Pasted image 20240417084319.png]]

## Monitoring job arrays

`bjobs -A` bjobs array
![[Pasted image 20240417084642.png]]

you can kill the all the jobs with the job id, or index into the job id to kill specific ones.
The indexing follows the same syntax as before.
### Job states

![[Pasted image 20240417084933.png]]

The susp are for suspension.

If a job isn't done, but exit it means it crashed.

### Peeking at jobs

![[Pasted image 20240417085133.png]]


# Job dependencies

## Example use cases

![[Pasted image 20240417090149.png]]

## The bsub option

![[Pasted image 20240417090455.png]]

? does the hpc queue schedule dependencies ? -> `We wait for a spot on the queue each time.`

We can also specify id

![[Pasted image 20240417090622.png]]

We have a few options for when to start

![[Pasted image 20240417090655.png]]

Ended also covers done, so it is if it finishes for any reason.

? if the job exits, will it still be pending ? -> ! Yes it will !

> There are more options, but these are the ones we need for now.

`He was unsure about if a job crashes which you are waiting for to be done, and you then submit a job with the same name, which is done this time, if the dependent job will start.`


### Job dependencies in arrays


#### Waiting for the full array

![[Pasted image 20240417091012.png]]

#### Waiting for specific elements

![[Pasted image 20240417091105.png]]

Notice that job 2 is now also an array.

## Monitoring job dependencies

![[Pasted image 20240417091443.png]]

The `-c` options shows us a job's children.

![[Pasted image 20240417091551.png]]

If we want the entire chain we can specify `-r` for recursive followed by a number, if we want to specify the depth `-r<i>`.

### monitoring arrays


![[Pasted image 20240417091846.png]]

look with job id are index into the array.


# Additional documentation

![[Pasted image 20240417091219.png]]
