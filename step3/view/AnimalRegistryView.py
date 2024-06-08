class AnimalRegistryView:
    def __init__(self):
        pass

    def print_menu(self):
        print('-------------------')
        print('Меню:')
        print('1. add для добавления животного в реестр')
        print('2. show_all для просмотра всех животных в реестре')
        print('3. show_by_id для просмотра животного по его id')
        print('4. exit для выхода из программы')
        print('-------------------')

    def print_pet_menu(self, animal):
        print('-------------------')
        self.print_selected_animal(animal)
        print('1. add_command для добавления новой команды')
        print('2. show_all_commands для просмотра всех команд')
        print('3. main для возврата в главное меню')
        print('4. exit для выхода из программы')
        print('-------------------')

    def print_pack_animal_menu(self, animal):
        print('-------------------')
        self.print_selected_animal(animal)
        print('1. add_command для добавления новой команды')
        print('2. show_all_commands для просмотра всех команд')
        print('3. add_task для добавления новой задачи')
        print('4. show_all_tasks для просмотра всех задач')
        print('5. main для возврата в главное меню')
        print('6. exit для выхода из программы')
        print('-------------------')

    def get_command(self):
        return self.prompt('Введите команду: ')

    def print_animals(self, animals):
        print('-------------------')
        print('Список животных:')
        for animal in animals:
            print(f"ID: {animal.get_id()}, " + animal)
        print('-------------------')

    def print_selected_animal(self, animal):
        print('Выбранное животное: ')
        print(f"ID: {animal.get_id()}, {animal}")

    def get_animal_id(self):
        return int(self.prompt('Введите id животного: '))

    def get_animal_info_for_add(self):
        animal_type = self.prompt("Введите тип животного")
        name = self.prompt("Введите имя")
        age = int(self.prompt("Введите возраст"))
        gender = int(self.prompt("Введите пол"))
        place_residence = int(self.prompt("Введите место проживания"))
        return animal_type, name, age, gender, place_residence

    def print_add_success(self, animal):
        print(f'Животное {animal} успешно добавлено!')

    def prind_error_command(self):
        print('Нет такой команды!')

    def prompt(self, message):
        return input(message)

    def print_message(self, message):
        print(message)

    def print_exit(self):
        print('Выход из программы')
