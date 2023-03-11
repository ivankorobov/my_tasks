def factorial(num):
    if num == 1:
        return num
    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1


my_num = int(input("Num: "))
result = factorial(my_num)
print(result)
