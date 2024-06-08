from model.exeptions.CommandException import CommandException
from view.AnimalTasksBehaviourView import AnimalTasksBehaviourView


class AnimalTasksBehaviourController:
    def __init__(self):
        self.__tasks_view = AnimalTasksBehaviourView()

    def add_task_for_animal(self, animal):
        try:
            task_name = self.__tasks_view.print_add_task()
            animal.add_task(task_name)
        except CommandException as error:
            self.__tasks_view.print_message(error.message)

    def show_all_tasks_of_animal(self, animal):
        self.__tasks_view.print_tasks_of_animal(animal.get_tasks())

    def do_task(self, animal):
        try:
            task_for_animal = self.__tasks_view.print_how_task(animal)
            animal.do_task(task_for_animal)
        except CommandException as error:
            self.__tasks_view.print_message(error.message)