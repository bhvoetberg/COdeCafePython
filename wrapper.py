def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("Decorating this function")
        return return_value

    return wrapper


@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}"


print(hello("Mike"))


# Other example


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
            print(f"{fname} returned value {value}")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(4, 5))
