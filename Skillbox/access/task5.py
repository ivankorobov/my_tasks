import os

file_name = input("Название: ")
abs_path = os.path.join(os.path.abspath(".."), file_name)
print(abs_path)
file_size = os.path.getsize(abs_path)
if os.path.isfile(abs_path):
    print(f"Путь: {abs_path}\nЭто файл\nРазмер файла: {file_size}")
elif os.path.isdir(abs_path):
    print("Это папка!")
else:
     print("Указанного пути не существует")
