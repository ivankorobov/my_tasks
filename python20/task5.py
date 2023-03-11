import random
random_letter_list_1 = [chr(random.randint(ord('а'), ord('я'))) for _ in range(10)]
random_letter_list_2 = [chr(random.randint(ord('а'), ord('я'))) for _ in range(10)]

print("Первый список", random_letter_list_1)
print("Второй список", random_letter_list_2)

random_letter_dict_1 = {}
random_letter_dict_2 = {}

for index, elem in enumerate(random_letter_list_1):
    random_letter_dict_1[index] = elem
for index, elem in enumerate(random_letter_list_2):
    random_letter_dict_2[index] = elem

print("Первый словарь", random_letter_dict_1)
print("Второй словарь", random_letter_dict_2)