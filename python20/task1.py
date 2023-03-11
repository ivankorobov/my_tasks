import random

first = tuple([random.randint(0, 5) for _ in range(10)])
second = tuple([random.randint(-5, 0) for _ in range(10)])
third = first + second
nulls_count = third.count(0)
print(third, nulls_count)