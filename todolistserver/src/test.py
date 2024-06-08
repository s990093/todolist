import click

from Bertchinese.predictionModel import PredictionModel as Model

# @click.command()
# @click.option('--task', default='寫程式', help='任務名稱')
# @click.option('--train', is_flag=True, help='執行訓練任務')
# def main(task, train):
#     env = {
#         "solver": "lbfgs",
#         "max_iter": 3000
#     }
#     m = TrainingModel("data.json", "classifier.pt",env)
#     if train:
#         m.train_data()
   

if __name__ == '__main__':    
    m = Model("data.json", "classifier.pt")
    m.test("中文作業")