class AnimalCommandsBehaviourView:
    def print_commands_menu(self):
        print('- add_command для добавления новой команды')
        print('- show_all_commands для просмотра всех команд')
        print('- do_command выполнить команду')

    def print_add_command(self):
        return input("Ввведите название команды: ")

    def print_how_command(self, animal):
        return input(f"Какую команду должен выполнить {animal}: ")

    def print_commands_of_animal(self, commands):
        for command in commands:
            print(command)

    def print_message(self, message):
        print(message)
