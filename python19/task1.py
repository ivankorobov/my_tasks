num = int(input("Введите целое число: "))
sqrt_dict = dict()
for i in range(1, num + 1):
    sqrt_dict[i] = i * i
print("Результат:", sqrt_dict)