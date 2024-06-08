from controller.AnimalRegistryController import AnimalRegistryController
from model.services.AnimalRegistryService import AnimalRegistryService
from view.AnimalRegistryView import AnimalRegistryView


def main():
    animal_registry_controller = AnimalRegistryController(AnimalRegistryView(), AnimalRegistryService())
    animal_registry_controller.start()
