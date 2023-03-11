idNum = int(input("Кол-во сотрудников в офисе: "))
id = []
for i in range(idNum):
    newID = int(input("ID сотрудника: "))
    id.append(newID)
findID = int(input("Какой ID ищем? "))
if findID  not in id:
    print("Сотрудник не работает!")
else:
    print("Сотрудник работает!")