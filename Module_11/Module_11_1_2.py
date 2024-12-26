import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Первый график') #Название
plt.show()

