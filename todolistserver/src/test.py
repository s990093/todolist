import click
from Bertchinese import Model 


@click.command()
@click.option('--task', default='寫程式', help='任務名稱')
@click.option('--train', is_flag=True, help='執行訓練任務')
def main(task, train):
    m = Model("data.json", "classifier.pt")
    if train:
        m.train_data(solver="lbfgs", max_iter=3000)
    else:
        m.test(task)

if __name__ == '__main__':
    main()