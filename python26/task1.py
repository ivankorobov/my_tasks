from random import randint
items = [randint(-10, 10) for _ in range(randint(0, 20))]
iterator = items.__iter__()  ##iter(items)
while True:
    try:
        print(iterator.__next__()) #next(iterator)
    except StopIteration:
        print("Элементы закончились.")
        break