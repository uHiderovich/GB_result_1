from model.domain.Pet import Pet


class Hamster(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'зерно', gender, place_residence)
        self.__gender_type = 'Хомяк' if self.gender == 'male' else 'Хомячиха'

    def __str__(self):
        return f"{self.__gender_type} {self.name}"

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

    def full_info(self):
        return f"{self.__gender_type} \n {super().full_info()}"
