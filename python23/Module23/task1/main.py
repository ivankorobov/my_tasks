with open('people.txt', 'r', encoding='utf-8') as new_file:
    let_count = 0
    err_line = 0
    for i_line, line in enumerate(new_file):
        try:
            clear_line = line.rstrip()
            if clear_line.isalpha():
                let_count += len(clear_line)
                if len(clear_line) < 3:
                    err_line = i_line + 1
                    raise ValueError
        except ValueError as error:
            print("Ошибка: менее трёх символов в строке", err_line)

    print("Общее количество символов:", let_count)
