import unittest

from ..gui import TodoListGUI


class TestGUI(unittest.TestCase):
    def setUp(self) -> None:
        self.gui = TodoListGUI()
        
    def tearDown(self) -> None:
        self.gui.close()
        
    def test_run_gui(self):
        self.gui.command("gui:run --sound = False")
        
    def test_close_gui(self):
        self.gui.run()
        self.gui.close()
    
    def test_restart_gui(self):
        self.gui.run()
        self.gui.restart()
