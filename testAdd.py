from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *

import sys


class A(QWidget):
    i = 0

    def __init__(self):
        super(A, self).__init__()
        self.setFixedSize(400, 500)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        # 时间
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 10毫秒
        self.timer.timeout.connect(self.btn1)
        self.timer.start()

    # def mousePressEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         print("test")
    #         # self.i += 1

    def btn1(self):
        label = {}

        pixmap = QPixmap("resource/star.png")

        label[self.i] = QLabel(str(self.i))
        label[self.i].setFixedSize(100, 100)
        self.layout.addWidget(label[self.i])
        label[self.i].setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        label[self.i].move(0,0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = A()

    win.show()
    sys.exit(app.exec_())
