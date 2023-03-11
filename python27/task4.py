import time


def timer(func):

    def wrapped_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Функция работала {round(end - start, 3)} секунд")

        return end - start

    return wrapped_func

@timer
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()