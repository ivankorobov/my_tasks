message1 = input("Введите первое сообщение: ")
message2 = input("Введите второе сообщение: ")
count1 = message1.count("!") + message1.count("?")
count2 = message2.count("!") + message2.count("?")
if count1 > count2:
    print("Третье сообщение:", message1 + message2)
elif count1 < count2:
    print("Третье сообщение:", message2 + message1)
elif count1 == count2:
    print("Третье сообщение: ОЙ!")