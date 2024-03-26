import logging
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, Callable, Tuple

from ..log import setup_logging

from ..style import Style


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Navbar:
    def __init__(self, frame: tk.Frame, root: tk.Tk, style: Style, texts: Dict[str, str], error_window: Callable, add_task: Callable, close: Callable, *args: Tuple[Any], **kwargs: Dict[str, Any]):
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
            (self.texts.get("close"), self.close_app)
        ]

        for idx, (button_text, command) in enumerate(buttons):
            btn = ttk.Button(self.frame, text=button_text, width=10, command=command)
            btn.grid(row=idx, column=0, sticky="ew", padx=10, pady=10)

    def add_tasks(self):
        task_window = tk.Toplevel(self.root, padx=10, pady=10)
        task_window.title(self.texts.get("add_tasks"))

        def create_task(task_name, priority):
            if not task_name:  # 檢查任務名稱是否為空
                self.error_window(self.texts.get("type_error_title"), self.texts.get("error_empty_mes"))
                return
            
            self.add_task(task_name, priority, 0)
            logger.info(f"adding task {task_name, priority}")
            
            task_window.destroy()
            
        # 創建新的 Tkinter 視窗
        # 添加任務名稱的標籤和輸入框到新視窗中
        ttk.Label(task_window, text=self.texts.get("task_name")).pack(pady=5)
        task_name_entry = ttk.Entry(task_window)
        task_name_entry.pack(pady=5)

        # 添加任務優先級的標籤和下拉框到新視窗中
        ttk.Label(task_window, text=self.texts.get("task_priority")).pack(pady=5)

        # 定義優先級選項（從1到5）
        priority_options = [str(i) for i in range(1, 4)]

        # 創建下拉框並設置選項
        priority_combo = ttk.Combobox(task_window, values=priority_options)
        priority_combo.pack(pady=5)
        
        # default priority
        priority_combo.set("1")

        # 添加確定按鈕到新視窗中
        ttk.Button(task_window, text=self.texts.get("confirm"), command=lambda: create_task(task_name_entry.get(), priority_combo.get())).pack(pady=5)
        
        
        


    def add_other_tasks(self):
        # 添加其他任務的相應代碼
        pass

    def analyze(self):
        # 分析的相應代碼
        pass

    def close_app(self):
        self.close()