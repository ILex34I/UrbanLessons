from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.sides = self.set_sides(*sides)
        self.__color = self.set_color(*color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for value in (r, g, b):
            if not (isinstance(value, int) and 0 <= value <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for value in sides:
            if not (isinstance(value, int) and value > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = [1] * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3
