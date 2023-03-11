import functools
global_cout = {}

def counter(func):
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        global_cout[func.__name__] = global_cout.get(func.__name__, 0) + 1
        return func(*args, **kwargs)

    wrapped_func.count = 0
    return wrapped_func

@counter
def new_func():
    print("TESTIN")


@counter
def new_func2():
    print("TESTIN")


print(global_cout, new_func.count, new_func2.count)
new_func()
print(global_cout, new_func.count, new_func2.count)
new_func2()
print(global_cout, new_func.count)
for i in dir("."):
    print(i)