def is_prime(n):
    """Tubmi yoki tubmasligini tekshiradigan skript."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit):
    """malum bir bolgan songacha generator"""
    n = 2
    while n <= limit:
        if is_prime(n):
            yield n
        n += 1


limit = 100
primes = prime_generator(limit)

print(f"Простые числа до {limit}:")
for prime in primes:
    print(prime)
