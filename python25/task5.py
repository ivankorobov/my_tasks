class MyOwnException(Exception):
    pass

with open("numbers.txt", 'r', encoding='utf-8') as text:
    for line in text:
        try:
            clear_line = line.rstrip()
            num_1, num_2 = clear_line.split()
            if int(num_1) < int(num_2):
                raise MyOwnException("Первое число должно быть больше второго!")
            print(int(num_1) / int(num_2))
        except (ValueError, MyOwnException) as exc:
            print(exc, type(exc), num_1, num_2)