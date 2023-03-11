my_string = input("Строка: ")
numbers = []
print("Ответ:", end= " ")
for index, elem in enumerate(my_string):
    if elem == "~":
        print(index, end=" ")
        numbers.append(index)
