import multiprocessing

from time import time

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

def readinfo(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for i in file:
            file.readline()
            all_data.append(i)

t1 = time()
readinfo(files[0])
readinfo(files[1])
readinfo(files[2])
readinfo(files[3])
t2 = time()
print(f'Время работы {t2 - t1}')

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = time()
    with multiprocessing.Pool(4) as p:
        p.map(readinfo, filenames)
    end = time()
    print(f'Работа процессов: {end - start}', '\n')