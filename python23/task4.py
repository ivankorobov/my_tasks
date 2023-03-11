my_str = input("Введите строку: ")
new_file = open("new_file.txt", 'w')
try:
    new_file.write(my_str)
except:
    print("Ошибка")
else:
    print("Программа выполнена")
finally:
    new_file.close()


if new_file.closed:
    print("Файл закрыт")