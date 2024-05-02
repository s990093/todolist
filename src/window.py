import os
import sys
import psutil
from PyQt5 import QtWidgets, QtCore

from PyQt5 import QtWidgets, QtCore, QtGui
import psutil
import datetime

class ProcessMonitorWindow(QtWidgets.QWidget):
    def __init__(self, nextjs_port=None, pyqt_pid=None):
        super().__init__()

        self.nextjs_port = nextjs_port
        self.pyqt_pid = pyqt_pid

        self.setWindowTitle("Process Monitor")
        self.resize(600, 300)

        # 创建主要布局为 QVBoxLayout
        main_layout = QtWidgets.QVBoxLayout()

        # 创建标题
        title = QtWidgets.QLabel("Process Monitor")
        title.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(title)

        # 创建水平布局来包含左右分布的内容
        horizontal_layout = QtWidgets.QHBoxLayout()

        # Next.js 信息部分
        nextjs_group = QtWidgets.QGroupBox("Next.js Process Info")
        nextjs_layout = QtWidgets.QVBoxLayout()
        self.nextjs_info = QtWidgets.QTextEdit()
        self.nextjs_info.setReadOnly(True)
        nextjs_layout.addWidget(self.nextjs_info)
        nextjs_group.setLayout(nextjs_layout)

        # PyQt 信息部分
        pyqt_group = QtWidgets.QGroupBox("PyQt Process Info")
        pyqt_layout = QtWidgets.QVBoxLayout()
        self.pyqt_info = QtWidgets.QTextEdit()
        self.pyqt_info.setReadOnly(True)
        pyqt_layout.addWidget(self.pyqt_info)
        pyqt_group.setLayout(pyqt_layout)

        # 将 Next.js 和 PyQt 信息部分添加到水平布局
        horizontal_layout.addWidget(nextjs_group)
        horizontal_layout.addWidget(pyqt_group)

        # 将水平布局添加到主布局
        main_layout.addLayout(horizontal_layout)

        # 设置窗口的主布局
        self.setLayout(main_layout)

        # 创建定时器，定期刷新进程信息
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_process_info)
        self.timer.start(1000) 

    # 更新进程信息
    def update_process_info(self):
        # 检查 Next.js 端口并更新相关信息
        if self.nextjs_port:
            # 尝试找到占用该端口的进程
            process = self.find_process_by_port(self.nextjs_port)
            if process:
                # 使用现有的更新函数来更新信息
                self.update_process(process.pid, self.nextjs_info)
            else:
                self.nextjs_info.setText("No process found on specified port.")

        # 检查 PyQt 进程 ID 并更新相关信息
        if self.pyqt_pid:
            self.update_process(self.pyqt_pid, self.pyqt_info)
        
    # 更新单个进程的信息
    def update_process(self, pid, info_widget):
        if pid is None:
            info_widget.setText("Invalid process ID.")
            return

        try:
            process = psutil.Process(pid)

            # 获取进程信息
            process_name = process.name()
            process_status = process.status()
            cpu_usage = process.cpu_percent(interval=0.1)
            memory_usage = process.memory_info().rss / (1024 * 1024)
            thread_count = process.num_threads()
            start_time = datetime.datetime.fromtimestamp(
                process.create_time()
            ).strftime("%Y-%m-%d %H:%M:%S")

            # 构建信息文本
            info_text = (
                f"Process Name: {process_name}\n"
                f"Status: {process_status}\n"
                f"CPU Usage: {cpu_usage:.2f}%\n"
                f"Memory Usage: {memory_usage:.2f} MB\n"
                f"Thread Count: {thread_count}\n"
                f"Start Time: {start_time}\n"
            )
            info_widget.setText(info_text)

        except psutil.NoSuchProcess:
            info_widget.setText("Process not found.")

        except psutil.AccessDenied:
            info_widget.setText("Access to process information denied.")

        except Exception as e:
            info_widget.setText(f"Error fetching process info: {str(e)}")
            
            
    def find_process_by_port(self, port):
        for proc in psutil.process_iter(['connections']):
            try:
                # 获取进程的所有网络连接
                connections = proc.connections(kind='inet')
                for conn in connections:
                    # 如果本地地址的端口号与目标端口匹配
                    if conn.laddr.port == port:
                        return proc  # 返回找到的进程
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # 跳过无法访问或不存在的进程
                continue

        return None  # 如果没有找到进程，则返回 None