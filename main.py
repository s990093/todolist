import sys
import os

# # Get the current directory of the script
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # # Get the parent directory (one level up) and append it to sys.path
# parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
# sys.path.append(parent_dir)

# Now you can perform your imports
from src.gui import TodoListGUI
from src.base.gui import GUI
from env import ENV




if __name__ == '__main__':
    # try:
        gui = TodoListGUI()
        gui.run()
    # except Exception as e:
    #     # raise Exception(e)
    #     print(str(e))
    #     sys.exit(0)

