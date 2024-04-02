import json
import tkinter as tk
from tkinter import  ttk

from env import ENV
from .texts import ChangeTextField
from .style import Style

from .db import DB
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
        
        self.style = Style()
        
        self.tasks = self.__get_tasks()

        # Create frames for left and right sides
        self.left_frame = ttk.Frame(self.root)
        self.right_frame = ttk.Frame(self.root)
        
        # Grid configurations for left and right frames
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Initialize notebook for different task lists
        self.notebook = ttk.Notebook(self.right_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # Add two tabs to the notebook
        # TODO: 需要修改
        for tab_text in self.texts.get("notebook_list"):
            tab_frame = ttk.Frame(self.notebook)
            self.main_task_list = TaskFrame(tab_frame, self.root, self.tasks, self.style, self.texts)
            self.notebook.add(tab_frame, text=tab_text)

        # Create navigation bar in the left frame
        Navbar(self.left_frame, self.root, self.style, self.texts, self.error_window, self.add_task, self.close)
        
    def add_task(self, task_name, priority, task_type):
        try:     
            new_task = self.db.insert_task(task_name, priority, task_type)
            
            # if repect type to insert to db
            if ChangeTextField.type_change_to_text(self.texts, task_type) == self.texts.get("repeat"):
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


