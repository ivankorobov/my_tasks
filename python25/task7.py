class CanFly:
    def __init__(self):
        self.heigh = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.heigh = 0
        self.speed = 0

    def info(self):
        print(self.heigh, self.speed)

class Butterfly(CanFly):

    def take_off(self):
        self.heigh = 1

    def fly(self):
        self.speed = 0.5

class Rocket(CanFly):
    def take_off(self):
        self.heigh = 500
        self.speed = 1000

    def land(self):
        self.heigh = 0
        self.destro_all()

    def destro_all(self):
        print("Ракета взорвалась!")


