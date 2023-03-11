student_inf = input("Введите информацию о студенте: ")
student_info = dict()
stud_arr = student_inf.split()
student_info["Имя"] = stud_arr[0]
student_info["Фамилия"] = stud_arr[1]
student_info["Город"] = stud_arr[2]
student_info["Место учебы"] = stud_arr[3]
student_info["Оценки"] = []
for i in stud_arr[4:]:
    student_info["Оценки"].append(i)
for i in student_info:
    print(i, "-", student_info[i])
