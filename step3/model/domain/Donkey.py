from model.domain.Pet import Pet


class Donkey(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'трава', gender, place_residence)
        self.__gender_type = 'Осёл' if self.gender == 'male' else 'Ослиха'

    def __str__(self):
        return f"{self.__gender_type} {self.name}"

    def neigh(self):
        print(f"{self.name} ржет")

    def make_sound(self):
        self.neigh()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def full_info(self):
        return f"{self.__gender_type} \n {super().full_info()}"
