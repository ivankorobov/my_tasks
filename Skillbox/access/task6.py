import os

def find_file(find_path, name, file_list=[]):
    for i_elem in os.listdir(find_path):
        new_path = os.path.join(find_path, i_elem)
        if i_elem == name:
            file_list.append(os.path.join(find_path, i_elem))
        if os.path.isdir(new_path):
            find_file(new_path, name)
    return file_list

abs_find_path = input("Ищем в: ")
file_name = input("Имя файла: ")
new_arr = find_file(abs_find_path, file_name)
print("\nНайдены следующие пути:")
for i in new_arr:
    print(i)


