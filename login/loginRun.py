from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QApplication

from Main.mainRun import window_ok
from common.common import printState, movehintmassage
from common.database import *
from registerAccount.registerAccountRun import RegisteredAccount

from ui.login_ui.login import Ui_Form


class loginRun(QtWidgets.QDialog, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super(loginRun, self).__init__()
        self.x = 0
        self.islogin = 0
        self.user = "未登录"
        self.userflag = -1
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示

        self.login_button.clicked.connect(self.confirmLogin)
        self.login_button.clicked.connect(self.rememberAccountAndPassword)

        self.register_button.clicked.connect(RegisteredAccount)

        self.user.editingFinished.connect(self.autologin)

        # self.y = self.groupBox.height() - (self.hintmassage.height() / 2)
        self.y = 30
        # 时间
        self.timer = QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(lambda: movehintmassage(self))

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:  # 大键盘上的键是Qt.Key_Return，小键盘上的Enter才是Qt.Key_Enter
            print('enter')
            self.confirmLogin()
            print("失败")

    # 【读取内容】按钮功能
    def confirmLogin(self):
        user = self.user.text().strip()
        password = self.password.text().strip()
        self.userflag = queryAccountandpassword(user, password)
        print(self.userflag)
        if printState(self):
            self.islogin = 1
            self.w1 = window_ok(user)

            self.w1.show()
            self.close()
            return True
        else:
            return False

    def rememberAccountAndPassword(self):

        print("1")
        if self.checkBox.isChecked():
            print("rememberAccountAndPassword")
            # 如果账号密码正确
            self.user = self.user.text().strip()
            password = self.password.text().strip()
            if queryAccountandpassword(self.user, password) == 0:
                UpdateAccountList(self.user, 1)
                print("保存账号")
            else:
                print("保存失败")
                # 如果已经登陆
                # 更新
                # UpdateAccountList(user, state=1)

                # 存入数据库

    def autologin(self):
        user = self.user.text().strip()
        if queryAccount(user):
            if queryAccountState(user):
                self.password.setText(queryAccountPassword(user))

        # password = queryAccountandpassword(user, password)
        # self.password.setText(password)




if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = loginRun()
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
