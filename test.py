from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets, QtGui
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    # 设置应用程序图标
    app_icon = QtGui.QIcon("/Users/hungwei/Desktop/proj/todolist/icon.ico")  # 替换成你的图标文件路径
    app.setWindowIcon(app_icon)

    Form = QtWidgets.QWidget()
    Form.setWindowTitle('todolist')
    Form.resize(800, 600)

    webView = QtWebEngineWidgets.QWebEngineView(Form)
    webView.move(0, 0)
    webView.resize(800, 600)

    # 这里更改 URL 以连接到本地服务器的 3000 端口
    webView.load(QtCore.QUrl("http://localhost:3000"))


    Form.show()
    sys.exit(app.exec_())
