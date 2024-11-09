import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        total = time.time() - start
        print("Time: ", total)
        return return_value

    return wrapper


@timer
def summer(x, y):
    time.sleep(2)
    return x + y


x = summer(3, 4)
print(x)


# other example

# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @decorator
# def say_whee():
#     print("Whee!")
#
#
# # @decorator is short for:
# # say_whee = decorator(say_whee)
# say_whee()
