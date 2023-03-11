a_num = int(input("Левая граница: "))
b_num = int(input("Правая граница: "))

list1 = [x ** 3 for x in range(a_num, b_num + 1)]
list2 = [x ** 2 for x in range(a_num, b_num + 1)]

print(f"\nСписок кубов чисел в диапазоне от {a_num} до {b_num}: {list1}")
print(f"Список квадратов чисел в диапазоне от {a_num} до {b_num}: {list2}")
