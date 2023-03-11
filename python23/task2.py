let_names = 'ABCDEFGHIJ'
read_file = open("ages.txt", 'r', encoding='utf-8')
write_file = open("ages_w_names", 'w')
try:
    for i, v in enumerate(read_file):
        save = (f"{let_names[i]} -- {int(v)}")
        write_file.write(save)
except IsADirectoryError:
    print("На чтение ожидался файл, но это оказалась директория")
except IndexError:
    print("Индексы не совпадают")
except ValueError as sss:
    print(sss)
except FileExistsError:
    print("Файл с таким названием нельзя создать, такой уже существует")
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Программа выполнена успешно")

finally:
    read_file.close()
    write_file.close()
    print(read_file.closed, write_file.closed)


# file_ages = None
# file_result = None
#
# try:
#     file_ages = open("ages.txt", "r", encoding="utf8")
#     file_result = open("result.txt", "x", encoding="utf8")
#     # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
#     print("Поймано исключение: ", exc, type(exc))
#
# if file_result and file_ages:
#     names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     count = 0
#     for line in file_ages:
#         try:
#             clear_line = line.rstrip()
#             int(clear_line)  # на всякий случай пытаемся преобразить данные в int,
#             но не сохраняем это в переменную, т.к. записывать нам
#             # в файл придётся именно строку
#             file_result.write(names[count] + " - " + clear_line)
#             count += 1
#         except (ValueError, TypeError) as exc:
#             print("Поймано исключение: ", exc, type(exc))