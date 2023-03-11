import random
def return_even_elements(data):
    result = []
    if isinstance(data, dict):
        print("Допустим, есть такой словарь:", data)
        data = data.values()
    if isinstance(data, list):
        print("Допустим, есть такой список:", data)
    if isinstance(data, str):
        print("Допустим, есть такой строка:", data)
    if isinstance(data, tuple):
        print("Допустим, есть такой кортеж:", data)
    for index, value in enumerate(data):
        if index % 2 == 0:
            result.append(value)
    return result
my_tuple = tuple([random.randint(0, 10) for _ in range(10)])
print("Результат:", return_even_elements(my_tuple))
print("Результат:", return_even_elements('О Дивный Новый мир!'))
print("Результат:", return_even_elements([100, 200, 300, 'буква', 0, 2, 'а']))
print("Результат:", return_even_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))