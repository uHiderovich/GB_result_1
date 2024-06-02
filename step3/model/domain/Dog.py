from model.domain.Pet import Pet


class Dog(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'predator', gender, place_residence)

    def bark(self):
        print(f"{self.name} лает")

    def gnawing_sofa(self):
        print(f"{self.name} грызет диван")

    def make_sound(self):
        self.bark()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def __str__(self):
        return f"Собака {self.name}"
