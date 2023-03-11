PLUGINS = dict()


def register(func):
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Привет, {name}!'


@register
def say_bye(name):
    return f'Пока, {name}!'


print(PLUGINS)
print(say_hello('Tom'))