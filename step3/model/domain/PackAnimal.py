from model.domain.HumanFriendsAnimal import HumanFriendsAnimal
from model.domain.Task import Task


class PackAnimal(HumanFriendsAnimal):
    def __init__(self, name, age, food_type, gender, place_residence):
        super().__init__(name, age, food_type, gender, place_residence)
        self.tasks = {}
        self.current_task = None

    def add_task(self, task_name):
        if self.tasks[task_name]:
            print(f"Задача {task_name} уже существует")
            return
        self.tasks[task_name] = Task(task_name)

    def get_tasks(self):
        return list(self.tasks.values())

    def do_task(self, task_name):
        if self.current_task:
            self.current_task.stop()
        if self.tasks[task_name]:
            self.tasks[task_name].do()
            self.current_task = self.tasks[task_name]
            return
        print(f"Задача {task_name} не найдена")

    def stop_current_task(self):
        if self.current_task:
            self.current_task.stop()
            self.current_task = None
        else:
            print("Нет текущей задачи")

    def remove_task(self, task_name):
        if self.tasks[task_name]:
            del self.tasks[task_name]
            return
        print(f"Задача {task_name} не найдена")

    def make_sound(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def run(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")