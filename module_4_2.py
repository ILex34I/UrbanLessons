# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции , функция должна печатать значение
# "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    return

#inner_function() - ошибка имя внутренней функции не определено

test_function()



