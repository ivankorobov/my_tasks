number_of_msgs = int(input("Количество пакетов: "))
result_msg = []
lost_packages = 0
for _ in range(number_of_msgs):
    buffer = []
    errors_in_package = 0
    for i in range(1, 5):
        bit = int(input(f"{i} бит: "))
        buffer.append(bit)
        if bit < 0:
            errors_in_package += 1
    if errors_in_package <= 1:
        result_msg.extend(buffer)
    else:
        lost_packages += 1

print("Полученное сообщение:", result_msg)
print("Кол-во ошибок в сообщении:", result_msg.count(-1))
print("Кол-во потерянных пакетов:", lost_packages)
