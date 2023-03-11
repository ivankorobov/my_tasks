class Primes:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.prime_number = []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i <= self.n:
            self.i += 1
            for prime in self.prime_number:
                if self.i % prime == 0:
                    break
            else:
                self.prime_number.append(self.i)
                return self.i
        raise StopIteration


prime_nums = Primes(50)
for i in prime_nums:
    print(i, end=' ')
