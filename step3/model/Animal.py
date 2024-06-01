class Animal:
    def __init__(self, age, food_type, gender):
        self.age = age
        self.food_type = food_type
        self.gender = gender

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")