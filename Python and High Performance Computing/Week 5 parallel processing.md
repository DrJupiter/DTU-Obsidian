
# Asynchronous programming

### Concurrency
The idea of doing things at different times in different order, essentially doing as much as we can.

#### Callbacks and Futures

A way to achieve concurrency is through __callbacks__.
Callbacks are a set of instructions to execute after we are done waiting.

__Futures__ are a way to keep track of the result/return value of an asynchronous call.

![[Pasted image 20240228091732.png]]
![[Pasted image 20240228091739.png]]
![[Pasted image 20240228091807.png]]
![[Pasted image 20240228091834.png]]

This code makes sure something executes when the future has received the result.

#### The event loop

Is a loop where everything has two layers.
The first is a ping when done, and the second is what to do when done.
We then continuously loop over the event loop and listen for pings.

##### An event loop is exposed through making it yourself or the asyncio framework

![[Pasted image 20240228093105.png]]

### Coroutines

**Coroutines** are [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program") components that allow execution to be suspended and resumed, generalizing [subroutines](https://en.wikipedia.org/wiki/Subroutine "Subroutine") for [cooperative multitasking](https://en.wikipedia.org/wiki/Non-preemptive_multitasking "Non-preemptive multitasking"). Coroutines are well-suited for implementing familiar program components such as [cooperative tasks](https://en.wikipedia.org/wiki/Cooperative_multitasking "Cooperative multitasking"), [exceptions](https://en.wikipedia.org/wiki/Exception_handling "Exception handling"), [event loops](https://en.wikipedia.org/wiki/Event_loop "Event loop"), [iterators](https://en.wikipedia.org/wiki/Iterator "Iterator"), [infinite lists](https://en.wikipedia.org/wiki/Lazy_evaluation "Lazy evaluation") and [pipes](https://en.wikipedia.org/wiki/Pipeline_(software) "Pipeline (software)").

They have been described as "functions whose execution you can pause".[[1 Fundamentals of vector spaces over a field]](https://en.wikipedia.org/wiki/Coroutine#cite_note-1)

![[Pasted image 20240228093752.png]]
![[Pasted image 20240228093804.png]]

## Making code async

We want to use non-blocking code, and thus async's inner framework which builds on the principals previously discussed.

# Reactive programming

![[Pasted image 20240228095127.png]]


## Amdahl's law


![[Pasted image 20240228090104.png]]

![[Pasted image 20240228095502.png]]
The execution time of the whole task before the improvement of the resources of the system is denoted as `T`.


He calss F the parallel fraction, it is p in the other definition.

### Example


![[Pasted image 20240306091148.png]]


Here F = (100/(100+20)), so sum of all paralizable tasks divided by sum of all tasks.

We can then insert this into formula S(4), S($\infty$), to get the theoretical speed ups.

Finally in d we consider the speed up of S(num p) vs 5 sec and see it is more worth to get the 5 seconds.


