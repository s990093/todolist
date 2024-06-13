import collections
import time
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score
import torch
from tqdm import tqdm
from imblearn.over_sampling import RandomOverSampler


from src.Bertchinese.baseModel import BaseModel

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
        # embeddings, categories = self.process_data()
        tasks = self.combined_data['task']
        categories = self.combined_data['category_encoded']
        embeddings = self.get_embeddings(tasks)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42,shuffle=True)

        # Train the classifier
        classifier = LogisticRegression(solver = self._environment.get('solver','lbfgs'),
                                        max_iter = self._environment.get('max_iter', 1000))
        
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
        
        
    def train_v3(self):
        tasks = self.combined_data['task']
        categories = self.combined_data['category_encoded']
        embeddings = self.get_embeddings(tasks)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42, shuffle=True)

        # Train the classifier
        classifier = LogisticRegression(solver=self._environment.get('solver', 'lbfgs'),
                                        max_iter=self._environment.get('max_iter', 1000))
        classifier.fit(X_train, y_train)

        # Predict
        y_pred = classifier.predict(X_test)

        # Evaluate
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        # Save the model
        joblib.dump(classifier, self.model_path)

            
        # Create a table to display metrics
        table = self.Table(title="Model Evaluation Metrics", title_style="bold magenta")
        table.add_column("Metric", style="cyan")
        table.add_column("Score", style="cyan")
        
        
        table.add_row("classifier", f"{classifier.__str__()}")
        table.add_row("solver", f"{self._environment.get('solver', 'lbfgs')}")
        table.add_row("max_iter", f"{self._environment.get('max_iter', 1000)}")

        table.add_row("Accuracy", f"{accuracy:.2f}")
        table.add_row("Precision", f"{precision:.2f}")
        table.add_row("Recall", f"{recall:.2f}")
        table.add_row("F1-score", f"{f1:.2f}")
        
        
        self.console.print(table)



        # Display model information

    def train_2(self):
        start_time = time.time()

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
        

        # Save the model
        joblib.dump(classifier, self.model_path)

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
        

        training_time = end_time - start_time
        rows = [
            ["accuracy", accuracy],
            ["model_path", self.model_path],
            ["total_training_time", training_time],
            ["n_estimators", classifier.n_estimators],
            ["random_state", classifier.random_state],
            ["param_grid", {}],
        ]


        for row in rows:
            table.add_row(*map(str, row))

        self.console.print(table)