import multiprocessing
import subprocess
import socket
import time
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from rich import pretty
from rich import print
from rich.console import Console

from src.window import ProcessMonitorWindow

# rich
pretty.install()
console = Console()

# 找到一个空闲端口
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))  # 绑定到一个空闲端口
        port = s.getsockname()[1]  # 获取分配的端口号
    return port

def is_port_open(host, port, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((host, port)) == 0:
                    return True
        except Exception:
            pass
        time.sleep(1)  # 等待一秒再检查
    return False


# 启动 Next.js 服务
def start_nextjs_server(port):
    project_directory = "todolist-web"

    env = os.environ.copy()
    env["PORT"] = str(port)  # 设置环境变量 PORT

    # # 显示要清除 Next.js 缓存
    # console.log("[bold yellow]正在清除 Next.js 缓存...[/bold yellow]")

    # # 清除 Next.js 缓存
    # subprocess.run(["npm", "run", "clean"], cwd=project_directory, check=True)

    # 显示启动 Next.js 服务器
    console.log(f"[bold green]正在启动 Next.js 服务器，端口：{port}...[/bold green]")

    # 启动 Next.js 服务器
    subprocess.Popen(
        ["npm", "run", "dev"], cwd=project_directory, env=env
    )


# 启动 PyQt 应用程序
def start_pyqt_app(port, nextjs_pid):
    app = QtWidgets.QApplication(sys.argv)

    form = QtWidgets.QWidget()
    form.setWindowTitle("TODOLIST")
    form.resize(800, 600)

    web_view = QtWebEngineWidgets.QWebEngineView(form)
    web_view.move(0, 0)
    web_view.resize(800, 600)

    # 加载指定端口的 Next.js 服务
    web_view.load(QtCore.QUrl(f"http://localhost:{port}"))
    
    form.show()
    
    def terminate_nextjs():
        console.log("PyQt 应用程序即将退出，终止 Next.js 进程")
        # try:
        #     os.kill(nextjs_pid, signal.SIGTERM)  
        # except OSError:
        #     console.log("Next.js 进程可能已关闭")

    app.aboutToQuit.connect(terminate_nextjs)  



    sys.exit(app.exec_())  # 运行 PyQt 应用程序
    
def run_window_ser(pyqt_pid, nextjs_port):
    console.log(f"[bold green]啟動監控效能process")
    


    app = QtWidgets.QApplication(sys.argv)


    # 创建并显示窗口
    monitor_window = ProcessMonitorWindow(nextjs_port, pyqt_pid)
    monitor_window.show()

    sys.exit(app.exec_())

# 主程序
def main(*args, **kwargs):
    # 找到一个空闲端口
    port = find_free_port()

    # 创建两个进程
    nextjs_process = multiprocessing.Process(
        target=start_nextjs_server, args=(port,)
    )

   
    # 启动 Next.js 服务器
    nextjs_process.start()
    
    
    pyqt_process = multiprocessing.Process(
        target=start_pyqt_app, args=(port, nextjs_process.pid,)
    )
    
    if not is_port_open("localhost", port):
        print("Next.js 服务器未在超时时间内启动")
        sys.exit(1)  # 退出程序

    # 启动 PyQt 应用程序
    pyqt_process.start()


    window_process =  multiprocessing.Process(
        target=run_window_ser, args=(pyqt_process.pid, port,)
    )
    
    window_process.start()
    window_process.join()
    
    # 等待两个进程完成
    nextjs_process.join()
    pyqt_process.join()
    
    
if __name__ == '__main__': 
    main()