from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt, QTimer

from common.common import movehintmassage, printState2
from common.database import queryAccount, insertAccountandpassword
from registerAccount import information_ok

from ui.RegisteredAccount_ui.RegisteredAccount import Ui_Form as form_register
from Main.mainRun import window_ok


# from registerAccount.information_ok import Ui_Form as register_ok

class window_register(QtWidgets.QWidget, form_register):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super(window_register, self).__init__()
        self.x = 0
        self.registeruserflag = -1
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示

        # 时间
        self.timer = QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(lambda: movehintmassage(self))
        self.y = 30
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

    def confirmRegiser(self):

        user = self.user_register.text().strip()
        password1 = self.password_register.text().strip()
        password2 = self.password_register2.text().strip()
        self.checkAccount()
        if self.registeruserflag == 0:
            print(password1)
            if len(password1) >= 6 and password1 == password2:

                insertResult = insertAccountandpassword(user, password1, 0)
                if insertResult is not None:
                    self.hintmassage.setVisible(True)
                    self.hintmassage.setText("注册成功")
                    print(insertResult)
                else:
                    self.hintmassage.setVisible(True)
                    self.hintmassage.setText("注册失败")
                # self.close()



            else:
                print("注册失败")
        else:
            print("注册失败")
        # if printState(self):
        #     self.w1 = window_ok()
        #     self.w1.show()
        #     self.close()

    def closeRegiser(self):
        self.close()

    def checkAccount(self):
        result = 0
        user = self.user_register.text().strip()
        if len(user) >= 6:
            result = queryAccount(user)
        if result:
            self.registeruserflag = 1
            print("账号已存在")
        elif result == 0:
            self.registeruserflag = 0
        else:
            self.registeruserflag = -1
            print("请输入账号")
        printState2(self)


def RegisteredAccount():
    win = window_register()

    win.show()
    # 设置提示框不可见
    win.hintmassage.setVisible(False)
    win.login_back_pushbutton.clicked.connect(lambda: window_register.closeRegiser(win))
    win.register_button_confirm.clicked.connect(lambda: window_register.confirmRegiser(win))

    win.user_register.editingFinished.connect(lambda: window_register.checkAccount(win))

# class window_registerOk(QtWidgets.QWidget, register_ok):
#     def __init__(self):
#         super(window_registerOk, self).__init__()
#         self.setupUi(self)
