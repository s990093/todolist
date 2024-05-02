r"""controller view """
import json

import webview


from .mock import get_faker_tasks
from .base.gui import GUI

# component
from .component.list import TaskFrame
from .component.navbar import Navbar



# error
from .base.error import WindowError

class TodoListGUI(GUI):  
    def __init__(self):
        super().__init__()
                
        self.tasks = self.__get_tasks()
        
    def add_task(self, task_name, priority, task_type):
        try:     
            new_task = self.db.insert_task(task_name, priority, task_type)
            
            # if repect type to insert to db
            if self.ChangeTexts.type_change_to_text(self.texts, task_type) == self.TEXTS.get("repeat"):
                self.db.insert_repect_tasks(task_name)
                
            # self.task_list.update()
            self.tasks.append(self.db.serialize_task(new_task))
            # update
            self.main_task_list.update(self.tasks)
          
        except WindowError as w:
            self.error_window(str(w.code))
            
    def __get_tasks(self) -> list:
        self.db.check_and_insert_repeat_tasks()
        rows = self.db.get_today_tasks()
        tasks = []
        for row in rows:
            tasks.append(self.db.serialize_task(row))
        return tasks


