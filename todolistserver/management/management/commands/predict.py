import click

from src.Bertchinese.trainModel import TrainingModel as Model

import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from src.Bertchinese.predictionModel import PredictionModel
from App.env import env



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
            
        model = PredictionModel(json_file_path="data.json", model_path="classifier.pt", env=env)
        

        
        # Task to predict
        task_to_predict = "數學作業"
        
        # Perform prediction
        predicted_category = model.predict(task_to_predict)
