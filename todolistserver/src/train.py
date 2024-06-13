import click

from Bertchinese.trainModel import TrainingModel as Model


if __name__ == '__main__':
    
    env = {
        "solver": "lbfgs",
        "max_iter": 3000
    }
    
    m = Model("data.json", "classifier.pt", env)
    m.train()
    
    