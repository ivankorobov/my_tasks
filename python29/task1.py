from contextlib import contextmanager
from collections.abc import Iterator
@contextmanager
def next_num(num) -> Iterator[int]:
    print('Входим в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print('Обнаружена ошибка:', exc)
    finally:
        print('Код в любом случае выполнится')
    print('Выход из функции')


with next_num(0) as next:
    print('Следующее число:', next)
    print(10 / next)