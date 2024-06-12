from model.domain.Dog import Dog
from model.domain.Cat import Cat
from model.domain.Hamster import Hamster
from model.domain.Horse import Horse
from model.domain.Camel import Camel
from model.domain.Donkey import Donkey

from model.exeptions.CreateAnimalException import CreateAnimalException
from model.exeptions.FindAnimalException import FindAnimalException


class AnimalRegistryService:
    def __init__(self):
        """
        Класс для регистрации животных
        """
        self.__pets = {}
        self.__pack_animals = {}
        self.__all_animals = []
        self.__pets_types = ['dog', 'cat', 'hamster']
        self.__pack_animals_types = ['horse', 'camel', 'donkey']
        self.__genders = ['male', 'femail']

    def register_animal(self, animal_type, name, age, gender, place_residence):
        """
        Регистрация животного
        :param animal_type: тип животного
        :param name: имя животного
        :param age: возраст животного
        :param gender: пол животного
        :param place_residence: место жительства животного
        :return: класс животного по animal_type
        """
        try:
            animal = self.animal_factory(animal_type, name, age, gender, place_residence)
            if self.is_pet(animal_type):
                self.__pets[animal.get_id()] = animal
            if self.is_pack(animal_type):
                self.__pack_animals[animal.get_id()] = animal
            self.__all_animals.append(animal)
            return animal
        except Exception as error:
            raise error

    def animal_factory(self, animal_type, name, age, gender, place_residence):
        """
        Фабричный метод для создания животных по типу
        :param animal_type: тип животного
        :param name: имя животного
        :param age: возраст животного
        :param gender: пол животного
        :param place_residence: место жительства животного
        :return: класс животного по animal_type
        """
        if animal_type == 'dog':
            return Dog(name, age, gender, place_residence)
        elif animal_type == 'cat':
            return Cat(name, age, gender, place_residence)
        if animal_type == 'hamster':
            return Hamster(name, age, gender, place_residence)
        elif animal_type == 'horse':
            return Horse(name, age, gender, place_residence)
        if animal_type == 'camel':
            return Camel(name, age, gender, place_residence)
        elif animal_type == 'donkey':
            return Donkey(name, age, gender, place_residence)
        else:
            return None

    def get_all_animals(self):
        """
        Получить всех животных
        :return: list
        """
        return self.__all_animals

    def is_pet(self, animal_type):
        """
        Проверка является ли животное домашним
        :param animal_type: тип животного
        :return: bool
        """
        return animal_type in self.__pets_types

    def is_pack(self, animal_type):
        """
        Проверка является ли животное рабочим
        :param animal_type: тип животного
        :return: bool
        """
        return animal_type in self.__pack_animals_types

    def get_animal_type(self, animal):
        """
        Получить тип животного
        :param animal: животное
        :return: str
        """
        return type(animal).__name__.lower()

    def get_animal_by_id(self, animal_id):
        """
        Получить животное по id
        :param animal_id: id животного
        :return: животное
        """
        for animal in self.__all_animals:
            if animal.get_id() == animal_id:
                return animal
        raise FindAnimalException(f"Животное с id {animal_id} не найдено!")

    def get_available_animals_types(self):
        """
        Получить доступные типы животных
        :return: list
        """
        return self.__pets_types + self.__pack_animals_types

    def get_available_genders(self):
        """
        Получить доступные полы животных
        :return: list
        """
        return self.__genders

    def get_animals_number_by_group(self, group):
        """
        Получить количество домашних животных по типу
        :return: int
        """
        animals = self.__pets if group == 'pets' else self.__pack_animals

        if len(animals) == 0:
            return 0
        else:
            # Тут разумеется достаточно получить длину animals,
            # но в задании кажется намек на статичнский класс, для демонстрации понимания ООП
            # по-этому вот такая загагулина:)
            return animals[0].get_animal_number()

    def get_available_groups(self):
        """
        Получить доступные типы групп животных
        :return: list
        """
        return ['pets', 'pack_animals']

    def validate_animal_info_for_register(self, animal_type, name, age, gender, place_residence):
        exception_text = (
            self.validate_animal_type(animal_type) or
            self.validate_age(animal_type, age) or
            self.validate_name(name) or
            self.validate_gender(gender) or
            self.validate_place_residence(place_residence)
        )

        if exception_text:
            raise CreateAnimalException(exception_text)

    def validate_animal_type(self, animal_type):
        """
        Валидация типа животного
        :param animal_type: тип животного
        :return: str
        """
        if animal_type not in self.get_available_animals_types():
            return "Не известный тип животного!"
        else:
            return None

    def validate_age(self, animal_type, age):
        """
        Валидация возраста животного
        :param animal_type: тип животного
        :param age: возраст животного
        :return: str
        """
        if not age.isdigit():
            return "Возраст домашнего животного должен быть числом"
        elif int(age) < 0:
            return "Возраст домашнего животного не может быть отрицательным"
        elif self.is_pet(animal_type) and int(age) > 20:
            return "Домашнее животное не может быть старше 20 лет"
        elif self.is_pack(animal_type) and int(age) > 30:
            return "Рабочее животное не может быть старше 30 лет"
        else:
            return None

    def validate_name(self, name):
        """
        Валидация имени животного
        :param name: имя животного
        :return: str
        """
        if len(name) < 2:
            return "Имя животного должно быть длиннее 2 символов"
        else:
            return None

    def validate_gender(self, gender):
        """
        Валидация пола животного
        :param gender: пол животного
        :return: str
        """
        if gender not in self.get_available_genders():
            return "Пол животного должен быть мальчик или девочка"
        else:
            return None

    def validate_place_residence(self, place_residence):
        """
        Валидация места жительства животного
        :param place_residence: место жительства животного
        :return:
        """
        if len(place_residence) < 2:
            return "Имя животного должно быть длиннее 2 символов"
        else:
            return None
