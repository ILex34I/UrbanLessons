import requests

requests.get('https://urban-university.pro/student/courses')

res = requests.get('https://urban-university.pro/student/courses') # Создаём переменную, в которую сохраним код состояния запрашиваемой страницы.

print(res) # Выводим код состояния.

response = requests.get('https://urban-university.pro/student/courses')
q = response.text
print(q)
respo = requests.get('https://urban-university.pro/student/courses')
w = response.content
print(w)

