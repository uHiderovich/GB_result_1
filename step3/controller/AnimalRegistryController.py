from controller.AnimalCommandsBehaviourController import AnimalCommandsBehaviourController
from controller.AnimalTasksBehaviourController import AnimalTasksBehaviourController

from model.exeptions.FindAnimalException import FindAnimalException
from model.exeptions.CreateAnimalException import CreateAnimalException


class AnimalRegistryController(AnimalCommandsBehaviourController, AnimalTasksBehaviourController):
    def __init__(self, view, model):
        """
        Класс контроллера для регистрации животных
        :param view: класс представления
        :param model: класс модели
        """
        super().__init__()
        self.__view = view
        self.__model = model

    def register_animal(self):
        """
        Метод для регистрации животного
        :return: None
        """
        animal_type = self.get_animal_type()
        name = self.get_animal_name()
        age = self.get_animal_age(animal_type)
        gender = self.get_animal_gender()
        place_residence = self.get_animal_place_residence()
        try:
            animal = self.__model.register_animal(animal_type, name, age, gender, place_residence)
            self.__view.print_add_success(animal)
        except CreateAnimalException as error:
            self.__view.print_message(error.message)

    def get_animal_type(self):
        """
        Метод для получения типа животного с валидацией
        :return: str
        """
        available_types = self.__model.get_available_animals_types()
        animal_type = self.__view.print_get_animal_type(available_types)
        validate_animal_type_error = self.__model.validate_animal_type(animal_type)
        if not validate_animal_type_error:
            return animal_type
        self.__view.print_message(validate_animal_type_error)
        return self.get_animal_type()

    def get_animal_name(self):
        """
        Метод для получения имени животного с валидацией
        :return: str
        """
        name = self.__view.print_get_animal_name()
        validate_name_error = self.__model.validate_name(name)
        if not validate_name_error:
            return name
        self.__view.print_message(validate_name_error)
        return self.get_animal_name()

    def get_animal_age(self, animal_type):
        """
        Метод для получения возраста животного с валидацией
        :param animal_type: тип животного
        :return: str
        """
        age = self.__view.print_get_animal_age()
        validate_age_error = self.__model.validate_age(animal_type, age)
        if not validate_age_error:
            return age
        self.__view.print_message(validate_age_error)
        return self.get_animal_age(animal_type)

    def get_animal_gender(self):
        """
        Метод для получения пола животного с валидацией
        :return: str
        """
        available_genders = self.__model.get_available_genders()
        animal_gender = self.__view.print_get_animal_gender(available_genders)
        validate_gender_error = self.__model.validate_gender(animal_gender)
        if not validate_gender_error:
            return animal_gender
        self.__view.print_message(validate_gender_error)
        return self.get_animal_gender()

    def get_animal_place_residence(self):
        """
        Метод для получения места проживания животного с валидацией
        :return: str
        """
        place_residence = self.__view.print_get_animal_place_residence()
        validate_place_residence_error = self.__model.validate_place_residence(place_residence)
        if not validate_place_residence_error:
            return place_residence
        self.__view.print_message(validate_place_residence_error)
        return self.get_animal_place_residence()

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
