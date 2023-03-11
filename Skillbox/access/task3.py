import os

disc = os.path.abspath('.').split("/")

print("Корень диска:", os.path.abspath('.').split("/")[0])


abs_path = os.path.abspath(os.path.join("..","..", ".."))
print(abs_path)