from model.domain.Pet import Pet


class Cat(Pet):
    def __init__(self, name, age, gender, place_residence):
        super().__init__(name, age, 'кошачий корм', gender, place_residence)
        self.__gender_type = 'Кот' if self.gender == 'male' else 'Кошка'

    def __str__(self):
        return f"{self.__gender_type} {self.name}"

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

    def full_info(self):
        return f"{self.__gender_type} \n {super().full_info()}"
