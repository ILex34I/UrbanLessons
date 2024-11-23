

def custom_write(file_name, strings):

    strings_positions = {}


    name = open(file_name, 'w', encoding='utf-8')

    for j, i in enumerate(strings):

        strings_positions[(j + 1, name.tell())] = i

        name.write(i + '\n')

    name.close()

    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]

result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)