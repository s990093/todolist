import logging
from queue import Queue
from threading import Thread
from playsound import playsound

class BaseFunctionClass:
    """_summary_
    """
    def __init__(self, sound: bool = True, log: bool = True, *args, **kwargs):
        """_summary_

        Args:
            sound (bool, optional): _description_. Defaults to True.
            log (bool, optional): _description_. Defaults to True.
        """
        # setup_logging() 
        # logger
        self.log = logging.getLogger(__name__)  
        
        self.__sound = sound
        
        # music
        self.sound_queue = Queue() 
        
        
        # 创建并启动播放音效的线程
        sound_thread = Thread(target=self.play_sound_thread)
        sound_thread.daemon = True  #
        sound_thread.start()
        
        

        
    def play_sound_thread(self):
        while True:
            sound_file = self.sound_queue.get()
            playsound(sound_file)
            self.sound_queue.task_done() 
    
    def play_sound(self, sound_file: str):
        if self.__sound:
            self.sound_queue.put(f"./asset/music/{sound_file}.wav")
        else:
            return
    