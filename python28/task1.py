class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(
            self.__class__.__name__,
            self.model
        )

    def operate(self):
        print("Я - Робот")


class CanFly:
    def __init__(self, *args, **kwargs):
        self.heigh = 0
        self.speed = 0

    def take_off(self):
        self.heigh = 100
        self.speed = 300
        print("Взлетаем")

    def flyy(self):
        self.speed = 5000
        print("Летаем")

    def landing(self):
        self.heigh = 0
        self.speed = 0
        print("Приземляемся")

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.heigh, self.speed
        )


class FlyDrone(CanFly, Robot):
    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print("Робот ведет разведку с воздуха")


class FlyWarDrone(CanFly, Robot):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f"Робот ведет разведку с воздуха при помощи {self.gun}")





class VacuumRobot(Robot):

    def __init__(self, model_num):
        super().__init__(model_num)
        self.trash = 0

    def operate(self):
        super().operate()
        print("Робот пылесосит пол\nЗагруженность мешка= {}".format(self.trash))

class WarRobot(Robot):
    def __init__(self, model_num, gun):
        super().__init__(model_num)
        self.gun = gun
    def operate(self):
        super().operate()
        print("Робот охраняет военный объект при помощи {}".format(self.gun))
class SubmarineRobot(WarRobot):
    def __init__(self, model_num, gun, depth):
        super().__init__(model_num, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print("Охрана ведется под водой на глубине", self.depth)

print()
FlyDrone('a1').operate()
print()
FlyWarDrone('r2-d2', 'intellect').operate()