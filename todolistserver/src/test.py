import click

# from Bertchinese.predictionModel import PredictionModel as Model

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
   

# if __name__ == '__main__':    
#     m = Model("data.json", "classifier.pt")
#     m.test("中文作業")



import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel

# 加載BERT模型和tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 定義函數來生成嵌入
def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

# 定義類別並生成嵌入
category_map = {
    "數學": "數學",
    "程式": "程式",
    "英文": "英文",
    "通識課": "通識課",
    "國文": "國文"
}
category_embeddings = {category: get_embedding(text) for category, text in category_map.items()}

# 輸入文本並生成嵌入
input_text = "寫英文雜誌"
input_embedding = get_embedding(input_text)

# 計算相似度並分類
similarities = {category: cosine_similarity(input_embedding, embedding)[0][0] for category, embedding in category_embeddings.items()}
classified_category = max(similarities, key=similarities.get)

print(f"輸入文本 '{input_text}' 被分類為 '{classified_category}'")
