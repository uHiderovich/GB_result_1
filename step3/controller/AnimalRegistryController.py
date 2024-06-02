from model.services.AnimalRegistryService import AnimalRegistryService
from view.AnimalRegistryView import AnimalRegistryView


class AnimalRegistryController:
    def __init__(self):
        self.animal_registry_service = AnimalRegistryService()
        self.animal_registry_view = AnimalRegistryView()

    def register_animal(self, animal_type, name, age, gender, place_residence):
        animal = self.animal_registry_service.register_animal(animal_type, name, age, gender, place_residence)

    def get_animal(self, animal_id):
        return self.animal_registry_service.get_animal(animal_id)

    def get_all_animals(self):
        return self.animal_registry_service.get_all_animals()

    def update_animal(self, animal_id, animal):
        return self.animal_registry_service.update_animal(animal_id, animal)

    def start(self):
        self.animal_registry_view.print_pet_menu()
        self.animal_registry_view.print_pet_menu()

        command = self.animal_registry_view.get_command()

        while True:
            if command == 'add':
                pass
            elif command == 'show_all':
                pass
            elif command == 'show_by_id':
                pass
            elif command == 'exit':
                break
            else:
                self.animal_registry_view.prind_error_command()
                self.start()
