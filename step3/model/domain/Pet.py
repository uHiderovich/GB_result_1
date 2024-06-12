from model.domain.HumanFriendsAnimal import HumanFriendsAnimal


class Pet(HumanFriendsAnimal):
    __animal_counter = 0

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
        Pet.__animal_counter += 1

    def get_animal_number(self):
        """
        Получить количество созданных животных
        :return: int
        """
        return Pet.__animal_counter

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