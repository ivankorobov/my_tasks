text = input ("Введите строку: ")
number = int(input("Номер символа: "))
sym_list = list(text)
print(f"\nСимвол слева: {sym_list[number - 2]}")
print(f"Символ справа: {sym_list[number]}")
count = 0
for i in sym_list:
    if i == sym_list[number - 1]:
        count += 1
if count >= 2:
    print("в строке есть похожие символы.")
else:
    print("в строке нет похожих символов.")

