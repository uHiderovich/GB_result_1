from model.services.AnimalRegistryService import AnimalRegistryService
from view.AnimalRegistryView import AnimalRegistryView

from model.exeptions.AddCommandException import AddCommandException
from model.exeptions.FindAnimalException import FindAnimalException
from model.exeptions.CreateAnimalException import CreateAnimalException


class AnimalRegistryController:
    def __init__(self):
        self.animal_registry_service = AnimalRegistryService()
        self.animal_registry_view = AnimalRegistryView()

    def register_animal(self, animal_type, name, age, gender, place_residence):
        try:
            animal = self.animal_registry_service.register_animal(animal_type, name, age, gender, place_residence)
            self.animal_registry_view.print_add_success(animal)
        except CreateAnimalException as error:
            self.animal_registry_view.print_message(error.message)

    def get_all_animals(self):
        return self.animal_registry_service.get_all_animals()

    def update_animal(self, animal_id, animal):
        return self.animal_registry_service.update_animal(animal_id, animal)

    def add_animal(self):
        new_animal_info = self.animal_registry_view.get_animal_info_for_add()
        self.register_animal(*new_animal_info)

    def show_all(self):
        all_animals = self.animal_registry_service.get_all_animals()
        self.animal_registry_view.print_animals(all_animals)

    def show_animal(self):
        animal_id = self.animal_registry_view.get_animal_id()
        try:
            animal = self.animal_registry_service.get_animal_by_id(animal_id)
            if self.animal_registry_service.is_pet(self.animal_registry_service.get_animal_type(animal)):
                self.update_pet(animal)
            elif self.animal_registry_service.is_pack(self.animal_registry_service.get_animal_type(animal)):
                self.update_pack(animal)
        except FindAnimalException as error:
            self.animal_registry_view.print_message(error.message)

    def add_command_for_animal(self, animal):
        try:
            command_name = self.animal_registry_view.print_add_command()
            animal.add_command(command_name)
        except AddCommandException as error:
            self.animal_registry_view.print_message(error.message)

    def show_all_command_of_animal(self, animal):
        self.animal_registry_view.print_commands_of_animal(animal.get_commands())

    def update_pet(self, animal):
        self.animal_registry_view.print_pet_menu(animal)
        while True:
            command = self.animal_registry_view.get_command()
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
                self.animal_registry_view.prind_error_command()
                self.update_pet(animal)

    def update_pack(self, animal):
        self.animal_registry_view.print_pack_animal_menu(animal)
        while True:
            command = self.animal_registry_view.get_command()
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
                self.animal_registry_view.prind_error_command()
                self.update_pack(animal)

    def start(self):
        self.animal_registry_view.print_menu()
        while True:
            command = self.animal_registry_view.get_command()
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
                self.animal_registry_view.prind_error_command()
                self.start()
