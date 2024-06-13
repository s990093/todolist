from App import env
from src.Bertchinese.predictionModel import PredictionModel


if __name__ == "__main__":
    # Assuming you've trained your model and saved it to "your_model.pkl"
  
    model = PredictionModel(json_file_path="data.json", model_path="classifier.pkl", env=env)

    
    # Task to predict
    task_to_predict = "Your task goes here"
    
    # Perform prediction
    predicted_category = model.predict_v2(task_to_predict)
    print("Predicted category:", predicted_category)