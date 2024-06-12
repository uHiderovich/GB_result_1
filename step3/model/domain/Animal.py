class Animal:
    def __init__(self, age, food_type, gender):
        """
        Родительский класс для всех животных
        :param age: возраст
        :param food_type: тип пищи
        :param gender: пол
        """
        self.age = age
        self.food_type = food_type
        self.gender = gender

    def make_sound(self):
        """
        Метод голоса животного.
        Должен быть реализован в дочерних классах.
        :return: None
        """
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        """
        Метод движения животного.
        Должен быть реализован в дочерних классах.
        :return: None
        """
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        """
        Метод питания животного.
        Должен быть реализован в дочерних классах.
        :return: None
        """
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")