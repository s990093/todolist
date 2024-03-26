import json
import tkinter as tk
from tkinter import  ttk

from env import ENV
from .style import Style

from .db import DB
from .mock import get_faker_tasks

# component
from .component.list import TaskFrame
from .component.navbar import Navbar

class GUI:
    V = (0, 0 ,0)
    
    def __init__(self):
        self.root = tk.Tk()
        self.db = DB()
        self.db.creat_table()
        
        self.texts: dict = self.__get_texts()
        
        self.root.title(ENV.get("title"))
        
        
    def error_window(self, error_title: str, error_message: str):
        """Create and display an error window with given title and message."""
        window = tk.Toplevel(self.root)
        window.title(error_title)

        label = ttk.Label(window, text=error_message)
        label.pack(padx=20, pady=20)
        
    def __get_texts(self) -> dict:
        with open('./data/texts.json', 'r') as file:
            texts: dict = json.load(file)
            
        # default
        
        return texts.get("CH")
    
    def __get_settings(self) -> dict:
        pass
    
    def close(self):
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()

class TodoListGUI(GUI):
    def __init__(self):
        super().__init__()
        
        self.style = Style()
        
        # Create frames for left and right sides
        self.left_frame = ttk.Frame(self.root)
        self.right_frame = ttk.Frame(self.root)
        
        # Grid configurations for left and right frames
      
        
        # self.root.columnconfigure(0, weight=1)  # Left column
        # self.root.columnconfigure(1, weight=9)  # Right column
        # self.root.rowconfigure(0, weight=1)     # Row

        # self.tasks = self.__get_task_listbox()
        self.tasks = self.__get_tasks()
        
        # task list
        self.task_list = TaskFrame(self.right_frame, self.root, self.tasks, self.style, self.texts)
        Navbar(self.left_frame, self.root, self.style, self.texts,
               self.error_window, 
               self.add_task,
               self.close)
        
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
    def add_task(self, task_name, priority, task_type):
        new_task = self.db.insert_task(task_name, priority, task_type)
        # self.task_list.update()
        self.tasks.append(self.db.serialize_task(new_task))
        
        
        self.task_list.update(self.tasks)

          
        
    def __get_tasks(self) -> list:
        rows = self.db.get_today_tasks()
        tasks = []
        for row in rows:
            tasks.append(self.db.serialize_task(row))
        return tasks


