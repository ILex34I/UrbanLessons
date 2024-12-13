import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power, counter=100):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.counter = counter

    def timer(self, name, power, counter):
        day = 0
        while counter:
            day += 1
            time.sleep(1)
            counter -= power
            print(f"{name} сражается {day} дней, осталось {counter} воинов.")
        print(f"{name} одержал победу спустя {day} дней!")

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer(self.name, self.power, self.counter)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

for knight in (first_knight, second_knight):
    knight.start()
for knight in (first_knight, second_knight):
    knight.join()
print('Все битвы закончились!')