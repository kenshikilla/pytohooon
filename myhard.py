from typing import List
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    description: str
    date: List
    deadline: List
    priority: bool


    def __str__(self):
        print([i for i in self.date]) #вывод списка date
        return f'''Название задачи:{self.name}Описание задачи:{self.description}Дата задачи: {self.date[0]}.{self.date[1]}.{self.date[2]}Дедлайн задачи: {self.deadline[0]}.{self.deadline[1]}.{self.deadline[2]}
'''

class TaskManager:
    def __init__(self, location: str):
        self.location = location
        self.tasks = []

    def __str__(self):
        return f'''{[print(i) for i in self.tasks]}'''

    def add_task(self, task):
        self.tasks.append(task)
        
    def write_txt(self):
        with open(self.location, "w") as t:
            for i in self.tasks:
                t.write(f'''Название задачи: {i.name}Описание задачи: {i.description}Дата задачи: {i.date[0]}.{i.date[1]}.{i.date[2]}Дедлайн задачи: {i.deadline[0]}.{i.deadline[1]}.{i.deadline[2]}Приоритет задачи: {i.priority}#''')

    def closing_task(self, name: str):
        for i in self.tasks:
            if i.name == name:
                self.tasks.remove(i)
        self.write_txt()

    def changing_task(self, name_of_task: str, type_of: str, new_value=None):
        for i in self.tasks:
            if i.name == name_of_task:
                if type_of == "Название задачи":
                    i.name = new_value
                elif type_of == "Описание задачи":
                    i.description = new_value
                elif type_of == "Дедлайн задачи":
                    if new_value == None:
                        i.deadline = [None, None, None]
                    else:
                        i.deadline = new_value
                elif type_of == "Приоритет задачи":
                    if i.priority == True:
                        i.priority = False
                    else:
                        i.priority = True
                    print("---------------")
                    print(f"Приоритет изменен на: {i.priority}")
                    print("---------------")

    def notyfication(self, today_date):
        print(f"Ежедневные задачи: ")
        for i in self.tasks:
            if today_date[2] == i.deadline[2]:
                if today_date[1] == i.deadline[1]:
                    if today_date[0] + 1 == i.deadline[0]: #все должно совпадать
                        print(i)

    def reading_txt(self):
        with open(self.location, "r") as file:
            text = file.read()
            text = text.split("#")
            final_text_list = []
            for i in text:
                i = str(i)
                i = i.split("\n")
                final_text_list.append(i)
            self.tasks = []
            for i in range(len(final_text_list) - 1):
                if i != 0:
                    final_text_list[i].remove('')
                    final_text_list[i].remove('')
                elif i == 0:
                    final_text_list[i].remove('')

                name = final_text_list[i][0].replace("Название задачи: ", "")
                description = final_text_list[i][1].replace("Описание задачи: ", "")
                date = final_text_list[i][2].replace("Дата задачи: ", "").split(".")
                deadline = final_text_list[i][3].replace("Дедлайн задачи: ", "").split(".")
                priority = final_text_list[i][4].replace("Приоритет задачи: ", "")                    

                if priority == "Важное":
                    priority = True
                elif priority == "Нормально":
                    priority = False

                self.add_task(Task(name, description, date, deadline, priority))
            final_text_list.pop(-1)

    def todays_tasks(self, today_date):
        for i in self.tasks:
            if today_date == i.deadline:
                print("Это задачи на сегодня:")
                print(i)

    def only(self, sett):
        print("Это задача на сегодня:")
        for i in self.tasks:
            if i.priority == sett:
                print(i)

task_manager = TaskManager("tasks.txt")
task = Task(name="Купить продукты. ", description="Купить молоко, яйца, хлеб. ", date=[2023, 3, 10], deadline=[2023, 3, 12], priority=True)
task_manager.add_task(task)
task_manager.write_txt()


print(task_manager)