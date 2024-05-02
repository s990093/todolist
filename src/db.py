import os
import sqlite3
from datetime import datetime

from .base.error import WindowError

class DB():
    def __init__(self, db_name: str = "db.sqlite3"):
        # self.conf = conf
        self.db_name = db_name
        self.conn = sqlite3.connect(database=self.db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.conn.cursor()
        
        self.today = datetime.today().date()  
        
        
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
            self.cursor.execute("SELECT * FROM Task WHERE DATE(timestamp) = ?", (self.today,))
            return self.cursor.fetchall()
    
    def get_repeat_names(self):
        sql = '''SELECT name FROM REPECT_Task'''
        self.cursor.execute(sql)
        rows =  self.cursor.fetchall()
        
        return [rows[0] for rows in rows]
    
    def get_today_repeat_task(self):
        sql = '''SELECT name FROM Task WHERE type = 0 AND DATE(timestamp) = ?'''
        self.cursor.execute(sql, (self.today,))
        return [row[0] for row in self.cursor.fetchall()]

    def check_and_insert_repeat_tasks(self) -> list:
        "把每日任務增加到當天任務裡面"
        names = self.get_repeat_names()
        repeat_tasks = self.get_today_repeat_task()
        data = []
        for name in names:
            for repeat_task in repeat_tasks:
                if name == repeat_task: 
                    data.append(name)
        return data

        
    def insert_task(self, name, level,task_type, time=0.0, des=None, click=False, ) -> list:
        # 定義 SQL 語句
        sql = '''INSERT INTO Task (name, level, time, des, click, type, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)'''

        # 定義參數值
        values = (name, level, time, des, click, task_type, self.__get_now_time())

        # 執行 SQL 語句並提交更改
        self.cursor.execute(sql, values)
        self.conn.commit()

        # 返回插入的任務資料
        return [-1, name, level, time, des, click, task_type, self.__get_now_time()]
    
    
    def insert_repect_tasks(self, task_name: str) -> bool:
        # 检查任务名是否已存在
        check_sql = "SELECT COUNT(*) FROM REPECT_Task WHERE name = ?"
        check_values = (task_name,)
        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()

        # 如果任务名已存在，则返回 False
        if result[0] > 0:
            raise WindowError(200)
        
        # 如果任务名不存在，则插入新任务
        insert_sql = "INSERT INTO REPECT_Task (name, timestamp) VALUES (?, ?)"
        insert_values = (task_name, self.__get_now_time())
        self.cursor.execute(insert_sql, insert_values)
        self.conn.commit()
        return True

    
    
    def close(self):
        self.conn.close()
        
        
        
    def __get_now_time(self):
        # 獲取當前時間
        return datetime.now()


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