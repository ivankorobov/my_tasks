numbers = 0
read_file = open('numbers.txt', 'r', encoding='utf8')
for i in read_file:
    numbers += int(i)
read_file.close()
write_file = open("answer.txt", 'w')
write_file.write(str(numbers))
write_file.close()

