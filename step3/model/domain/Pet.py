from model.domain.HumanFriendsAnimal import HumanFriendsAnimal


class Pet(HumanFriendsAnimal):
    def __init__(self, name, age, food_type, gender, place_residence):
        """
        Класс домашних животных
        :param name: имя животного
        :param age: возраст животного
        :param food_type: тип питания
        :param gender: пол животного
        :param place_residence: место жительства
        """
        super().__init__(name, age, food_type, gender, place_residence)

    def play(self):
        """
        Метод для игры с животным
        :return: None
        """
        print(f"{self.name} играет")

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")