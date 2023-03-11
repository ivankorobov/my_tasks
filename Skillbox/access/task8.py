import os

def find_file(cur_path, file_name):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                all_paths.extend(result)
    return all_paths

# def check_file_inside(path_to_file):
#     file = open(path_to_file, 'r', encoding='utf8')
#     for line in file:
#         print(line, end="")
#     file.close()

abs_find_path = input("Ищем в: ")
file_name = input("Имя файла: ")
all_paths = find_file(abs_find_path, file_name)
file = open(all_paths[0], 'r', encoding='utf8')
for line in file:
    print(line, end="")
file.close()
# check_file_inside(all_paths[0])