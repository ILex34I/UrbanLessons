import queue
import random
import time
from threading import Thread


class Table:

    def __init__(self, number):

        self.number = number
        self.guest = None




class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:


    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests): #Прибытие гостей

        for guest in guests:

            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self): #Обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None for table in tables):
            for table in tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} за текущим столом покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} из очереди> вышел(-ла) и сел(-а) за стол номер {table.number}')






# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
# cafe.guest_arrival(*guests)
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
