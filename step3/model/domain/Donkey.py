from model.domain.Pet import Pet


class Donkey(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'herbivore', gender, place_residence)

    def neigh(self):
        print(f"{self.name} ржет")

    def make_sound(self):
        self.neigh()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def __str__(self):
        gender_type = 'Осёл' if self.gender == 'male' else 'Ослиха'
        return f"{gender_type} {self.name}"