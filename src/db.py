import os
import sqlite3
from datetime import datetime

class DB():
    def __init__(self):
        # self.conf = conf
        
        self.conn = sqlite3.connect("db.sqlite3", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.conn.cursor()
        
        
    def creat_table(self):
        sql_commands = None
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        if not tables:
            with open('./src/table.sql', 'r') as file:
                sql_commands = file.read()
            self.cursor.executescript(sql_commands)
            self.conn.commit()
            
    def get_today_tasks(self) -> list:
            today = datetime.today().date()  
            self.cursor.execute("SELECT * FROM Task WHERE DATE(timestamp) = ?", (today,))
            return self.cursor.fetchall()
            
 

    def insert_task(self, name, level, time=0.0, des=None, click=False, task_type = 0):
        # 獲取當前時間
        timestamp = datetime.now()

        # 定義 SQL 語句
        sql = '''INSERT INTO Task (name, level, time, des, click, type, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)'''

        # 定義參數值
        values = (name, level, time, des, click, task_type, timestamp)

        # 執行 SQL 語句並提交更改
        self.cursor.execute(sql, values)
        self.conn.commit()

        # 返回插入的任務資料
        return [-1, name, level, time, des, click, task_type, timestamp]
    
    
    def close(self):
        self.conn.close()


    def serialize_task(self, row: list) -> dict:
        """
        將資料庫中的任務序列化為字典格式的列表。

        Args:
            rows: 從資料庫中檢索到的任務列表。

        Returns:
            包含每個任務的字典格式的列表。
        """

        # 遍歷 rows 中的每個任務
   
        # 創建任務字典
        task = {
            "name": row[1],
            "level": row[2],
            "completed": row[5],
            "type": row[6]
        }
        
        # 將任務字典添加到 tasks 列表中
         

        # 回傳序列化後的 tasks 列表
        return task