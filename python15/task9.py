wordsList = []
counts = [0, 0, 0]
for i in range(3):
    print("Введите", i + 1, "слово:", end=" ")
    word = input()
    wordsList.append(word)

text = input("Слово их текста: ")
while text != "end":
    for index in range(3):
        if wordsList[index] == text:
            counts[index] += 1
    text = input("Слово их текста: ")

print("\nПодсчет слов в тексте:")
for i in range(3):
    print(f"{wordsList[i]} : {counts[i]}")