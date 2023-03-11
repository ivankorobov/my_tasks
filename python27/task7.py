
import functools
from typing import Callable, Any
def do_twice(func: Callable) -> Callable:
    """

    :param func: Функция которую надо изменить
    :return: Измененная функция greeting()
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapped_func

@do_twice
def greeting(name):
    """

        :param func: Имя
        :return: Сообщение приветствия
    """
    print('Привет, {name}!'.format(name=name))

greeting('Tom')
print(do_twice.__doc__)
print(greeting.__name__)
print(greeting.__doc__)