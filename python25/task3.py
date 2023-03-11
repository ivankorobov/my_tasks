class Ship:
    def __init__(self, model):
        self.__model = model
    def model_print(self):
        return "\nМодель корабля {model}".format(
            model=self.__model)
    def walk_on_water(self):
        return "\nКорабль {model} идёт куда-то".format(
            model=self.__model)
    def get_model(self):
        return self.__model

class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun
    def attack(self):
        print("Корабль {model} стреляет из орудия {gun}".format(
            model=self.get_model(),
            gun=self.__gun
        ))

class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.__tonnage = 0

    def load(self):
        print("\nЗагружаем корабль")
        self.__tonnage += 1
        print("\nЗагруженность корабля= {}".format(self.__tonnage))
    def unload(self):
        print("\nРазгружаем корабль")
        if self.__tonnage > 0:
            self.__tonnage -= 1
        else:
            print("\nКорабль уже разгружен")
        print("\nЗагруженность корабля= {}".format(self.__tonnage))

warship = WarShip("qwe", "BOOM")
warship.attack()
