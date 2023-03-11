class CoordinatePoint:
    count = 0
    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)
        CoordinatePoint.count += 1

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if not isinstance(x, int):
            raise Exception("Координата должна быть int класса")
        else:
            self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, int):
            raise Exception("Координата должна быть int класса")
        else:
            self.__y = y

    def __str__(self):
        return f"X: {self.__x}\nY: {self.__y}\n"

    def print_info(self, new_c=count):
        print(f"X: {self.__x}\nY: {self.__y}\n")



a = CoordinatePoint()
print(CoordinatePoint.count)
print(a)

b = CoordinatePoint("4", 5)
print(CoordinatePoint.count)
b.print_info()

c = CoordinatePoint(9, 2)
print(CoordinatePoint.count)
print(c.get_x())
c.print_info()