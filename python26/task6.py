def fibonacci(number):
    cur_val = 0
    next_val = 1
    for i in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        """ принудительная остановка """
        if cur_val > 10 ** 6:
            return

def square(nums):
    for num in nums:
        yield num ** 2


fib_seq = fibonacci(number=100000000)
print(fib_seq)
for i in fib_seq:
    print(i, end=' ')

print("\n")
#генератор от генератора
print(sum(square(fibonacci(5000))))

#генераторные выражения

print()
cubes_gen = (num ** 3 for num in range(10))
print(cubes_gen)
for i in cubes_gen:
    print(i, end=' ')