class CoordinatePoint:
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        CoordinatePoint.count += 1

    def print_info(self, new_c=count):
        print(f"X: {self.x}\nY: {self.y}\n")



a = CoordinatePoint()
print(CoordinatePoint.count)
a.print_info()

b = CoordinatePoint(3, 5)
print(CoordinatePoint.count)
b.print_info()

c = CoordinatePoint(9, 2)
print(CoordinatePoint.count)
c.print_info()
