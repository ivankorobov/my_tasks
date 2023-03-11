file = open('/Users/ivankorobov/PycharmProjects/Skillbox/access/task/Additional_info/group_1.txt', 'r')
summa = 0
diff = 0
compose = 1
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
file.close()
file_2 = open('/Users/ivankorobov/PycharmProjects/Skillbox/access/task/Dont touch me/group_2.txt', 'r')
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
file_2.close()
print(summa)
print(diff)
print(compose)