incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
name = ""

print("Общий доход составил:", sum(incomes.values()))
print("Самый маленьких доход у:", min(incomes, key=incomes.get), ":", min(incomes.values()))
incomes.pop(min(incomes, key=incomes.get))
for i in incomes:
    print(i, incomes[i], end="\n")