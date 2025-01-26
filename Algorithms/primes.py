def prime_numbers(limit: int):
    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


print(prime_numbers(100))