from model.services.AnimalRegistryService import AnimalRegistryService
from view.AnimalRegistryView import AnimalRegistryView

from model.exeptions.AddCommandException import AddCommandException
from model.exeptions.FindAnimalException import FindAnimalException
from model.exeptions.CreateAnimalException import CreateAnimalException


class AnimalRegistryController:
    def __init__(self):
        self.__model = AnimalRegistryService()
        self.__view = AnimalRegistryView()

    def register_animal(self, animal_type, name, age, gender, place_residence):
        try:
            animal = self.__model.register_animal(animal_type, name, age, gender, place_residence)
            self.__view.print_add_success(animal)
        except CreateAnimalException as error:
            self.__view.print_message(error.message)

    def get_all_animals(self):
        return self.__model.get_all_animals()

    def update_animal(self, animal_id, animal):
        return self.__model.update_animal(animal_id, animal)

    def add_animal(self):
        new_animal_info = self.__view.get_animal_info_for_add()
        self.register_animal(*new_animal_info)

    def show_all(self):
        all_animals = self.__model.get_all_animals()
        self.__view.print_animals(all_animals)

    def show_animal(self):
        animal_id = self.__view.get_animal_id()
        try:
            animal = self.__model.get_animal_by_id(animal_id)
            if self.__model.is_pet(self.__model.get_animal_type(animal)):
                self.update_pet(animal)
            elif self.__model.is_pack(self.__model.get_animal_type(animal)):
                self.update_pack(animal)
        except FindAnimalException as error:
            self.__view.print_message(error.message)

    def add_command_for_animal(self, animal):
        try:
            command_name = self.__view.print_add_command()
            animal.add_command(command_name)
        except AddCommandException as error:
            self.__view.print_message(error.message)

    def show_all_command_of_animal(self, animal):
        self.__view.print_commands_of_animal(animal.get_commands())

    def update_pet(self, animal):
        self.__view.print_pet_menu(animal)
        while True:
            command = self.__view.get_command()
            if command == 'add_command':
                self.add_command_for_animal(animal)
            elif command == 'show_all_commands':
                self.show_all_command_of_animal(animal)
            elif command == 'main':
                self.start()
                break
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
                self.update_pet(animal)

    def update_pack(self, animal):
        self.__view.print_pack_animal_menu(animal)
        while True:
            command = self.__view.get_command()
            if command == 'add_command':
                self.add_command_for_animal(animal)
            elif command == 'show_all_commands':
                self.show_all_command_of_animal(animal)
            elif command == 'add_task':
                break
            elif command == 'show_all_tasks':
                break
            elif command == 'do_task':
                break
            elif command == 'mian':
                self.start()
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
                self.update_pack(animal)

    def start(self):
        self.__view.print_menu()
        while True:
            command = self.__view.get_command()
            if command == 'add':
                self.add_animal()
            elif command == 'show_all':
                self.show_all()
            elif command == 'show_by_id':
                self.show_animal()
                break
            elif command == 'exit':
                exit()
            else:
                self.__view.prind_error_command()
                self.start()
