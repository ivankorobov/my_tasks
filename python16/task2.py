staffN = int(input("Введите кол-во сотрудников: "))
staffMoney = []
for i in range(staffN):
    print(f"Зарплата {i + 1} сотрудника: ", end= "")
    staff = int(input())
    staffMoney.append(staff)
for n in staffMoney:
    if n == 0:
        staffMoney.remove(n)

print("\nОсталось сотрудников:", len(staffMoney))
print("Зарплаты:", staffMoney)
max_n = max(staffMoney)
min_n = min(staffMoney)
print("\nМаксимальная ЗП:", max_n)
print("Минимальная ЗП:", min_n)