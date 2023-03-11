
class MyCar:
    color = "red"
    price = 1000000
    max_speed = 200
    curr_speed = 0

    def print_class(self):
        print("Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}".format(
            self.color, self.price, self.max_speed, self.curr_speed)
        )

    def curr_speed_plus(self, new_c_speed):
        old_c_speed = self.curr_speed
        self.curr_speed = new_c_speed
        print("Speed changed {} --> {}".format(old_c_speed, self.curr_speed))

car_1 = MyCar()
car_1.print_class()
car_1.curr_speed_plus(69)
car_1.print_class()
