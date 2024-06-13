import os
import json
import time
import torch
import numpy as np
import copy
import joblib
from transformers import BertTokenizer, BertModel
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import pretty
import collections

class TaskPreprocessor:
    def preprocess_task(self, task):
        # Implement your task preprocessing logic here
        return task

class BaseModel:
    def __init__(self, json_file_path: str, model_path: str, model_name: str = 'bert-base-chinese', *args, **kwargs):
        
        self.__script_dir = os.path.dirname(os.path.abspath(__file__))
        self._json_file_path = os.path.join(self.__script_dir, 'json', json_file_path)
        self.model_path = os.path.join(self.__script_dir, model_path)
        self._model_name = model_name
        self.taskreprocessor = TaskPreprocessor()
        
        pretty.install()
        self.console = Console()
        self.Table = copy.copy(Table)
        self.Panel = copy.copy(Panel)
        
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
        
        # Encode the categories
        self.combined_data['category_encoded'] = self.label_encoder.fit_transform(self.combined_data['category'])

    def get_embeddings(self, text_list):
        embeddings = []
        for text in text_list:
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=32)
            with torch.no_grad():
                outputs = self.model(**inputs)
            embedding = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
            embeddings.append(embedding)
        return embeddings

    def train(self):
        # Extract tasks and category labels
        tasks = self.combined_data['task']
        categories = self.combined_data['category_encoded']

        # Generate embeddings for tasks
        embeddings = self.get_embeddings(tasks)

        # Handle class imbalance with random oversampling
        oversampler = RandomOverSampler(random_state=42)
        embeddings_resampled, categories_resampled = oversampler.fit_resample(embeddings, categories)

        # Convert to NumPy arrays if not already
        embeddings_resampled = np.array(embeddings_resampled)
        categories_resampled = np.array(categories_resampled)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(embeddings_resampled, categories_resampled, test_size=0.2, random_state=42, shuffle=True)

        # Define the classifier
        classifier = RandomForestClassifier(n_estimators=100, random_state=42)  # Using 100 trees

        # Fit the classifier
        classifier.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Save the model and label encoder
        joblib.dump(classifier, self.model_path)
        joblib.dump(self.label_encoder, self.model_path.replace('.pkl', '_label_encoder.pkl'))
        self.classifier = classifier

        # Generate and display classification report
        unique_categories = [category for category, count in collections.Counter(self.combined_data['category']).items() if count > 1]
        report = classification_report(y_test, y_pred, target_names=unique_categories)
        report_panel = self.Panel(report, title="Classification Report", border_style="green")
        self.console.print(report_panel)

        end_time = time.time()
        
        # Show accuracy and model path in a table
        table = self.Table(title="Training Summary")
        columns = ["Key", "Value"]
        
        for column in columns:
            table.add_column(column)

        rows = [
            ["accuracy", accuracy],
            ["model_path", self.model_path],
            ["n_estimators", classifier.n_estimators],
            ["random_state", classifier.random_state],
        ]
        
        for row in rows:
            table.add_row(*map(str, row))
        
        self.console.print(table)

    def predict(self, task):
        task = self.taskreprocessor.preprocess_task(task)

        # 獲取嵌入向量
        embedding = self.get_embeddings([task])[0]

        # 使用模型進行預測
        category_encoded = self.classifier.predict([embedding])[0]

        # 獲取預測分數
        prediction_score = self.classifier.predict_proba([embedding])[0][category_encoded]

        # 如果預測分數低於閾值，顯示警告消息    
        if prediction_score < 0.5:
            return -1

        # 轉換編碼為類別標籤
        category = self.label_encoder.inverse_transform([category_encoded])[0]

        return category, prediction_score

# Example usage:
if __name__ == "__main__":
    # Load your tokenizer and model here
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    model = BertModel.from_pretrained('bert-base-chinese')
    
    # Assuming you have your combined data
    combined_data = {
        'task': ["task1", "task2", "task3"],
        'category': ["cat1", "cat2", "cat1"]
    }
    
    # Dummy console, Panel, and Table for example purposes
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    
    console = Console()
    
    # Assuming you've trained your model and saved it to "your_model.pkl"
    model_path = "your_model.pkl"
    env = {'threshold': 0.5}
    model_trainer = BaseModel('data.json', model_path, 'bert-base-chinese', env=env, console=console, Panel=Panel, Table=Table)
    
    # Train the model
    model_trainer.train()
    
    # Task to predict
    task_to_predict = "人工智慧題目"
    
    # Perform prediction
    predicted_category, prediction_score = model_trainer.predict(task_to_predict)
    print("Task ->", task_to_predict)
    print("Predicted Category ->", predicted_category)
    print("Prediction Score ->", prediction_score)
