from PyQt5 import QtWidgets



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
        # print("(%s,%s)" % (self.x, self.y))

        # self.hintmassage.move(self.groupBox.width() - (self.hintmassage.width() / 2),
        #                       self.groupBox.height() - -(self.hintmassage.height() / 2))


def printState(self):
    self.timer.start()
    # 显示状态
    #        if self.lineEdit_username.text == "1" and self.lineEdit_password.text == "1":
    if self.userflag == 0:
        return True
    if self.userflag == -1:
        words = "用户名不存在"
        self.hintmassage.setText(words)
    elif self.userflag == 1:
        words = "密码错误"
        self.hintmassage.setText(words)
    else:
        words = "请输入账号密码"
        self.hintmassage.setText(words)


def printState2(self):
    self.timer.start()
    # 显示状态
    #        if self.lineEdit_username.text == "1" and self.lineEdit_password.text == "1":
    if self.registeruserflag == -1:
        words = "请输入账号密码"
        self.hintmassage.setText(words)
    if self.registeruserflag == 0:
        self.timer.stop()  # 通过stop 进行停止
        return True
    elif self.registeruserflag == 1:
        words = "账号已存在"
        self.hintmassage.setText(words)

