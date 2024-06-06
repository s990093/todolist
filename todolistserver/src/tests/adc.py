import json
import torch
from transformers import BertModel, BertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_FILE = "new_course.json"  # Use constant for clarity

# 載入預訓練的BERT模型和分詞器
model_name = 'bert-base-chinese'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


def load_data(data_file):
    """Loads training data from the specified JSON file.

    Args:
        data_file (str): Path to the JSON file containing tasks and categories.

    Returns:
        dict: Dictionary containing processed data:
            - task_texts: List of text entries
            - category_labels: List of category labels (encoded)
    """

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    label_encoder = LabelEncoder()
    data['category_encoded'] = label_encoder.fit_transform(data['category'])
    return {
        'task_texts': data['task'],
        'category_labels': data['category_encoded'],
    }


def get_embeddings(data):
    # Implementation for getting BERT embeddings (already defined)
    pass


def save_model(classifier, filename):
    """Saves the trained classifier model to the specified file.

    Args:
        classifier (object): Trained classifier model
        filename (str): Path to save the model file
    """

    torch.save(classifier, filename)


def load_saved_model(filename):
    """Loads a saved classifier model from the specified file.

    Args:
        filename (str): Path to the saved model file

    Returns:
        object: Loaded classifier model
    """

    return torch.load(filename)


def train(data_file):
    """Trains a logistic regression classifier on the provided data.

    Args:
        data_file (str): Path to the JSON file containing labeled tasks and categories.
    """

    training_data = load_data(data_file)
    embeddings = get_embeddings(training_data['task_texts'])

    # Split data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(embeddings, training_data['category_labels'], test_size=0.2, random_state=42)

    # Train the classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # Evaluate and save the model
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    save_model(classifier, 'classifier.pt')


def predict(new_task):
    """Classifies a new task using the trained model.

    Args:
        new_task (str): The task text to be classified.

    Returns:
        str: Predicted category for the new task.
    """

    # Load the saved model
    classifier = load_saved_model('classifier.pt')

    # Get embedding for the new task
    embedding = get_embeddings([new_task])[0]

    # Predict category
    category_encoded = classifier.predict([embedding])[0]
    category = label_encoder.inverse_transform([category_encoded])[0]
    
