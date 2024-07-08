# my_iter_list = [17,19,44,66,331,6653,234,675,324,12,375,78,643,132,635,87,98]
# my_iterator = iter(my_iter_list)
# for i in my_iterator:
#     if i % 2 == 0:
#         print("toq emas", i)
#     elif i % 3 == i % i:
#         print("toq emas", i)
#     elif i % 5 == i % i:
#         print("toq emas", i)
#     elif i % 7 == i % i:
#         print("toq emas", i)
#
#     else:
#         print(next(my_iterator),"Toq")

class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    @staticmethod
    def is_prime(n):
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

    def __next__(self):
        self.current += 1
        while self.current <= self.limit:
            if self.is_prime(self.current):
                return self.current
            self.current += 1
        raise StopIteration


limit = int(input("Sonni kiriting:"))
primes = PrimeIterator(limit)

print(f"Tubsonlar {limit}:")
for prime in primes:
    print(prime)
