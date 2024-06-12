from model.exeptions.CommandException import CommandException
from view.AnimalTasksBehaviourView import AnimalTasksBehaviourView


class AnimalTasksBehaviourController:
    def __init__(self):
        """
        Класс контроллера для задач животных
        """
        self.__tasks_view = AnimalTasksBehaviourView()

    def add_task_for_animal(self, animal):
        """
        Метод для добавления задачи животному
        :param animal: животное
        :return: None
        """
        try:
            task_name = self.__tasks_view.print_add_task()
            animal.add_task(task_name)
        except CommandException as error:
            self.__tasks_view.print_message(error.message)

    def show_all_tasks_of_animal(self, animal):
        """
        Метод для вывода всех задач животного
        :param animal: животное
        :return: None
        """
        self.__tasks_view.print_tasks_of_animal(animal.get_tasks())

    def do_task(self, animal):
        """
        Метод для выполнения задачи животного
        :param animal: животное
        :return: None
        """
        try:
            task_for_animal = self.__tasks_view.print_how_task(animal)
            animal.do_task(task_for_animal)
        except CommandException as error:
            self.__tasks_view.print_message(error.message)