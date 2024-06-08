import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch
from tqdm import tqdm

from Bertchinese.baseModel import BaseModel

__all__ = ['TrainingModel']


class TrainingModel(BaseModel):
    def __init__(self,
                 json_file_path: str,
                 model_path: str, 
                 environment: dict,
                 model_name: str = 'bert-base-chinese', 
                 *args, **kwargs):
        super(TrainingModel, self).__init__(json_file_path, model_path, model_name, *args, **kwargs)
        
        self._environment = environment


    def process_data(self):
        tasks = self.combined_data['task']
        categories = self.combined_data['category_encoded']
        embeddings = self.get_embeddings(tasks)

        # Combine data and labels
        data_with_labels = list(zip(embeddings, categories))

        # Shuffle data
        np.random.shuffle(data_with_labels)

        # Separate data and labels
        shuffled_embeddings, shuffled_categories = zip(*data_with_labels)
    

        return np.array(shuffled_embeddings), np.array(shuffled_categories)

    def train(self):
        """Entry point for training the model.

        Args:
            solver (str): The solver to use in Logistic Regression.
            max_iter (int, optional): Maximum number of iterations. Defaults to 1000.
        """
        embeddings, categories = self.process_data()

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42)

        # Train the classifier
        classifier = LogisticRegression(solver= self._environment.get('solver','lbfgs'),
                                        max_iter= self._environment.get('max_iter', 1000))
        
        classifier.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Save the model
        torch.save(classifier, self.model_path)

        # Display progress bar and model accuracy
        with tqdm(total=100, desc="Training Progress") as pbar:
            pbar.update(100)

        accuracy_panel = self.Panel.fit(f'Accuracy: {accuracy:.2f}', title="Accuracy", border_style="blue")
        self.console.print(accuracy_panel)



    