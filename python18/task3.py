ip_adress = "{0}.{1}.{2}.{3}"
numbers = []
for _ in range(4):
    num = int(input("Введите число (от 0 до 255 включ.): "))
    if 0 <= num <= 255:
        numbers.append(num)
print(ip_adress.format(*numbers))