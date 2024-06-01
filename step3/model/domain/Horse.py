import itertools
from model.domain.Pet import Pet


class Horse(Pet):
    id_iter = itertools.count()

    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'herbivore', gender, place_residence)
        self.id = next(Horse.id_iter)

    def neigh(self):
        print(f"{self.name} ржет")

    def make_sound(self):
        self.neigh()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def __str__(self):
        gender_type = 'Конь' if self.gender == 'male' else 'Кабыла'
        return f"{gender_type} {self.name}"
