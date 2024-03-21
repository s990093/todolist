class TreeNode:
    def __init__(self, task, due_date=None):
        self.task = task
        self.due_date = due_date
        self.left = None
        self.right = None

class TodoList:
    def __init__(self):
        self.root = None

    def add_task(self, task, due_date=None):
        new_task = TreeNode(task, due_date)
        if not self.root:
            self.root = new_task
        else:
            self._add_task_recursive(self.root, new_task)

    def _add_task_recursive(self, current_node, new_task):
        if new_task.due_date <= current_node.due_date:
            if current_node.left is None:
                current_node.left = new_task
            else:
                self._add_task_recursive(current_node.left, new_task)
        else:
            if current_node.right is None:
                current_node.right = new_task
            else:
                self._add_task_recursive(current_node.right, new_task)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"Task: {node.task} - Due Date: {node.due_date}")
            self.inorder_traversal(node.right)

# 示例用法
todo = TodoList()

todo.add_task("完成项目报告", "2024-03-25")
todo.add_task("购物", "2024-03-26")
todo.add_task("健身", "2024-03-24")

print("=== 初始任务 ===")
todo.inorder_traversal(todo.root)
