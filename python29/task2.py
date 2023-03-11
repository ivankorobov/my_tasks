import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)

with timer() as t1:
    print('TEST 1')
    test = 100 * 100 ** 1000000
with timer() as t2:
    print('TEST 1')
    test2 = 100 * 100 ** 1000000
    test2 += 'abc'
with timer() as t3:
    print('TEST 1')
    test3 = 100 * 100 ** 1000000