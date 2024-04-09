import json
import logging
import os
from queue import Queue
from threading import Thread
from playsound import playsound

from ..texts import ChangeTextField
from .tool import to_prase_json

class BaseWithSetting(object):
    SETTING = to_prase_json("./data/setting.json")
    USERSETTING = to_prase_json("./data/user_setting.json")
    TEXTS : dict = to_prase_json("./data/texts.json").get(SETTING.get('language'))
    ChangeTexts = ChangeTextField()
    
    
    def to_prase_json(self, filename: str) -> dict:
        with open(filename, 'r') as file:
            data: dict = json.load(file)
            
        return data
    
        
    def _path(self, path: str, filename: str) -> str:
        return f"./{path}/{filename}"

class BaseFunctionClass(BaseWithSetting):
    def __init__(self,sound: bool = False, canLog: bool = True, *args, **kwargs):
        super(BaseFunctionClass, self).__init__()
        """_summary_

        Args:
            sound (bool, optional): _description_. Defaults to True.
            log (bool, optional): _description_. Defaults to True.
        """
        # setup_logging() 
        # logger
        self._log = canLog
        self.log = logging.getLogger(__name__)  
        
        self.__sound = self.USERSETTING.get('sound', sound)
        
        
        # music
        self.sound_queue = Queue() 
        
        # 创建并启动播放音效的线程
        sound_thread = Thread(target=self.play_sound_thread)
        sound_thread.daemon = True  
        sound_thread.start()
        
    def play_sound_thread(self):
        while True:
            sound_file = self.sound_queue.get()
            playsound(sound_file)
            self.sound_queue.task_done() 
    
    def play_sound(self, sound_file: str):
        """_summary_

        Args:
            sound_file (str): _description_
        """
        if self.__sound:
            self.sound_queue.put(self.music_path(f"{sound_file}.wav"))
        else:
            return
    
    def static_path(self, filename: str) -> str:
        return self._path("static", filename)
    
    def music_path(self, path: str) -> str:
        return self._path("asset/music", path)
    
    def data_path(self, filename: str) -> str:
        return self._path("data", filename)
    
