import re
import jieba.posseg as pseg

__all__ = ['preprocess_task']

vocabulary = ['程式', '數字概論', '作業', '課程', '計算機']

def preprocess_task(task):
    # 預處理
    task = remove_keywords(task, ['作業', '課程', '寫', '回', '次'])
    task = remove_numbers(task)
    task = task.strip()
    
    # 過濾打錯字
    task = filter_typo(task)
    
    # 分詞並刪除動詞
    cleaned_task = remove_verbs(task)
    
    return cleaned_task

def remove_keywords(text, keywords):
    # 刪除指定的關鍵字
    for keyword in keywords:
        text = text.replace(keyword, "")
    return text

def remove_numbers(text):
    # 刪除數字
    return re.sub(r'\d+', '', text)

def filter_typo(task):
    # 過濾打錯字
    return ''.join(word for word in task if word in vocabulary or word not in vocabulary)

def remove_verbs(task):
    # 使用jieba分詞，標註詞性，並刪除動詞
    words = pseg.cut(task)
    return ''.join(word for word, flag in words if flag[0] != 'v')

