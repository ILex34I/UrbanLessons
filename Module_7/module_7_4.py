

team1_num = 5

team2_num = 6

score_1 = 40

score_2 = 42

team1_time = 1552.512

team2_time = 2153.31451

tasks_total = 82

time_avg = 45.2

challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:

    result = 'Победа команды Мастера кода!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:

    result = 'Победа команды Волшебники Данных!'

else:

    result = 'Ничья!'


print('В команде Мастера кода участников: %(num1)s ! ' % {'num1': team1_num})

print('Итого сегодня в командах участников: %(num1)s и %(num2)s !' % {'num1': team1_num, 'num2': team2_num})

print('Команда Волшебники данных решила задач: {score_} !'. format(score_=score_2))

print('Волшебники данных решили задачи за {time__} с !'. format(time__=team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: {result}')
