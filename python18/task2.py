name = input("Введите имя: ")
number = int(input("Номер долг: "))
string_line = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! ".format(name, number)
print(string_line)