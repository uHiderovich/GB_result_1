from model.domain.HumanFriendsAnimal import HumanFriendsAnimal


class Pet(HumanFriendsAnimal):
    def __init__(self, name, age, food_type, gender, place_residence):
        super().__init__(name, age, food_type, gender, place_residence)

    def play(self):
        print(f"{self.name} играет")

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")