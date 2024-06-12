class Task:
    def __init__(self, name):
        """
        Класс задачи
        :param name: Название задачи
        """
        self.name = name

    def __str__(self):
        return self.name

    def do(self):
        """
        Выполнение задачи
        :return: None
        """
        print(f"Выполняю задачу {self.name}")

    def stop(self):
        """
        Остановка задачи
        :return: None
        """
        print(f"Задача {self.name} остановлена")
