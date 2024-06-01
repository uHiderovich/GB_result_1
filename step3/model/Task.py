class Task:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def do(self):
        print(f"Выполняю задачу {self.name}")

    def stop(self):
        print(f"Задача {self.name} остановлена")
