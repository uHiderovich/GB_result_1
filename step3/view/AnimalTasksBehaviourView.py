class AnimalTasksBehaviourView:
    def print_tasks_menu(self):
        print('- add_task для добавления новой задачи')
        print('- show_all_tasks для просмотра всех задач')
        print('- do_task для изменения текущей задачи')

    def print_add_task(self):
        return input("Ввведите название задача: ")

    def print_how_task(self, animal):
        return input(f"Какую задачу должен выполнять {animal}: ")

    def print_tasks_of_animal(self, tasks):
        if len(tasks) == 0:
            print("Список задач пока что пуст:(")
        else:
            for task in tasks:
                print(task)

    def print_message(self, message):
        print(message)
