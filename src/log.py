class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Log:
    def __init__(self):
        self.head = None

    def add_entry(self, entry):
        new_node = Node(entry)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_log(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# # 示例用法
# log = Log()

# log.add_entry("2024-03-21: 用户登录")
# log.add_entry("2024-03-21: 创建新任务")
# log.add_entry("2024-03-22: 完成项目报告")
# log.add_entry("2024-03-23: 修改并完成项目报告")

# print("=== 日志内容 ===")
# log.display_log()
