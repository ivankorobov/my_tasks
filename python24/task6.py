
class MyCar:

    def __init__(self, color, price, max_speed, curr_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.curr_speed = curr_speed

    def print_class(self):
        print("Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}".format(
            self.color, self.price, self.max_speed, self.curr_speed)
        )

    def curr_speed_plus(self, new_c_speed):
        old_c_speed = self.curr_speed
        self.curr_speed = new_c_speed
        print("Speed changed {} --> {}".format(old_c_speed, self.curr_speed))

car_1 = MyCar("BLCK", 999.999, 200, 10)
car_1.print_class()
car_1.curr_speed_plus(69)
car_1.print_class()
