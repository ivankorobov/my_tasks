word = input("Введите строку: ")
exc_marc = input("Введите дополнительный знак: ")

list1 = [x * 2 for x in word]
list2 = [(x * 2) + exc_marc for x in word]

print(f"\nСписок удвоенных сомволов {list1}")
print(f"Склейка с доп символом {list2}")