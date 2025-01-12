import numba
import datetime

@numba.njit
def takes_less(inner: int, outer: int) -> int:
    mult = 1
    for o in range(outer):
        for i in range(inner):
            mult += o*i
    return mult

def takes_more(inner: int, outer: int) -> int:
    mult = 1
    for o in range(outer):
        for i in range(inner):
            mult += o*i
    return mult


inner = 10000
outer = 10000

start_time = datetime.datetime.now()
print(takes_less(inner,outer))
endtime_time = datetime.datetime.now()
print('Took: ', endtime_time - start_time)

start_time = datetime.datetime.now()
print(takes_more(inner,outer))
endtime_time = datetime.datetime.now()
print('Took: ', endtime_time - start_time)



