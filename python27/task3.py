from typing import Callable, Any
def do_twice(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapped_func

@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))

greeting('Tom')