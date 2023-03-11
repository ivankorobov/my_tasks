import os

file_name = "admin.bat"
path_to_file = os.path.abspath("admin.bat")
print(path_to_file)
path_join_to_file = os.path.join("Skillbox", "access", file_name)
print(path_join_to_file)

