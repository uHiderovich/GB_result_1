class Command:
    def __init__(self, name):
        """
        Класс команды
        :param name: Название команды
        """
        self.__name = name

    def __str__(self):
        return self.__name

    def do(self):
        """
        Выполнение команды
        :return: None
        """
        print(f"Выполнил команду {self.__name}")