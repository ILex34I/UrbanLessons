from time import sleep, time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

t = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

t2 = time()

print(f'Работа функции заняла {t2 - t}')

thread1 = Thread(target=write_words, args=(10,'example1.txt'))
thread2 = Thread(target=write_words, args=(30,'example2.txt'))
thread3 = Thread(target=write_words, args=(200,'example3.txt'))
thread4 = Thread(target=write_words, args=(100,'example4.txt'))

t = time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

t2 = time()

print(f'Работа потоков заняла {t2 - t}')