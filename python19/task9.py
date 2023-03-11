text = input("Введите строку: ")
exclMarc = ".,;:!?"
count = 0
unique = set(exclMarc)
for elem in unique:
    if elem in exclMarc:
        count += 1
print("Количество знаков пунктуации:", count)

