import random

random_exceptions = [
    "NO WAY",
    "NOT TODAY",
    "SORRY, NO"
]

with open("out_file.txt", 'w') as out_file:
    try:
        count = 0
        while count <= 777:
            rand_num = random.randint(1, 13)
            number = int(input("Введите число: "))
            if random.randint(1, 13) == 13:
                raise Exception
            out_file.write(f"{str(number)}\n")
            count += number
        print("Вы успешно выполнили условие для выхода из порочного цикла!")
    except Exception:
        print(random.choice(random_exceptions))

