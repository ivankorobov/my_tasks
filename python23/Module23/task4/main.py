def check_exceptions():
    data = line.rstrip().split()
    if len(data) != 3:
        raise IndexError("НЕ присутствуют все три поля")
    elif not (str(data[0])).isalpha():
        raise NameError("Поле имени содержит НЕ только буквы")
    elif data[1].count("@") < 1 or data[1].count(".") < 1:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и .(точку)")
    elif not 10 <= int(data[2]) <= 99:
        raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")
    with open('registrations_good.log','a', encoding='utf-8') as file_good:
        file_good.write(line)

with open("registrations.txt", "r", encoding="utf-8") as reg_file:
    for line in reg_file:
        try:
            check_exceptions()
        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            with open('registrations_bad.log','a', encoding='utf-8') as file_bad:
                file_bad.write(f'Данные: {line}\nОшибка: {exc}\n')