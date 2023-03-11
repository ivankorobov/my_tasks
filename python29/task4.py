import functools
from typing import Callable, Any
def do_twice_w_num(num):

    def do_twice(func: Callable) -> Callable:

            @functools.wraps(func)
            def wrapped_func(*args, **kwargs) -> Any:
                for _ in range(num):
                    func(*args, **kwargs)

            return wrapped_func

    return do_twice

numb = int(input('Сколько раз: '))
text = input("Что: ")

@do_twice_w_num(numb)
def greeting(name):
    print('Привет, {name}!'.format(name=name))

greeting(text)
