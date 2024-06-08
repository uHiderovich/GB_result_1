from model.domain.Dog import Dog
from model.domain.Cat import Cat
from model.domain.Hamster import Hamster
from model.domain.Horse import Horse
from model.domain.Camel import Camel
from model.domain.Donkey import Donkey

from model.exeptions.CreateAnimalException import CreateAnimalException
from model.exeptions.FindAnimalException import FindAnimalException


class AnimalRegistryService:
    def __init__(self):
        self.__pets = {}
        self.__pack_animals = {}
        self.__all_animals = []
        self.__pets_types = ['dog', 'cat', 'hamster']
        self.__pack_animals_types = ['horse', 'camel', 'donkey']

    def register_animal(self, animal_type, name, age, gender, place_residence):
        animal = self.animal_factory(animal_type, name, age, gender, place_residence)

        if not animal:
            raise CreateAnimalException("Не известный тип животного")

        if self.is_pet(animal_type):
            self.__pets[animal.get_id()] = animal
        if self.is_pack(animal_type):
            self.__pack_animals[animal.get_id()] = animal

        self.__all_animals.append(animal)
        return animal

    def animal_factory(self, animal_type, name, age, gender, place_residence):
        if animal_type == 'dog':
            return Dog(name, age, gender, place_residence)
        elif animal_type == 'cat':
            return Cat(name, age, gender, place_residence)
        if animal_type == 'hamster':
            return Hamster(name, age, gender, place_residence)
        elif animal_type == 'horse':
            return Horse(name, age, gender, place_residence)
        if animal_type == 'camel':
            return Camel(name, age, gender, place_residence)
        elif animal_type == 'donkey':
            return Donkey(name, age, gender, place_residence)
        else:
            return None

    def get_all_animals(self):
        return self.__all_animals

    def is_pet(self, animal_type):
        return animal_type in self.__pets_types

    def is_pack(self, animal_type):
        return animal_type in self.__pack_animals_types

    def get_animal_type(self, animal):
        return type(animal).__name__.lower()

    def get_animal_by_id(self, animal_id):
        for animal in self.__all_animals:
            if animal.get_id() == animal_id:
                return animal
        raise FindAnimalException(f"Животное с id {animal_id} не найдено!")
