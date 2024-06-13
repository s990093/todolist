import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

from App.models import Task

class Command(BaseCommand):
    help = 'Upload 100 tasks to the database'

    def handle(self, *args, **kwargs):
        tasks = []
        subjects = [
            "微積分", "離散數學", "線性代數", "工程數學", "數值分析", "數學邏輯導論", 
            "數據分析", "數位信號處理", "資訊理論", "編碼理論", "數位邏輯設計", 
            "程式設計(一)", "計算機概論", "物件導向程式設計", "計算機程式設計實習", 
            "演算法", "資料結構", "作業系統", "計算機網路", "程式設計(二)", 
            "實務專題(一)", "物件導向程式設計實習", "嵌入式系統", "數位影像處理", 
            "機器學習", "人工智慧", "網際網路協定", "高速網路", "生物資訊資料庫", 
            "多媒體程式設計", "資料壓縮", "影像壓縮", "互動式網頁程式設計", 
            "資料結構實務", "電腦圖學概論", "語音壓縮", "資訊工程概論", 
            "系統程式", "硬體描述語言設計", "電腦遊戲設計", "數位電子學", 
            "通訊系統概論", "虛擬實境", "組合語言程式設計", "網路程式設計實務", 
            "資訊安全", "視窗程式設計", "網路資料庫程式設計", "分散式系統", 
            "生物資訊概論", "多媒體資料庫", "無線網路", "程式語言", 
            "計算分子生物學", "資料探勘", "IoT系統實務整合應用", "三維電腦圖學", 
            "Linux系統實務整合應用", "語音信號處理", "網路安全", "動畫程式設計實務", 
            "行動計算", "平行處理", "Linux系統", "多媒體網路通訊", "人工智慧", 
            "數位視訊處理", "編譯器", "電腦視覺", "嵌入式系統程式設計實務", 
            "語音辨認", "軟體工程", "APP程式設計(一)", "通識課程"
        ]
        priorities = ['low', 'medium', 'high']
        types = ['數學', '英文', '程式', "程式", '程式']
        tags = ['homework', 'exam', 'lab']

        for i in range(100):
            text = random.choice(subjects)
            completed = random.choice([True, False])
            time = random.choice(['1 hour', '2 hours', '3 hours'])
            desc = f'This is the description for {text}'
            priority = random.choice(priorities)
            deadline = datetime.now() + timedelta(days=random.randint(1, 30))
            task_type = random.choice(types)
            task_tags = ', '.join(random.sample(tags, random.randint(1, 3)))

            task = Task(
                text=text,
                completed=completed,
                time=time,
                desc=desc,
                priority=priority,
                deadline=deadline,
                type=task_type,
                tags=task_tags
            )
            tasks.append(task)

        Task.objects.bulk_create(tasks)
        self.stdout.write(self.style.SUCCESS('Successfully uploaded 100 tasks'))
