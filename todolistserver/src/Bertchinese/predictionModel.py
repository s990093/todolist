import os
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch
from tqdm import tqdm
import numpy as np

from src.Bertchinese.baseModel import BaseModel


__all__ = ['PredictionModel']

class PredictionModel(BaseModel):
    def __init__(self, json_file_path: str, model_path: str, model_name: str = 'bert-base-chinese', env: dict|None = None, *args, **kwargs):
        super(PredictionModel, self).__init__(json_file_path, model_path, model_name, *args, **kwargs)
        
        self.classifier = self.load_model()
        
        self.env = env


    def predict(self, task: str):
        """_summary_
        entry point for classification
        """
        # 預處理任務
        task = self.taskreprocessor.preprocess_task(task)

        # 獲取嵌入向量
        embedding = self.get_embeddings([task])[0]

        # 使用模型進行預測
        category_encoded = self.classifier.predict([embedding])[0]

        # 獲取預測分數
        prediction_score = self.classifier.predict_proba([embedding])[0][category_encoded]
        

        # 如果預測分數低於閾值，顯示警告消息    
        if prediction_score < self.env.get('threshold', 0.5):
            return -1

        # 轉換編碼為類別標籤
        category = self.label_encoder.inverse_transform([category_encoded])[0]
     
        self.console.print(
            self.Panel.fit(
                f"Task -> {task} \nPredicted Category -> {category} \nprediction_score -> {prediction_score}",
                title="Model Information",
                border_style="green",
                padding=(1, 2)
            )
        )
        
        # 返回類別標籤
        return category, prediction_score
    
    
    
    def test(self, new_task: str):
        """_summary_

        Args:
            new_task (str): _description_
        """
        predicted_category , prediction_score= self.predict(new_task)
        
        if predicted_category == -1:
            print("其他")
            
        self.console.print(
            self.Panel.fit(
                f"Task -> {new_task} \nPredicted Category -> {predicted_category} \nprediction_score -> {prediction_score}",
                title="Model Information",
                border_style="green",
                padding=(1, 2)
            )
        )
            