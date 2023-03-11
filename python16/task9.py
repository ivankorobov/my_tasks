goods = [
    ["яблоки", 50], ["апельсины", 190], ["груши", 100],
    ["нектарины", 200], ["бананы", 77]
]
new_fruit = []
fruit_name = input("Новый фрукт: ")
new_fruit.append(fruit_name)
fruit_price = int(input("Цена: "))
new_fruit.append(fruit_price)

goods.append(new_fruit)
print(goods)
for i in goods:
    i[1] += i[1] / 100 * 8
print(goods)

