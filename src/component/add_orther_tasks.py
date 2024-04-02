import logging
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, Callable, Tuple

import tkinter.simpledialog as sd

class AddOtherTasks:
    def __init__(self, root: tk.Tk, texts: Dict[str, str], error_window: Callable):
        self.root = root
        self.texts = texts
        self.error_window = error_window
        error_window
        
        self.__layout()
        
    def __layout(self):
        for button_text in self.texts.get("add_other_tasks_list"):
            button = ttk.Button(self.root, text=button_text, command=lambda bt=button_text: self.open_input_dialog(bt))
            button.pack()
            
    def open_input_dialog(self, button_text: str):
        task = sd.askstring("Input", f"Enter task for {button_text}:")
        if task is not None:
            logging.info(f"New task for {button_text}: {task}")
        else:
            self.error_window("Error", "Task cannot be empty.")
