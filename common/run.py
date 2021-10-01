# run.py

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QApplication

from common.database import *
from ui.login_ui.login import Ui_Form

from ui.star_ui.start import Ui_Form as form_ok
from ui.RegisteredAccount_ui.RegisteredAccount import Ui_Form as form_register

import pymysql


class mywindow(QtWidgets.QDialog, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super(mywindow, self).__init__()
        self.x = 0
        self.userflag = -1
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示

        self.login_button.clicked.connect(self.printState)
        self.register_button.clicked.connect(self.RegisteredAccount)

        self.y = self.groupBox.height() - (self.hintmassage.height() / 2)

        # 时间
        self.timer = QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(self.movehintmassage)

        # 提示框不可见
        self.hintmassage.setVisible(False)

    def mouseMoveEvent(self, event):  # 重写移动事件
        self._endPos = event.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def test(self):
        print("test")

    def RegisteredAccount(self):
        self.w2 = window_register()
        self.w2.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.w2.setAutoFillBackground(False)
        self.w2.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示
        # 提示框不可见
        self.w2.hintmassage.setVisible(False)
        self.w2.register_button.clicked.connect(self.confirmRegiser)
        self.w2.login_back_pushbutton.clicked.connect(self.closeRegiser)

        self.w2.show()
        # 前一个窗口设为不可见
        self.setVisible(False)

    def closeRegiser(self):
        self.w2.close()
        self.setVisible(True)

    def movehintmassage(self):
        if self.x > self.height() + (self.hintmassage.width()):
            self.timer.stop()  # 通过stop 进行停止
            self.x = 0  # 重置x的值，使得提示框得以重新滑动
            self.hintmassage.setVisible(False)  # 重新隐藏，因为进入此函数时设置为了显示，此句是让提示框回到最初
        else:
            # 提示框出现
            self.hintmassage.setVisible(True)

            self.x += 5

            self.hintmassage.move(self.x, self.y)
            print("(%s,%s)" % (self.x, self.y))

            # self.hintmassage.move(self.groupBox.width() - (self.hintmassage.width() / 2),
            #                       self.groupBox.height() - -(self.hintmassage.height() / 2))

    def printState(self):
        self.timer.start()
        # 显示状态
        #        if self.lineEdit_username.text == "1" and self.lineEdit_password.text == "1":
        if self.user.text().strip() == "1747105016":
            self.userflag = 0
            if self.password.text() == "123456":
                words = "Login successful!"
                self.w1 = window_ok()
                self.w1.show()
                self.close()
        if self.userflag == -1:
            words = "用户名不存在"
            self.hintmassage.setText(words)
            print("test1")
        else:
            print("test2")
            words = "密码错误"
            self.hintmassage.setText(words)
            print(self.userflag)

        self.userflag = -1  # 没有这一步的话userflag的值一直是0

    # 【读取内容】按钮功能
    def confirmRegiser(self):
        user = self.user.text().strip()
        password = self.password.text().strip()
        queryAccount(user, password)


from Main.mainRun import window_ok
class window_ok(QtWidgets.QWidget, form_ok):
    def __init__(self):
        super(window_ok, self).__init__()
        self.setupUi(self)


class window_register(QtWidgets.QWidget, form_register):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super(window_register, self).__init__()
        self.setupUi(self)

    def mouseMoveEvent(self, event):  # 重写移动事件
        self._endPos = event.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None


# if __name__ == '__main__':
#     app = QApplication(sys.argv)  # 创建应用程序
#     loginwidget = QWidget()  # 创建主窗口
#
#     loginwidget.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
#     loginwidget.setAutoFillBackground(False)
#     loginwidget.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示
#     ui = Ui_Form()  # 调用主窗口
#
#     ui.setupUi(loginwidget)  # 向主窗口添加控件
#
#     loginwidget.show()  # 显示窗口
#     sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = mywindow()
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
