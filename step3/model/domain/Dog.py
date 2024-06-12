from model.domain.Pet import Pet


class Dog(Pet):
    def __init__(self, name, age, gender, place_residence):
        """
        Класс собаки
        :param name: имя
        :param age: возраст
        :param gender: пол
        :param place_residence: место жительства
        """
        super().__init__(name, age, 'собачий корм', gender, place_residence)

    def __str__(self):
        return f"Собака {self.name}"

    def bark(self):
        """
        Метод лаяния
        :return: None
        """
        print(f"{self.name} лает")

    def gnawing_sofa(self):
        """
        Метод грызки дивана
        :return: None
        """
        print(f"{self.name} грызет диван")

    def make_sound(self):
        self.bark()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def full_info(self):
        """
        Полная информация о собаке
        :return: str
        """
        return f"Собака \n {super().full_info()}"


