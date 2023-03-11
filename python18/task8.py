full_way = input("Путь к файлу: ")
# C:/user/docs/folder/new_file.txt
disc = input("Диск: ")
file_extension = input("Расширение файла: ")
if full_way.endswith(file_extension) and full_way.startswith(disc):
    print("Путь корректен")
else:
    print("Ошибка")