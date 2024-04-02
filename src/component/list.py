import tkinter as tk
from tkinter import ttk
from typing import Callable

from ..texts import ChangeTextField

class TaskFrame:
    def __init__(self, frame: tk.Frame, root: tk.Tk, tasks: list, style: dict, texts: dict, *args, **kwargs):
        self.root = root
        self.frame = frame
        self.tasks = tasks
        
        self.style = style
        self.texts = texts
        
        # Initialize the treeview
        self.task_treeview = ttk.Treeview(self.frame, selectmode="browse", columns=("Task Name", "Completed","Level", "Type"))
        self.task_treeview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Set column headings
        self.task_treeview.heading("Task Name", text=self.texts.get("table_name"))
        self.task_treeview.heading("Completed", text=self.texts.get("table_complete"))
        self.task_treeview.heading("Level", text=self.texts.get("table_pritory"))
        self.task_treeview.heading("Type", text=self.texts.get("table_type"))
        
        # Configure column widths
        self.task_treeview.column("#0", width=10)
        self.task_treeview.column("Task Name", width=200)
        self.task_treeview.column("Completed", width=100)
        self.task_treeview.column("Level", width=50)
        self.task_treeview.column("Type", width=100)
        
        # Configure column alignments
        self.task_treeview.column("#0", anchor="w")
        self.task_treeview.column("Task Name", anchor="center")
        self.task_treeview.column("Completed", anchor="center")
        self.task_treeview.column("Level", anchor="center")
        self.task_treeview.column("Type", anchor="center")
        
        # Populate tasks
        self.populate_tasks(self.tasks)
        
        # Bind double click event
        self.task_treeview.bind("<Double-1>", self.toggle_completion)

    def populate_tasks(self, tasks):
        # Insert tasks
        for idx, task in enumerate(tasks):
            task_name = task['name']
            completed = ChangeTextField.int_number_to_complete(self.texts, task.get('completed'))
            level = ChangeTextField.level_change_to_text(self.texts, int(task.get('level')))
            task_type = ChangeTextField.type_change_to_text(self.texts, task.get("type"))
            self.task_treeview.insert("", tk.END, values=(task_name, completed,level, task_type))
            
            
    def toggle_completion(self, event):
        # Get item clicked
        item_clicked = self.task_treeview.selection()
        if not item_clicked:
            return
        task_name = self.task_treeview.item(item_clicked, "values")[0]
        current_status =  ChangeTextField.complete_to_int_number(self.texts, self.task_treeview.item(item_clicked, "values")[1])
        new_status = 1 if current_status == 0 else 0 
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = new_status
                break
        
        self.update(self.tasks)
        
 
    def update(self, new_tasks: list):
        # delete old tasks
        self.task_treeview.delete(*self.task_treeview.get_children())        
        
        self.populate_tasks(self.__sort(new_tasks))

            
    def __sort(self, tasks: list):
        def sort_key(task):
            return (task["completed"], ChangeTextField.level_change_to_text(self.texts, task["level"]))
        
        
        sorted_tasks = sorted(tasks, key=sort_key)
        
        return sorted_tasks
    
  