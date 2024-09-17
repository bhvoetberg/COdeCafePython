def return_yield_values(range_):
    for i in range(range_):
        yield i


print(list(return_yield_values(10)))


def fibonacci_generator(stop):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number


print(*fibonacci_generator(1000))

