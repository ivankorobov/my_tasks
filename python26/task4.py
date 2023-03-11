import random

elen_num = int(input("Кол-во элементов: "))

class NewIter():

    def __init__(self, num):
        self.last = 0
        self.end = num
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random.random()
        return self.last


my_iter = NewIter(num=elen_num)
print("Элементы итератора:")
for i in my_iter:
    print(i)