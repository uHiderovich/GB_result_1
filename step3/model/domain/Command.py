class Command:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def do(self):
        print(f"Выполнил команду {self.name}")
