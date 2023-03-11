class Human:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name):
        if not name.isalpha():
            raise Exception("Имя должно состоять только из букв.")
        else:
            self.__name = name

    def set_age(self, age):
        if not age in range(0, 101):
            raise Exception("Возрасть должен быть в диапазоне от 0 до 100.")
        else:
            self.__age = age

    def get_info(self):
        print(f"Имя: {self.__name}\nВозраст: {self.__age}")

    def get_count(self):
        print("Кол-во созданных объектов:", self.__count)

person_1 = Human("Bob", 32)
person_2 = Human("Ron", 24)
person_3 = Human("John", 45)
person_4 = Human("Ronny", 24)
person_1.get_info()
person_2.get_count()
person_2.get_count()
person_2.get_count()


