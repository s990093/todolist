import json
from sklearn.preprocessing import LabelEncoder

# 示例数据
chinese_data = {
    "task": ["寫數學作業", "閱讀英文書籍", "寫國文作文", "學習程式設計", "做數學練習", "閱讀國文文章"],
    "category": ["數學", "英文", "國文", "程式", "數學", "國文"]
}

additional_chinese_data = {
    "task": ["計算面積", "解方程式", "閱讀詩詞", "寫作文", "練習字帖", "背誦古文"],
    "category": ["數學", "數學", "國文", "國文", "國文", "國文"]
}

additional_english_data = {
    "task": ["Do math homework", "Read English books", "Write an essay", "Learn programming", "Do math exercises", "Read Chinese articles"],
    "category": ["Math", "English", "Chinese", "Programming", "Math", "Chinese"]
}

combined_data = {
    "task": chinese_data["task"] + additional_chinese_data["task"] + additional_english_data["task"],
    "category": chinese_data["category"] + additional_chinese_data["category"] + additional_english_data["category"]
}

# 标签编码



def load_chinese_data():
        # 将数据写入 JSON 文件
    with open('task_data.json', 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)



def change_data_to_ai_data():
    with open('course.json', 'r', encoding='utf-8') as f:
        course_data = json.load(f)

    # 初始化新的結構
    new_format = {
        "task": [],
        "category": []
        }

    # 遍歷每個學期，添加必修課程
    for semester, courses in course_data["semester"].items():
        for course in courses:
            new_format["task"].append(course["課程名稱"])
            new_format["category"].append("資工核心課程")

    # 遍歷專業選修課程
    for course in course_data["專業選修"]:
        new_format["task"].append(course["課程名稱"])
        new_format["category"].append("資工核心課程")

    # 遍歷通識課程
    for course in course_data["通識課程"]:
        new_format["task"].append(course["課程名稱"])
        new_format["category"].append("通識課程")

    # 輸出新格式的資料
    with open('new_course.json', 'w', encoding='utf-8') as f:
        json.dump(new_format, f, ensure_ascii=False, indent=4)

    print("轉換完成，結果已保存到 new_course.json")

if __name__ == '__main__':
    # change_data_to_ai_data()
    with open('new_course.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = {"task": [], "category": []}

    for category, courses in data.items():
        for course in courses:
            result["task"].append(course)
            
            if category == "數學":
                print(  result["task"])
                result["category"].append("數學")
            elif category == "程式":
                result["category"].append("程式")
            elif category == "通識":
                result["category"].append("通識")

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
