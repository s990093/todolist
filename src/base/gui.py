import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk

class GUI():
    def __init__(self, conf:dict[str, str | bool | int], *args, **kwargs):
        super(self).__init__(*args, **kwargs)
        
        self.root = tk.Tk()
        self.root.title(conf.get('title'))

        