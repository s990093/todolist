import sqlite3


class DB():
    def __init__(self, conf: dict):
        self.conf = conf
        
        self.conn = sqlite3.connect(conf.get('db_connection'))
        self.cursor = self.conn.cursor()
        
        
    def creat_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
        
        
    def get_all_task(self):
        self.cursor.execute("SELECT * FROM tasks")
        self.conn.commit()
        return self.cursor.fetchall()


