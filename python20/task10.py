def pasport_name(num, ser, data_base):
    for i_person in data_base:
        if num in i_person and ser in i_person:
            print(f"Имя: {data_base[i_person][1]}\nФамилия: {data_base[i_person][0]}")
        else:
            print("Человек с таким паспортом не найден.")
            break

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
number = int(input("Введите номер паспорта: "))
series = int(input("Введите серию паспорта: "))
pasport_name(number, series, data)