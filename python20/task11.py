contacts = {}

while True:
    name = input("Введите имя: ")
    if name == "стоп":
        break
    surname = input("Введите фамилию: ")
    name_n_surname = (name, surname)
    if name_n_surname not in contacts:
        contacts[name_n_surname] = int(input("Введите номер телефона: "))
    else:
        print("Такой контакт уже есть!")
    print(contacts)