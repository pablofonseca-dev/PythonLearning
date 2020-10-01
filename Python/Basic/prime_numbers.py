def print_prime_numbers(lim):
    primes = []
    for num in range(1, lim + 1):
        prime = True
        for val in range(2, lim + 1 // 2):
            if num % val == 0 and num != val:
                prime = False
                break
        if(prime):
            primes.append(num)
    return primes

print(print_prime_numbers(1000))