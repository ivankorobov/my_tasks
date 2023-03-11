numCount = int(input("Введите кол-во чисел в списке: "))
numbers = []
for i in range(numCount):
    print(f"Введите {i + 1} число: ", end= "")
    newNum = int(input())
    numbers.append(newNum)
print(numbers)
zz = int(input("Введите делитель: "))
index = 0
idSumm = 0
for id in numbers:
    if id % zz == 0:
        print(f"Индекс числа {id}: {index}")
        idSumm += index
    index += 1
print("Сумма индексов:", idSumm)