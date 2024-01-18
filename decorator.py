import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time: ", total)
        return rv

    return wrapper


@timer
def summer(x, y):
    time.sleep(2)
    return x + y


x = summer(3, 4)
print(x)