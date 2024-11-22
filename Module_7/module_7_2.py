

def custom_write(file_name, strings):






    
    file_name = open(name, 'a', encoding='utf-8')




















info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)