import click

from src.Bertchinese.trainModel import TrainingModel as Model

import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Upload 100 tasks to the database'

    def handle(self, *args, **kwargs):
        
        env = {
            "solver": "lbfgs",
            "max_iter": 3000,
            "random_file": True,
        }
        
        m = Model("data.json", "classifier.pt", env)
        m.train_v3()
        
        