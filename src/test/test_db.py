import os
import unittest

from ..base.error import WindowError

from ..db import DB


# 單元測試類，繼承自 unittest.TestCase
class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB("testdb.sqlite3")
        self.db.creat_table()
    
        
    def tearDown(self):
        if os.path.exists("testdb.sqlite3"):
            os.remove("testdb.sqlite3")
            
            
    def test_insert_repect_tasks_repeat_name(self):
        self.db.insert_repect_tasks("test") 
        with self.assertRaises(WindowError):
            self.db.insert_repect_tasks("test")  

