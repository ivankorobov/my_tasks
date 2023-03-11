def new_func(question,
             message= "Неверный ввод. Пожалуйста, введите 'да' или 'нет'.",
             retries= 4):
    while True:
        que = input(question).lower()
        if que == "да" or que == "нет":
            return 1
        else:
            retries -= 1
            print(message)
            print("Осталось попыток:", retries)
        if retries == 0:
            print("Попытки кончились")
            break

new_func("Вы действительно хотите выйти?", "Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
new_func("Удалить файл?", message="Так удалить или нет?")
new_func("Записать файл?", retries=2)

