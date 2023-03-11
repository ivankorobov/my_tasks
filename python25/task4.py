class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(
            self.__class__.__name__,
            self.model
        )

    def operate(self):
        print("Робот ездит по кругу")


class VacuumRobot(Robot):

    def __init__(self, model_num):
        super().__init__(model_num)
        self.trash = 0

    def operate(self):
        print("Робот пылесосит пол\nЗагруженность мешка= {}".format(self.trash))

class WarRobot(Robot):
    def __init__(self, model_num, gun):
        super().__init__(model_num)
        self.gun = gun
    def operate(self):
        print("Робот охраняет военный объект при помощи {}".format(self.gun))
class SubmarineRobot(WarRobot):
    def __init__(self, model_num, gun, depth):
        super().__init__(model_num, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print("Охрана ведется под водой на глубине", self.depth)

vacrob = VacuumRobot('qwe1')
vacrob.operate()
warrob = WarRobot("qwe1", "GUN")
warrob.operate()
subrob = SubmarineRobot("qwe1", "GUN", 999)
subrob.operate()