def infinit_gen():
    num = 0
    while True:
        yield num
        num += 1
def get_prime(n):
    prime_nums = []
    for number in range(2, n + 1):
        for prime in prime_nums:
            if number % prime == 0:
                break
        else:
            prime_nums.append(number)
            yield number

# new_gen = infinit_gen()
# for i in new_gen:
#     print(i)
    

new_gen2 = get_prime(50)
for i in new_gen2:
    print(i, end=' ')