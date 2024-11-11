class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):

        if args:
            cls.houses_history.append(args[0])

        return object.__new__(cls)



    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):

        return self.number_of_floors

    def __str__(self):

        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __le__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def  __ne__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __del__(self):

        print(f" {self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):

        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')





h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

h3 = House('ЖК Матрёшки', 20)

del h3

print(h1)
print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)



h1 += 10 # __iadd__
print(h1)



h2 = 10 + h2 # __radd__
print(h2)



print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__