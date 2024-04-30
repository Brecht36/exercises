from datetime import date, timedelta, datetime

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False
    
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
class TaskList:
    def __init__(self):
        self.__tasklist = list()

    def add_task(self, task):
        if task.due_date >= date.today():
            self.__tasklist.append(task)
        else:
            raise RuntimeError

    def __len__(self):
        return len(self.__task_list)
        # gives the number of tasks in the list
    @property
    def finished_tasks(self):
        return [task for task in self.__tasklist if task.finished == True]
    @property
    def due_tasks(self):
        return [task for task in self.__tasklist if task.finished == False]
    @property
    def overdue_tasks(self):
        return [task for task in self.__tasklist if task.finished == False and task.due_date < date.today()]
    
# task = Task('A', datetime.tomorrow())
# task2 = Task('B', datetime.tomorrow())
# task3 = Task('C', datetime.tomorrow())
# taskList = TaskList()
# TaskList.add_task(task)
# TaskList.add_task(task2)
# TaskList.add_task(task3)
# len(taskList)