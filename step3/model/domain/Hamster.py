from model.domain.Pet import Pet


class Hamster(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'herbivore', gender, place_residence)

    def squeak(self):
        print(f"{self.name} пищит")

    def run_in_wheel(self):
        print(f"{self.name} бежит в колесе")

    def make_sound(self):
        self.squeak()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def __str__(self):
        gender_type = 'Хомяк' if self.gender == 'male' else 'Хомячиха'
        return f"{gender_type} {self.name}"
