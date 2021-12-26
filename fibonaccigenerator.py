import time
def timeit(func):
    def timed(*args, **kwargs):
        starttime = time.perf_counter()
        result = func(*args, **kwargs)
        endtime = time.perf_counter()
        d = endtime-starttime
        print(f"Starting time: {starttime}")
        print(f"Ending time: {endtime}")
        print(f"Time taken: {d}")
        return result
    return timed
@timeit
def fib(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
n=int(input("ENTER NUMBER OF FIBONACCI NUMBERS TO GENERATE:"))
for i in fib(n):
    print(i)
