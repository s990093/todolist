import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk
import sqlite3
import chartify
import pandas as pd

# 连接到SQLite数据库
conn = sqlite3.connect('todo_list.db')
c = conn.cursor()

# 创建任务表
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )''')

# 创建主窗口
root = tk.Tk()
root.title("To-Do List")

# 创建任务列表
tasks = []

# 从数据库加载任务函数
def load_tasks():
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    for row in rows:
        tasks.append(row[1])
    update_listbox()

# 添加任务函数
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# 删除任务函数
def delete_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        task_id = selected_task + 1
        tasks.pop(selected_task)
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# 显示时间统计函数
def show_time_statistics():
    c.execute("SELECT strftime('%Y-%m-%d', timestamp) AS date, COUNT(*) AS count FROM tasks GROUP BY date")
    rows = c.fetchall()
    
    # 准备数据
    data = []
    for row in rows:
        data.append({'date': row[0], 'count': row[1]})
    
    # 转换为Pandas DataFrame
    df = pd.DataFrame(data)
    
    # 创建Chartify图表
    chart = chartify.Chart(blank_labels=True, x_axis_type='categorical')
    chart.plot.bar(data_frame=df, x_column='date', y_column='count', color_column=None)
    chart.set_title("Tasks Added Over Time")
    chart.set_subtitle("Number of tasks added per day")
    chart.show()

# 更新任务列表函数
def update_listbox():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, task)

# 创建任务输入框和添加按钮
task_entry = ttk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

add_button = ttk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

# 创建任务列表框架和删除按钮
tasks_listbox = tk.Listbox(root, width=50, height=10, borderwidth=0, highlightthickness=0)
tasks_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

delete_button = ttk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# 创建时间统计按钮
stats_button = ttk.Button(root, text="Time Statistics", width=15, command=show_time_statistics)
stats_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 创建滚动条
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tasks_listbox.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
tasks_listbox.config(yscrollcommand=scrollbar.set)

# 加载任务列表
load_tasks()

# 设置窗口自适应大小
root.columnxconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()
