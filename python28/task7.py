class Pet:
    def __init__(self):
        self.__legs = 4
        self.__has_tail = True

    def __str__(self):
        tail = 'yes' if self.__has_tail else 'no'
        return f"Всего ног: {self.__legs}\nХвост присутствует - {tail}"


class Cat(Pet):
    @classmethod
    def sound(cls):
        print('MYAU')


class Dog(Pet):
    @classmethod
    def sound(cls):
        print('GAV')