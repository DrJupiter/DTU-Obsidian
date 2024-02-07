
## Global interpreter lock (GIL)

Makes it so threads can only execute python code once at a time. They can do I/O calls asynchronously, but will be joined concurrently to avoid race conditions.

## Threading 

Runs on the some process and shares memory.

## Multiprocessing

Runs on multiple cores, but requires sending all data etc.
Is good for CPU heavy tasks, if the amount of setup doesn't kill the performance.


