def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # ни чего не возвращает

inner_function() # выдает ошибку
