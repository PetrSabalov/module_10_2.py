from threading import Thread
import time
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        
    def run(self):
        count_war = 100
        days_count = 0
        while count_war > 0:
            time.sleep(1)
            days_count += 1
            count_war -= self.power
            if count_war > 0:
                print(f'{self.name} сражается {days_count} день(дня)..., '
                      f'осталось {count_war} воинов.')
            else:
                print(f'{self.name} одержал победу спустя {days_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы окончились!')

