import json
import os
import webview

from ..base.tool import auto_load_css 


from .base_class import BaseFunctionClass
from ..db import DB




class GUI(BaseFunctionClass):
    V = (0, 0 ,0)
    
    def __init__(self):
        super(GUI, self).__init__()
        # music
        self.play_sound("open")
        
        self.db = DB()
        self.db.creat_table() 

        self.window = webview.create_window(
            self.SETTING.get("title"), 
            self.static_path("index.html"),     
            resizable=False,
            )

    def error_window(self, error_code: str, error_title: str = "error"):
        """Create and display an error window with given title and message."""
        self.window.evaluate_js(f"errorWindow('{error_code}', '{self.TEXTS.get(error_title)}')")

  
    def close(self):
        self.window.close()
        
    def run(self):
        webview.start(auto_load_css, self.window)
        
    def restart(self):
        self.webview.window.close()
        self.run()
        
    def command(self,command: str):
        """use by test
        Args:
            command (str): _description_
        """
        pass
    

