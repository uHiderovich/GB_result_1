from model.domain.HumanFriendsAnimal import HumanFriendsAnimal
from model.domain.Task import Task
from model.exeptions.CommandException import CommandException


class PackAnimal(HumanFriendsAnimal):
    def __init__(self, name, age, food_type, gender, place_residence):
        """
        Класс, описывающий животное, которое может выполнять задачи
        :param name: имя животного
        :param age: возраст животного
        :param food_type: тип пищи, которую любит животное
        :param gender: пол животного
        :param place_residence: место жительства животного
        """
        super().__init__(name, age, food_type, gender, place_residence)
        self.tasks = {}
        self.current_task = None

    def add_task(self, task_name):
        """
        Добавить задачу животному
        :param task_name: название задачи
        :return: None
        """
        if self.tasks[task_name]:
            raise CommandException(f"Задача {task_name} уже существует")
        self.tasks[task_name] = Task(task_name)

    def get_tasks(self):
        """
        Получить список задач животного
        :return: list
        """
        return list(self.tasks.values())

    def do_task(self, task_name):
        """
        Выполнить задачу животного
        :param task_name: название задачи
        :return: None
        """
        if not self.tasks[task_name]:
            raise CommandException(f"Задача {task_name} не найдена")
        self.stop_current_task()
        self.tasks[task_name].do()
        self.current_task = self.tasks[task_name]

    def stop_current_task(self):
        """
        Остановить текущую задачу
        :return: None
        """
        if self.current_task:
            self.current_task.stop()
            self.current_task = None

    def remove_task(self, task_name):
        """
        Удалить задачу животного
        :param task_name: название задачи
        :return: None
        """
        if not self.tasks[task_name]:
            raise CommandException(f"Задача {task_name} не найдена")
        del self.tasks[task_name]

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")