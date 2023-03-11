name = input("Введите имя: ")
number = int(input("Номер заказа: "))
string_line = "Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!".format(
    name=name,
    number=number
)
print(string_line)
