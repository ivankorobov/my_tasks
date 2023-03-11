word = input ("Введите текст: ")
count = 0
chtoZamen = input("Что заменяем: ")
replace_sym = input("Чем заменяем: ")

sym_list = list(word)
index = 0
for i in sym_list:
    if i == chtoZamen:
        count += 1
        sym_list[index] = replace_sym
    index += 1
for i in sym_list:
    print(i, end="")