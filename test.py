from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
import sys


if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)

   Form = QtWidgets.QWidget()
   Form.setWindowTitle('Local Web View')
   Form.resize(800, 600)

   webView = QtWebEngineWidgets.QWebEngineView(Form) 
   webView.move(0, 0)
   webView.resize(800, 600)

   # 这里更改 URL 以连接到本地服务器的 3000 端口
   webView.load(QtCore.QUrl("http://localhost:3000"))  

   Form.show()
   sys.exit(app.exec_())
