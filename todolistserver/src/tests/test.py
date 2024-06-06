import json
import re
from preprocess import preprocess_task
import torch
from transformers import BertModel, BertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import click

FILE = "json/data.json"
# 載入預訓練的BERT模型和分詞器
model_name = 'bert-base-chinese'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

with open(f"./{FILE}", 'r', encoding='utf-8') as f:
    combined_data = json.load(f)

# 标签编码
label_encoder = LabelEncoder()
combined_data['category_encoded'] = label_encoder.fit_transform(combined_data['category'])

# 获取BERT嵌入
def get_embeddings(text_list):
    embeddings = []
    for text in text_list:
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=32)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().numpy())
    return embeddings


# 保存模型

# 加载模型
def load_saved_model():
    classifier = torch.load('classifier.pt')
    return classifier

# 测试新任务


def classify_task(task, threshold=0.5):
    # 預處理任務
    task = preprocess_task(task)

    # 獲取嵌入向量
    embedding = get_embeddings([task])[0]

    # 使用模型進行預測
    category_encoded = load_saved_model().predict([embedding])[0]

    # 獲取預測分數
    prediction_score = load_saved_model().predict_proba([embedding])[0][category_encoded]
    

    # 如果預測分數低於閾值，顯示警告消息    
    if prediction_score < threshold:
        return -1

    # 轉換編碼為類別標籤
    category = label_encoder.inverse_transform([category_encoded])[0]

    # 返回類別標籤
    return category




def train_data():
    tasks = combined_data['task']
    categories = combined_data['category_encoded']
    embeddings = get_embeddings(tasks)

    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42)

    # 训练分类器
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # 预测并评估
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    torch.save(classifier, 'classifier.pt')

    
def test(new_task):
    predicted_category = classify_task(new_task)
    
    if predicted_category == -1:
        print("其他")
    print(f'Task: {new_task}, Predicted Category: {predicted_category}')


    

@click.command()
@click.option('--task', default='寫程式', help='任務名稱')
@click.option('--train', is_flag=True, help='執行訓練任務')
def main(task, train):
    if train:
        train_data()
    else:
        test(task)

if __name__ == '__main__':
    main()