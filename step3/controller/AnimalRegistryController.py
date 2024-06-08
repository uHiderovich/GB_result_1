from model.exeptions.FindAnimalException import FindAnimalException
from model.services.AnimalRegistryService import AnimalRegistryService
from view.AnimalRegistryView import AnimalRegistryView

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

    def get_animal(self, animal_id):
        return self.animal_registry_service.get_animal(animal_id)

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

    def find_animal(self):
        animal_id = self.animal_registry_view.get_animal_id()
        try:
            animal = self.animal_registry_service.get_animal_by_id(animal_id)
        except FindAnimalException as error:
            self.animal_registry_view.print_message(error.message)

    def start(self):
        self.animal_registry_view.print_menu()
        command = self.animal_registry_view.get_command()

        while True:
            if command == 'add':
                self.add_animal()
                break
            elif command == 'show_all':
                self.show_all()
                break
            elif command == 'show_by_id':
                self.find_animal()
                break
            elif command == 'exit':
                exit()
            else:
                self.animal_registry_view.prind_error_command()
                self.start()
