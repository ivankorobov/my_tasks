fullNum = int(input("Кол-во участников: "))
teamN = int(input("Человек в команде: "))
team = []
count = 1
if fullNum % teamN == 0:
    for _ in range(fullNum // teamN):
        team.append(list(range(count, count + teamN)))
        count += teamN
else:
    print(f"{fullNum} участников невозможно поделить на команды по {teamN} человек!")
print("Общий список команд:", team)

