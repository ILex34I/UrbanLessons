

class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):


        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):

        print(f"Модель: {self.__model}")

    def get_horsepower(self):

        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):

        print(f"Цвет: {self.__color}")


    def set_color(self, new_color):

        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color

        else:
            print(f'Нельзя сменить цвет на {new_color}.')

    def print_info(self):

        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5







# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()