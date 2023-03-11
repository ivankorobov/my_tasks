# class Figure:
#
#     def __init__(self, pos_x, pos_y, length, width):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.length = length
#         self.width = width
#
#     def move(self, pos_x, pos_y):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
#
# class ResizeAbleMixin:
#     def resize(self, length, width):
#         self.length = length
#         self.width = width
#
#
# class Rectangle(Figure, ResizeAbleMixin):
#     pass
#
#
# class Square(Figure, ResizeAbleMixin):
#
#     def __init__(self, pos_x, pos_y, size):
#         super().__init__(pos_x, pos_y, size, size)

from abc import ABC
class Figure(ABC):
    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, width, length):
        pass


class Rectangle(Figure):

    def resize(self, width, length):
        self.width = width
        self.length = length


class Square(Figure):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, width, length):
        if width == length:
            self.width = width
            self.length = length
        else:
            print("У квадрата стороны равны!")