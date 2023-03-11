import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        return 0
def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError:
        return 0

with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as file_2:
    try:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            file_2.write(f"{str(my_list)}\n")
    except ValueError:
        print("Каждая координата должна являться цифрой.")
