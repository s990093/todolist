import json
import os
from sklearn.calibration import LabelEncoder
import torch
from transformers import BertModel, BertTokenizer
from rich import pretty
from rich.panel import Panel
from rich.console import Console
from preprocess import TaskPreprocessor

class BaseModel:
    def __init__(self, json_file_path: str, model_path: str, model_name: str = 'bert-base-chinese', *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.__script_dir = os.path.dirname(os.path.abspath(__file__))
        self._json_file_path = os.path.join(self.__script_dir, 'json', json_file_path)
        self.model_path = os.path.join(self.__script_dir, model_path)
        self._model_name = model_name
        self.taskreprocessor = TaskPreprocessor()
        
        pretty.install()
        self.console = Console()
        self.Panel = Panel
        self.console.print(
            Panel.fit(
                f"[bold green]Load model ->[/bold green] [yellow]{self._model_name}[/yellow] \n[bold green]Model path ->[/bold green] [yellow]{self.model_path}[/yellow]",
                title="Model Information",
                border_style="green",
                padding=(1, 2)
            )
        )
        
        with open(self._json_file_path, 'r', encoding='utf-8') as f:
            self.combined_data = json.load(f)
        
        self.tokenizer = BertTokenizer.from_pretrained(self._model_name)
        self.model = BertModel.from_pretrained(self._model_name)
        self.label_encoder = LabelEncoder()
        self.combined_data['category_encoded'] = self.label_encoder.fit_transform(self.combined_data['category'])

        
        
    def get_embeddings(self, text_list: str):
        embeddings = []
        for text in text_list:
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=32)
            with torch.no_grad():
                outputs = self.model(**inputs)
            embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().numpy())
        return embeddings
      
      
    def __str__(self) -> str:
        print("BaseModel")
        
    def load_model(self):
        if os.path.exists(self.model_path):
            return torch.load(self.model_path)
        else:
            return None
