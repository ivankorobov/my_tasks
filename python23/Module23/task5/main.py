
calc_lines = open("calc.txt", 'r')
count = 0
for i_line in calc_lines:
    try:
        count += eval(i_line)
    except SyntaxError:
        print(f"Обнаружена ошибка в строке: {i_line}", end="")
        choice = input("Хотите исправить? ").lower()
        if choice == "да":
            new_line = input("Введите исправленную строку: ")
            count += eval(new_line)

print("Сумма результатов:", count)
