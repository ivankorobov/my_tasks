class Fibonacci:
    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration
        self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val

        return self.cur_val


fic_iterator = Fibonacci(10)
for i in fic_iterator:
    print(i)

print(8 in fic_iterator)