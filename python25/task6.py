class Unit:

    def __init__(self, health):
        self.__health = health

    def set_hp(self, other):
        self.__health = other

    def get_hp(self):
        return self.__health

    def take_damage(self, damage):
        print("Получен урон", damage)
        self.set_hp(self.get_hp() - 0)
        print("HP:", self.__health)

class Soldier(Unit):

    def take_damage(self, damage):
        print("Получен урон", damage)
        self.set_hp(self.get_hp() - damage)
        print("HP:", self.get_hp())

class Grazhdanin(Unit):

    def take_damage(self, damage):
        print("Получен урон", damage)
        self.set_hp(self.get_hp() - damage * 2)
        print("HP:", self.get_hp())

soldier_1 = Soldier(100)
soldier_1.take_damage(20)
just_man = Grazhdanin(100)
just_man.take_damage(20)
