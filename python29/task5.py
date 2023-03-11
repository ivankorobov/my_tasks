import time
import functools
def how_m_sec_to_slow(num=1):
    def slow_slow_func(func):

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            start = time.time()
            time.sleep(num)
            func()
            end = time.time()
            print(f"и так каждые {round(end - start, 3)} секунд")

        return wrapped_func
    return slow_slow_func

sec_num = int(input("На сколько замедлить функцию? "))
@how_m_sec_to_slow(sec_num)
def main_func():
    print("?¿?¿создали ⚇ видимость ⚇ работы?¿?¿")

main_func()

