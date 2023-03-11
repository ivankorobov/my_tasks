phone_dict = dict()
while True:
    name = input("Введите имя: ")
    if name in phone_dict:
        print("Ошибка. Такое имя цже записано.")
        break
    elif name == "стоп":
        break
    phone_number = input("Введите номер телефона: ")
    phone_dict[name] = phone_number
    for i in phone_dict:
        print(i, phone_dict[i] ,end= "\n")