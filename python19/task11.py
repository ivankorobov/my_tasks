text = input("Введите строку: ")
result = set(text) & set("0123456789")
print(*result)
