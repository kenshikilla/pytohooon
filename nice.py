from dataclasses import dataclass
from typing import List
import unittest

@dataclass
class Task:
    name: str
    description: str
    date: int
    deadline: int
    importance: str

class TaskManager:
    def __init__(self, location: str):
        self.loc = location
        self.tasks = []

    def add_task(self):
        name = input("Придумайте название задачи: ")
        description = input("Введите описание: ")
        date = input("Дата: ")
        deadline = input("Дедлайн: ")
        importance = input("Важна ли задача? (да или нет): ")
        self.task = Task(name=name, description=description, date=date, deadline=deadline, importance=importance)
        self.tasks.append(self.task)

        with open("txt.txt", "a") as f:
            print(f"Название задачи: {self.task.name}", file=f)
            print(f"Описание: {self.task.description}", file=f)
            print(f"Дата задачи: {self.task.date}", file=f)
            print(f"Дедлайн: {self.task.deadline}", file=f)
            print(f"Важность: {self.task.importance}\n", file=f)

        print("Задача добавлена")

    def delete_task(self):
        name = input("Введите название задачи, которую нужно удалить: ")
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Задача '{name}' удалена")
                break
        else:
            print(f"Задача '{name}' не найдена")

    def change_task(self):
        change = input("Введите то, что хотели бы изменить в данной задаче: ")
        with open("txt.txt", 'w') as f:
            f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.description}\nДата:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.importance}")

        if change == "Название задачи":
            self.task.name = input("Введите новое название задачи: ")
            print("Задача изменена")
        elif change == "Описание":
            self.task.description = input("Введите новое описание задачи: ")
            print("Описание изменено")
        elif change == "Дата":
            self.task.date = input("Введите новую дату задачи: ")
            print("Дата изменена")
        elif change == "Дедлайн":
            self.task.deadline = input("Введите новый дедлайн задачи: ")
            print("Дедлайн изменен")
        elif change == "Важность":
            self.task.importance = input("Введите новую важность задачи: ")
            print("Важность изменена")
       
a = TaskManager(location="tasks.txt")
a.add_task()
a.delete_task()
a.change_task()


