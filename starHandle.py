# 通过天气接口获取晴雨，鼠标点击将有不同特效，比如晴天的时候是太阳，雨天的时候是雨滴，晚上是星星和月亮

from PyQt5.Qt import *
from ui.start import Ui_Form


# 创建主窗口
class MainWin(QMainWindow):  # 这里如果是QWight，背景图片会加载不了
    i = 0
    j = 0
    time = 0
    count = 0
    # "star.png", "star_pink.png", "star_green.png", "star_purple.png"
    # "sun.png",, "litghting.png",
    star_list = (["rain.png","sun.png"],["water.png","star.png"])
    tianqi_list = ["water.png","star.png"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # 向主窗口添加控件

        # self.ui.label_tianqi.setPixmap(QPixmap("tianqi.png").scaled(self.ui.label_tianqi.width(),
        # self.ui.label_tianqi.height()))

        # 时间
        self.timer = QTimer()
        self.timer.setInterval(10)  # 10毫秒
        self.timer.timeout.connect(self.movestar)

    def selectIcon(self):
        import random
        print(random.randint(0, 0))

        i = random.randint(0, 0)
        print(str(self.star_list[i][0]))
        return QPixmap(str(self.tianqi_list[i]))

    def close(self):
        print("test1")
        self.ui.push_close.close()
        self.ui.note_ui.close()

    # 点击时出现图片
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:

            if 350 <= event.x() < 390 and 50 <= event.y() < 90:
                self.close()
            # if self.j > 310:  # 判断前一个星星是否掉落，若无此句，会导致星星卡在中间就生成了标签
            else:

                self.time = 0  # 清空

                # 让标签出现在鼠标中点，当前鼠标位置减去1/2图像大小，即为中心点
                ofsetx = self.ui.label.width() / 2
                ofsety = self.ui.label.height() / 2
                self.i = event.x() - ofsetx
                self.j = event.y() - ofsety
                self.openimage()
                self.ui.label.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
                self.count += 1
                # self.ui.label.setText("test")  # 是self.ui.label,注意不要写成self.lable或者self.label

    # 松开时图片掉落效果
    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.time = 0  # 清空
            self.timeChange()

    def timeChange(self):
        self.timer.start()
        # print("松开")

    def openimage(self):
        pixmap = self.selectIcon()
        self.ui.label.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
        self.createIcon(pixmap)
        # jpg = QPixmap("beizi.png").scaled(self.label.width(), self.label.height())
        # self.ui.label.setText("test")  # 是self.ui.lable,注意不要写成self.lable
        # self.ui.label.setPixmap(jpg)

    # 每2毫秒修改movestar

    def movestar(self):

        if self.j < 315:
            self.time += 20
            # print(self.time)
            self.j += 10
            self.ui.label.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动

            # print("(%s,%s)" % (self.i, self.j))

    def createIcon(self,pixmap):
        import random

        i = random.randint(0, 1)
        print(str(self.star_list[0][i]))
        pixmap = QPixmap(str(self.star_list[0][i]))

        if self.count == 0:
            self.ui.label_2.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_2.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 1:
            self.ui.label_3.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_3.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 2:
            self.ui.label_4.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_4.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 3:
            self.ui.label_5.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_5.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 4:
            self.ui.label_6.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_6.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 5:
            self.ui.label_7.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_7.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 6:
            self.ui.label_8.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_8.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 7:
            self.ui.label_9.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_9.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动
        if self.count == 8:
            self.ui.label_10.setPixmap(pixmap.scaled(self.ui.label.width(), self.ui.label.height()))
            self.ui.label_10.move(self.i, self.j)  # 实现点击生成图片（伪），实际上是标签随着移动

        elif self.count > 10:
            self.count = -1  # 让星星重新开始


if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = MainWin()
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
