import re
import jieba.posseg as pseg

class TaskPreprocessor:
    def __init__(self):
        self.vocabulary = ['程式', '數字概論', '作業', '課程', '計算機']
        self.words = pseg.cut("初始化加载分词模型")

    def preprocess_task(self, task):
        task = self.remove_keywords(task, ['作業', '課程', '寫', '回', '次'])
        task = self.remove_numbers(task)
        task = task.strip()
        task = self.filter_typo(task)
        cleaned_task = self.remove_verbs(task)
        return cleaned_task

    def remove_keywords(self, text, keywords):
        for keyword in keywords:
            text = text.replace(keyword, "")
        return text

    def remove_numbers(self, text):
        return re.sub(r'\d+', '', text)

    def filter_typo(self, task):
        return ''.join(word for word in task if word in self.vocabulary or word not in self.vocabulary)

    def remove_verbs(self, task):
        return ''.join(word for word, flag in self.words if flag[0] != 'v')
