from model.domain.Pet import Pet


class Cat(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'predator', gender, place_residence)

    def meow(self):
        print(f"{self.name} мяукает")

    def catching_mouse(self):
        print(f"{self.name} ловит мышь")

    def make_sound(self):
        self.meow()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def __str__(self):
        gender_type = 'Кот' if self.gender == 'male' else 'Кошка'
        return f"{gender_type} {self.name}"
