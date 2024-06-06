from typing import Literal
import torch
from transformers import BertModel, BertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.preprocess import preprocess_task

model_name = 'bert-base-chinese'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


__all__ = ['classify_task']


def get_embeddings(text_list):
    embeddings = []
    for text in text_list:
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=32)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().numpy())
    return embeddings



def classify_task(task, classifier, label_encoder, threshold=0.5)-> (tuple | Literal['其他']): 
            # 預處理任務
            task = preprocess_task(task)

            # 獲取嵌入向量
            embedding = get_embeddings([task])[0]

            # 使用模型進行預測
            category_encoded = classifier.predict([embedding])[0]

            # 獲取預測分數
            prediction_score = classifier.predict_proba([embedding])[0][category_encoded]
            

            # 如果預測分數低於閾值，顯示警告消息    
            if prediction_score < threshold:
                return "其他"

            # 轉換編碼為類別標籤
            category = label_encoder.inverse_transform([category_encoded])[0]

            # 返回類別標籤
            return category, prediction_score