class Command:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def do(self):
        print(f"Выполнил команду {self.__name}")