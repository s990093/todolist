import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, Callable, Tuple

# self
from ..texts import ChangeTextField
from ..base.base_class import BaseFunctionClass
from ..style import Style
from .add_orther_tasks import AddOtherTasks



class Navbar(BaseFunctionClass):
    def __init__(self, frame: tk.Frame, root: tk.Tk, style: Style, texts: Dict[str, str], error_window: Callable, add_task: Callable, close: Callable, *args: Tuple[Any], **kwargs: Dict[str, Any]):
        super(Navbar, self).__init__(args, kwargs)
        self.root = root
        self.frame = frame
        self.style = style
        self.texts = texts
        
        # func api
        self.error_window = error_window
        self.close = close
        self.add_task = add_task
        
        
        self.__layout()
        
        
    def __layout(self):  
        # Navigation bar
        buttons = [
            (self.texts.get("add_tasks"), self.add_tasks),      
            (self.texts.get("add_other_tasks"), self.add_other_tasks),
            (self.texts.get("analysis"), self.analyze),
            (self.texts.get("other"), self.other),
            (self.texts.get("close"), self.close_app)
        ]

        for idx, (button_text, command) in enumerate(buttons):
            btn = ttk.Button(self.frame, text=button_text, width=10, command=command)
            btn.grid(row=idx, column=0, sticky="ew", padx=10, pady=10)
            
    def add_tasks(self):
        # music
        task_window = tk.Toplevel(self.root, padx=10, pady=10)
        task_window.title(self.texts.get("add_tasks"))

        def create_task(task_name, priority, task_type):
            if not task_name:  # 檢查任務名稱是否為空
                self.error_window("501", "error_empty_mes")
                return
            
            self.add_task(task_name, priority, task_type)
            
            task_window.destroy()
            
        # 創建新的 Tkinter 視窗
        # 添加任務名稱的標籤和輸入框到新視窗中
        ttk.Label(task_window, text=self.texts.get("task_name")).pack(pady=5)
        task_name_entry = ttk.Entry(task_window)
        task_name_entry.pack(pady=5)
        
        
        # 添加任務優先級的標籤和下拉框到新視窗中
        ttk.Label(task_window, text=self.texts.get("task_priority")).pack(pady=5)

        # 定義優先級選項（從1到5）
        priority_options = [ChangeTextField.level_change_to_text(self.texts, i) for i in range(1, 4)]
        # 創建下拉框並設置選項
        priority = ttk.Combobox(task_window, values=priority_options)
        priority.pack(pady=5)
        # default priority
        priority.set(ChangeTextField.level_change_to_text(self.texts, 1)) 
        
        
        ttk.Label(task_window, text=self.texts.get("task_type")).pack(pady=5)
        task_type_options = [ChangeTextField.type_change_to_text(self.texts, 0), ChangeTextField.type_change_to_text(self.texts, 1)] 
        task_type_combo = ttk.Combobox(task_window, values=task_type_options)
        task_type_combo.pack(pady=5)
        # default task type
        task_type_combo.set(ChangeTextField.type_change_to_text(self.texts, 1)) 

        

        # 添加確定按鈕到新視窗中
        ttk.Button(task_window, text=self.texts.get("confirm"), 
            command=lambda: create_task(task_name_entry.get(),
                                        ChangeTextField.text_change_to_int_level(self.texts, priority.get()),
                                        ChangeTextField.text_change_to_type(self.texts, task_type_combo.get()))).pack(pady=5)
        
    def add_other_tasks(self):
        # add = AddOtherTasks(self.root, self.texts, self.error_window)
        pass
        

    def analyze(self):
        # 分析的相應代碼
        pass
    
    def other(self):
        task_window = tk.Toplevel(self.root, padx=10, pady=10)
        task_window.title(self.texts.get("other"))


    def close_app(self):
        self.close()