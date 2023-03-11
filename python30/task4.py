# numbers = input("Введите числа: ")
# int_numbers = sorted(map(int, numbers.split()))
# print(list(int_numbers))

string = input("Введите строку: ")
new_string = filter(lambda x: x.isalpha() and x.islower(), string)
new_string2 = filter(lambda x: not (x.isdigit() or x.isupper()), string)
print(list(new_string))
print(list(new_string2))