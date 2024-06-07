import json
import os

def main():
    # 確保程式從當前腳本所在目錄執行
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'json', 'new_course.json')
    output_path = os.path.join(script_dir, 'json', 'test.json')

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = {"task": [], "category": []}
    category_map = {
        "數學": "數學",
        "程式": "程式",
        "英文": "英文",
        "通識課": "通識課",
        "國文": "國文"
    }

    for category, courses in data.items():
        for course in courses:
            result["task"].append(course)
            result["category"].append(category_map.get(category, "其他"))

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
