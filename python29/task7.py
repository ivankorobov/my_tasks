from datetime import datetime


def logged(func):
    def wrapped(*args, **kwargs):
        print('Запуск функции произошел в:', datetime.now())
        return func(*args, **kwargs)
    return wrapped

def decorator(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue
        a = getattr(cls, i_method)
        if hasattr(a, '__call__'):
            decorated_a = logged(a)
            setattr(cls, i_method, decorated_a)
    return cls

@decorator
class A:
    def test_sum_1(self):
        print("тут метод test_sum_1")
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(1000)])

        return result
    
A().test_sum_1()