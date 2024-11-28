class Car:

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(vin_number):

        if isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999:
            return True
        raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(numbers):
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        raise IncorrectCarNumbers('Некорректный тип данных для номеров')


class  IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:

  first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{first.model} успешно создан')



try:

  second = Car('Model2', 300, 'т001тр')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{second.model} успешно создан')



try:

  third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{third.model} успешно создан')