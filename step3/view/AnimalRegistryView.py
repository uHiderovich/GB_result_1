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

    def get_command(self):
        return self.promnt('Введите команду: ')

    def print_animals(self, animals):
        print('-------------------')
        print('Список животных:')
        for animal in animals:
            print(f"ID: {animal.id}, " + animal)
        print('-------------------')

    def print_selected_animal(self, animal):
        print('Выбранное животное: ')
        print(f"ID: {animal.id}, {animal}")

    def get_animal_id(self):
        return int(self.promnt('Введите id животного: '))

    def get_animal_info_for_add(self):
        return self.promnt(f'Введите данные животного для добавления в формате: имя, возраст, пол, место проживания')

    def print_add_success(self):
        print('Животное успешно добавлено!')

    def promnt(self, message):
        return input(message)

    def print_exit(self):
        print('Выход из программы')
