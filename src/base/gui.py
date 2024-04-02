
import json
import tkinter as tk
from tkinter import  ttk


from ..base.base_class import BaseFunctionClass


# self
from ..db import DB

class GUI(BaseFunctionClass):
    V = (0, 0 ,0)
    
    def __init__(self):
        super(GUI, self).__init__()
        # music
        self.play_sound("open")
        
        self.root = tk.Tk()
        self.db = DB()
        self.db.creat_table()
        
        self.texts: dict = self.__get_texts()
        self.setting: dict = self.__get_settings()
        
        
        self.root.resizable(False, False) 
        
        self.root.title(self.setting.get("title"))
        self.root.iconphoto(False, tk.PhotoImage(file=self.setting.get("icon")))
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file=self.setting.get("icon"))) 
        
    
       
        
    def error_window(self, error_code: str, error_title: str = "error"):
        """Create and display an error window with given title and message."""
        window = tk.Toplevel(self.root)
        window.title(self.texts.get(error_title))

        label = ttk.Label(window, text=self.texts["error_code"][error_code])
        label.pack(padx=20, pady=20)
        
        # 添加确认按钮
        confirm_button = ttk.Button(window, text=self.texts.get("confirm"), command=window.destroy)
        confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

        # 添加取消按钮
        cancel_button = ttk.Button(window, text=self.texts.get("cancel"), command=window.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        
    def __get_texts(self) -> dict:
        with open('./data/texts.json', 'r') as file:
            texts: dict = json.load(file)
            
        # default
        return texts.get("CH")
    
    def __get_settings(self) -> dict:
        with open('./data/setting.json', 'r') as file:
            setting: dict = json.load(file)
            
        # default
        return setting
    

    def close(self):
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()
        
        
    def restart(self):
        self.root.destroy()
        self.__init__(tk.Tk())  
        
        # update settings
        self.texts: dict = self.__get_texts()
        self.setting: dict = self.__get_settings()
        self.run()
        
        
    def command(self,command: str):
        """use by test
        Args:
            command (str): _description_
        """
        pass