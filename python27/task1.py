x = int(input("X: "))


def func_1(x):
    return x + 10

res1 = func_1(x)


def func_2(func, *args, **kwargs):
    result = func(*args, **kwargs)
    return result * result


print(func_2(func_1, x))