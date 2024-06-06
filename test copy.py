import torch
from transformers import BertModel, BertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 載入預訓練的BERT模型和分詞器
model_name = 'bert-base-chinese'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# 示例数据
# Existing data
chinese_data = {
    "task": ["寫數學作業", "閱讀英文書籍", "寫國文作文", "學習程式設計", "做數學練習", "閱讀國文文章"],
    "category": ["數學", "英文", "國文", "程式", "數學", "國文"]
}

# Additional Chinese data
additional_chinese_data = {
    "task": ["計算面積", "解方程式", "閱讀詩詞", "寫作文", "練習字帖", "背誦古文"],
    "category": ["數學", "數學", "國文", "國文", "國文", "國文"]
}

# Additional English data
additional_english_data = {
    "task": ["Do math homework", "Read English books", "Write an essay", "Learn programming", "Do math exercises", "Read Chinese articles"],
    "category": ["Math", "English", "Chinese", "Programming", "Math", "Chinese"]
}

# Combine all data
combined_data = {
    "task": chinese_data["task"] + additional_chinese_data["task"] + additional_english_data["task"],
    "category": chinese_data["category"] + additional_chinese_data["category"] + additional_english_data["category"]
}

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

# tasks = combined_data['task']
# categories = combined_data['category_encoded']
# embeddings = get_embeddings(tasks)

# # 分割数据集
# X_train, X_test, y_train, y_test = train_test_split(embeddings, categories, test_size=0.2, random_state=42)

# # 训练分类器
# classifier = LogisticRegression()
# classifier.fit(X_train, y_train)

# # 预测并评估
# y_pred = classifier.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')

# # 保存模型
# torch.save(classifier, 'classifier.pt')

# 加载模型
def load_saved_model():
    classifier = torch.load('classifier.pt')
    return classifier

# 测试新任务
def classify_task(task):
    embedding = get_embeddings([task])[0]
    category_encoded = load_saved_model().predict([embedding])[0]
    category = label_encoder.inverse_transform([category_encoded])[0]
    return category

new_task = "寫數學作業"
predicted_category = classify_task(new_task)
print(f'Task: {new_task}, Predicted Category: {predicted_category}')
