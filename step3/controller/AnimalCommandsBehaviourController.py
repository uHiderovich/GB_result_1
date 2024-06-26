from model.exeptions.CommandException import CommandException
from view.AnimalCommandsBehaviourView import AnimalCommandsBehaviourView


class AnimalCommandsBehaviourController:
    def __init__(self):
        """
        Класс контроллер для взаимодействия с командами животного
        """
        self.__commands_view = AnimalCommandsBehaviourView()

    def add_command_for_animal(self, animal):
        """
        Добавление команды для животного
        :param animal: животное
        :return: None
        """
        try:
            command_name = self.__commands_view.print_add_command()
            animal.add_command(command_name)
            self.__commands_view.print_add_command_success(command_name)
        except CommandException as error:
            self.__commands_view.print_message(error.message)
        except Exception as error:
            self.__commands_view.print_message(error)

    def show_all_command_of_animal(self, animal):
        """
        Вывод всех команд животного
        :param animal: животное
        :return: None
        """
        self.__commands_view.print_commands_of_animal(animal.get_commands())

    def do_command(self, animal):
        """
        Выполнение команды животного
        :param animal: животное
        :return: None
        """
        try:
            command_for_animal = self.__commands_view.print_how_command(animal)
            animal.do_command(command_for_animal)
        except CommandException as error:
            self.__commands_view.print_message(error.message)
        except Exception as error:
            self.__commands_view.print_message(error)
