from model.domain.Dog import Dog
from model.domain.Cat import Cat
from model.domain.Hamster import Hamster
from model.domain.Horse import Horse
from model.domain.Camel import Camel
from model.domain.Donkey import Donkey


class AnimalRegistryService:
    def __init__(self):
        self.pets = {}
        self.pack_animals = {}
        self.all_animals = []

    def register_animal(self, animal_type, name, age, gender, place_residence):
        animal = self.create_animal(animal_type, name, age, gender, place_residence)

        if self.is_pet(animal_type):
            self.pets[animal.id] = animal
        if self.pack_animal(animal_type):
            self.pack_animals[animal.id] = animal

        self.all_animals.append(animal)

        return animal

    def create_animal(self, animal_type, name, age, gender, place_residence):
        animal = None
        if animal_type == 'dog':
            animal = Dog(name, age, gender, place_residence)
        elif animal_type == 'cat':
            animal = Cat(name, age, gender, place_residence)
        if animal_type == 'hamster':
            animal = Hamster(name, age, gender, place_residence)
        elif animal_type == 'horse':
            animal = Horse(name, age, gender, place_residence)
        if animal_type == 'camel':
            animal = Camel(name, age, gender, place_residence)
        elif animal_type == 'donkey':
            animal = Donkey(name, age, gender, place_residence)
        else:
            animal = None
        return animal

    def get_all_animals(self):
        return self.all_animals

    def is_pet(self, animal_type):
        return animal_type in ['dog', 'cat', 'hamster']

    def pack_animal(self, animal_type):
        return animal_type in ['horse', 'camel', 'donkey']

    def get_animal(self, animal_id):
        pass

    def update_animal(self, animal_id, animal):
        pass
