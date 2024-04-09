import sys
import os
import unittest

# # Get the current directory of the script
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # # Get the parent directory (one level up) and append it to sys.path
# parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
# sys.path.append(parent_dir)

# Now you can perform your imports
from env import ENV
from src.gui import TodoListGUI

# test unit
from src.test.test_db import TestDB
from src.test.test_gui import TestGUI

DEBUG = True


if __name__ == '__main__':
   unittest.main()