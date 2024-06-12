import itertools
from model.domain.Animal import Animal
from model.domain.Command import Command
from model.exeptions.CommandException import CommandException


class HumanFriendsAnimal(Animal):
    _id_iter = itertools.count()

    def __init__(self, name, age, food_type, gender, place_residence):
        """
        Класс, описывающий животное, которое является домашним другом человека
        :param name: имя животного
        :param age: возраст животного
        :param food_type: тип пищи, которую любит животное
        :param gender: пол животного
        :param place_residence: место жительства животного
        """
        super().__init__(age, food_type, gender)
        self._id = next(HumanFriendsAnimal._id_iter)
        self.name = name
        self.place_residence = place_residence
        self.commands = {}

    def get_id(self):
        """
        Получить идентификатор животного
        :return: int
        """
        return self._id

    def set_name(self, name):
        """
        Установить имя животного
        :param name: имя животного
        :return: None
        """
        self.name = name

    def get_name(self):
        """
        Получить имя животного
        :return: str
        """
        return self.name

    def full_info(self):
        """
        Получить полную информацию о животном
        :return: str
        """
        return (f"Имя: {self.name}, \n"
                f"Возраст: {self.age}, \n"
                f"Любит кушать: {self.food_type}, \n"
                f"Пол: {self.gender}, \n"
                f"Место жительства: {self.place_residence}\n")

    def set_place_residence(self, place_residence):
        """
        Установить место жительства животного
        :param place_residence: место жительства
        :return: None
        """
        self.place_residence = place_residence

    def add_command(self, command_name):
        """
        Добавить команду животному
        :param command_name: название команды
        :return: None
        """
        if self.commands.get(command_name, None):
            raise CommandException(f"Команда {command_name} уже существует")
        self.commands[command_name] = Command(command_name)

    def get_commands(self):
        """
        Получить список команд животного
        :return: list
        """
        return list(self.commands.values())

    def do_command(self, command_name):
        """
        Выполнить команду животного
        :param command_name: название команды
        :return: None
        """
        if not self.commands.get(command_name, None):
            raise CommandException(f"Команда {command_name} не найдена")
        self.commands[command_name].do()

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")