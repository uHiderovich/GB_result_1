from model.domain.Pet import Pet


class Camel(Pet):
    def __init__(self, name, age, gender, place_residence):
        """
        Класс Верблюд
        :param name: имя
        :param age: возраст
        :param gender: пол
        :param place_residence: место обитания
        """
        super().__init__(name, age, 'кактус', gender, place_residence)
        self.__gender_type = 'Верблюд' if self.gender == 'male' else 'Верблюдица'

    def __str__(self):
        return f"{self.__gender_type} {self.name}"

    def neigh(self):
        """
        Метод, который выводит звук, издаваемый верблюдом
        :return: None
        """
        print(f"{self.name} ржет")

    def spit(self):
        """
        Метод плевка верблюда
        :return: None
        """
        print(f"{self.name} плюет")

    def make_sound(self):
        self.neigh()

    def run(self):
        print(f"{self.name} бежит")

    def eat(self):
        print(f"{self.name} ест")

    def full_info(self):
        """
        Полная информация о верблюде
        :return: str
        """
        return f"{self.__gender_type} \n {super().full_info()}"
