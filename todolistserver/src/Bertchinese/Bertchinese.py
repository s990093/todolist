import json
import os



import torch
from transformers import BertModel, BertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
from tqdm import tqdm 
import numpy as np

# rich
from rich import pretty
from rich.panel import Panel
from rich.console import Console

from preprocess import TaskPreprocessor

__all__ = ['Model']

class Model(object):
    def __init__(self, 
                 json_file_path: str, 
                 model_path: str,
                 model_name: str = 'bert-base-chinese',
                 *args, **kwargs):
        """_summary_

        Args:
            json_file_path (str): _description_
            model_path (str): _description_
            model_name (str, optional): _description_. Defaults to 'bert-base-chinese'.
        """
        super(object, self).__init__(*args, **kwargs)
        
        self.__script_dir = os.path.dirname(os.path.abspath(__file__))
        self._json_file_path = os.path.join( self.__script_dir , 'json', json_file_path)
        self.model_path = os.path.join( self.__script_dir , model_path)
        
        self._model_name = model_name
        self.taskreprocessor = TaskPreprocessor()
        
                
        pretty.install()
        self.console = Console()
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

        # BertTokenizer model 
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.label_encoder = LabelEncoder()
        

        self.classifier = self.__load_model()

        # category_encoded
        self.combined_data['category_encoded'] = self.label_encoder.fit_transform(self.combined_data['category'])
        
    def __load_model(self):
        if os.path.exists(self.model_path):
            return torch.load(self.model_path)
        else:
            return None

    def classify_task(self, task: str, threshold=0.5):
        """_summary_
        entry point for classification

        Args:
            task (str): _description_
            threshold (float, optional): _description_. Defaults to 0.5.

        Returns:
            _type_: _description_
        """
        # 預處理任務
        task = self.taskreprocessor.preprocess_task(task)

        # 獲取嵌入向量
        embedding = self.__get_embeddings([task])[0]

        # 使用模型進行預測
        category_encoded = self.classifier.predict([embedding])[0]

        # 獲取預測分數
        prediction_score = self.classifier.predict_proba([embedding])[0][category_encoded]
        

        # 如果預測分數低於閾值，顯示警告消息    
        if prediction_score < threshold:
            return -1

        # 轉換編碼為類別標籤
        category = self.label_encoder.inverse_transform([category_encoded])[0]

        # 返回類別標籤
        return category, prediction_score
    
    def train_data(self, solver, max_iter=1000):
        """_summary_

        Args:
            solver (_type_): _description_
            max_iter (int, optional): _description_. Defaults to 1000.
        """
        
        tasks = self.combined_data['task']
        categories = self.combined_data['category_encoded']
        embeddings = self.__get_embeddings(tasks)
        
        # 先将数据和标签合并在一起
        data_with_labels = list(zip(embeddings, categories))

        # 打乱数据
        np.random.shuffle(data_with_labels)

        # 将数据和标签分开
        shuffled_embeddings, shuffled_embeddings = zip(*data_with_labels)
        
        # self.console.print(shuffled_embeddings, shuffled_embeddings)

        # 分割数据集

        X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42)

        # 训练分类器
        classifier = LogisticRegression(solver=solver, max_iter=max_iter)
        classifier.fit(X_train, y_train)

        # 预测并评估
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # 保存模型
        torch.save(classifier, self.model_path)

        # 使用 tqdm 显示进度条和模型精度
        with tqdm(total=100, desc="Training Progress") as pbar:
            pbar.update(100)  # 更新进度条到 100%

        # 显示模型精度
        accuracy_panel = Panel.fit(f'Accuracy: {accuracy:.2f}', title="Accuracy", border_style="blue")
        self.console.print(accuracy_panel)
        
    def test(self, new_task: str):
        """_summary_

        Args:
            new_task (str): _description_
        """
        predicted_category , prediction_score= self.classify_task(new_task)
        
        if predicted_category == -1:
            print("其他")
            
        self.console.print(
            Panel.fit(
                f"Task -> {new_task} \nPredicted Category -> {predicted_category} \nprediction_score -> {prediction_score}",
                title="Model Information",
                border_style="green",
                padding=(1, 2)
            )
        )
            
            
    def __get_embeddings(self, text_list: str):
        embeddings = []
        for text in text_list:
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=32)
            with torch.no_grad():
                outputs = self.model(**inputs)
            embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().numpy())
        return embeddings
        
    def __time(self):
        pass