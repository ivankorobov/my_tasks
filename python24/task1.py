import random
class Toyota:
    color = "red",
    price = 1000000,
    max_speed = 200
    curr_speed = 0

car_1 = Toyota()
car_1.curr_speed = random.randint(0, 200)
print(car_1.curr_speed)
car_2 = Toyota()
car_2.curr_speed = random.randint(0, 200)
print(car_2.curr_speed)
car_3 = Toyota()
car_3.curr_speed = random.randint(0, 200)
print(car_3.curr_speed)