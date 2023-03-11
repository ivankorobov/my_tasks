names = ['Tom', 'Bob', 'Albert']

ages = [20, 45, 70, 100]

dict_people = dict(zip(names, ages))
list_people = list(zip(names, ages))
zip_people = zip(names, ages)
print(dict_people)
print(list_people)
print(zip_people)


people_2 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
    }
print(people_2)