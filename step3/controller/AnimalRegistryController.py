from controller.AnimalCommandsBehaviourController import AnimalCommandsBehaviourController
from controller.AnimalTasksBehaviourController import AnimalTasksBehaviourController

from model.exeptions.FindAnimalException import FindAnimalException
from model.exeptions.CreateAnimalException import CreateAnimalException


class AnimalRegistryController(AnimalCommandsBehaviourController, AnimalTasksBehaviourController):
    def __init__(self, view, model):
        """
        Класс контроллера для регистрации животных
        :param view:
        :param model:
        """
        super().__init__()
        self.__view = view
        self.__model = model

    def register_animal(self):
        """
        Метод для регистрации животного
        :return: None
        """
        available_types = self.__model.get_available_animals_types()
        available_genders = self.__model.get_available_genders()
        new_animal_info = self.__view.get_animal_info_for_add(available_types, available_genders)
        try:
            animal = self.__model.register_animal(*new_animal_info)
            self.__view.print_add_success(animal)
        except CreateAnimalException as error:
            self.__view.print_message(error.message)

    def show_all(self):
        """
        Метод для вывода всех животных
        :return: None
        """
        all_animals = self.__model.get_all_animals()
        self.__view.print_animals(all_animals)

    def show_selected_animal(self):
        """
        Метод для вывода выбранного животного
        :return: None
        """
        animal_id = self.__view.get_animal_id()
        try:
            animal = self.__model.get_animal_by_id(animal_id)
            if self.__model.is_pet(self.__model.get_animal_type(animal)):
                self.start_pet_actions(animal)
            elif self.__model.is_pack(self.__model.get_animal_type(animal)):
                self.start_pack_actions(animal)
        except FindAnimalException as error:
            self.__view.print_message(error.message)

    def start_pet_actions(self, animal):
        self.__view.print_pet_menu(animal)
        while True:
            command = self.__view.get_menu_command()
            if command == 'add_command':
                self.add_command_for_animal(animal)
            elif command == 'show_all_commands':
                self.show_all_command_of_animal(animal)
            elif command == 'do_command':
                self.do_command(animal)
            elif command == 'main':
                self.start()
                break
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
                self.start_pet_actions(animal)

    def start_pack_actions(self, animal):
        self.__view.print_pack_animal_menu(animal)
        while True:
            command = self.__view.get_menu_command()
            if command == 'add_command':
                self.add_command_for_animal(animal)
            elif command == 'show_all_commands':
                self.show_all_command_of_animal(animal)
            elif command == 'do_command':
                self.do_command(animal)
            elif command == 'add_task':
                self.add_task_for_animal(animal)
            elif command == 'show_all_tasks':
                self.show_all_tasks_of_animal(animal)
            elif command == 'do_task':
                self.do_task(animal)
            elif command == 'mian':
                self.start()
                break
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
                self.start_pack_actions(animal)

    def start(self):
        """
        Метод для запуска контроллера
        :return: None
        """
        self.__view.print_menu()
        while True:
            command = self.__view.get_menu_command()
            if command == 'add':
                self.register_animal()
            elif command == 'show_all':
                self.show_all()
            elif command == 'show_by_id':
                self.show_selected_animal()
                break
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
