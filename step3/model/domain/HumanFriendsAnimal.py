import itertools
from model.domain.Animal import Animal
from model.domain.Command import Command


class HumanFriendsAnimal(Animal):
    _id_iter = itertools.count()

    def __init__(self, name, age, food_type, gender, place_residence):
        super().__init__(age, food_type, gender)
        self._id = next(HumanFriendsAnimal._id_iter)
        self.name = name
        self.place_residence = place_residence
        self.commands = {}

    def get_id(self):
        return self._id

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return (f"Имя: {self.name}, "
                f"Возраст: {self.age}, "
                f"Люит кушать: {self.food_type}, "
                f"Пол: {self.gender}, "
                f"Место жительства: {self.place_residence}")

    def set_place_residence(self, place_residence):
        self.place_residence = place_residence

    def add_command(self, command_name):
        if self.commands[command_name]:
            print(f"Команда {command_name} уже существует")
            return
        self.commands[command_name] = Command(command_name)

    def get_commands(self):
        return list(self.commands.values())

    def do_command(self, command_name):
        if self.commands[command_name]:
            self.commands[command_name].do()
            return
        print(f"Команда {command_name} не найдена")

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")