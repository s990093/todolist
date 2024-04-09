from .base.base_class import BaseWithSetting


class ChangeTextField(BaseWithSetting):
    """_summary_

    Returns:
        _type_: _description_
    """
    @staticmethod
    def level_change_to_text(texts: dict, level: int):
        """_summary_

        Args:
            texts (dict): _description_
            level (int): _description_

        Returns:
            _type_: _description_
        """
        level_texts = {
            1: texts.get("high"),
            2: texts.get("medium"),
            3: texts.get("low"),
        }
        return level_texts.get(level) 
    @staticmethod
    def text_change_to_int_level(texts: dict, text: str):
        """_summary_

        Args:
            texts (dict): _description_
            text (str): _description_

        Returns:
            _type_: _description_
        """
        level_texts = {
            texts.get("high"): 1,
            texts.get("medium"): 2,
            texts.get("low"): 3,
        }
        return level_texts.get(text) 
    @staticmethod
    def type_change_to_text(texts: dict, task_type: int):
        """_summary_

        Args:
            texts (dict): _description_
            task_type (int): _description_

        Returns:
            _type_: _description_
        """
        task_type_texts = {
            0: texts.get("repeat"),
            1: texts.get("short")
        }
        return task_type_texts.get(task_type) 
    
       
    @staticmethod
    def text_change_to_type(texts: dict, text: str):
        """_summary_

        Args:
            texts (dict): _description_
            text (str): _description_

        Returns:
            _type_: _description_
        """
        task_type_texts = {
            texts.get("repeat"): 0,
            texts.get("short"): 1,
        }
        return task_type_texts.get(text) 
    
    
    @staticmethod
    def complete_to_int_number(texts: dict, text: str):
        """_summary_

        Args:
            texts (dict): _description_
            text (str): _description_

        Returns:
            _type_: _description_
        """
        complete_texts = {
            texts.get("yes"): 0,
            texts.get("no"): 1
        }
        return complete_texts.get(text) 
        
    @staticmethod
    def int_number_to_complete(texts: dict, text: str):
        """_summary_
        Args:
            texts (dict): _description_
            text (str): _description_

        Returns:
            _type_: _description_
        """
        complete_texts = {
            0:texts.get("yes"),
            1: texts.get("no")
        }
        return complete_texts.get(text)
    
