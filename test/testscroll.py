from PyQt5.QtWidgets import QApplication, QTableWidget, QMainWindow

from test.testwritenote import Ui_MainWindow


class MyTableWidget(QTableWidget):
    def __init__(self):
        super(MyTableWidget, self).__init__()

        self.nCurScroller = 0  # 翻页时的当时滑动条位置
        self.pageValue = 24  # 一页显示条数
        self.create_form()

    def create_form(self):
        self.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)  # 双击编辑
        # self.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        # self.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)

    def pre_page(self):

        max_value = self.verticalScrollBar().maximum()  # 当前SCROLLER最大显示值
        self.nCurScroller = self.verticalScrollBar().value()  # 获得当前scroller值

        if self.nCurScroller > 0:
            self.verticalScrollBar().setSliderPosition(self.nCurScroller - self.pageValue)
        else:
            self.verticalScrollBar().setSliderPosition(max_value)

    def next_page(self):

        # verticalScrollBar().setSliderPosition()  设置当前滑动条的位置
        # verticalScrollBar().maximum()            滑动条能移动的最大位置
        # verticalScrollBar().value()                  获得当前滑动条的位置
        max_value = self.verticalScrollBar().maximum()  # 当前SCROLLER最大显示值
        self.nCurScroller  = self.verticalScrollBar().value()  # 获得当前scroller值

        if self.nCurScroller < max_value:
            self.verticalScrollBar().setSliderPosition(self.pageValue + self.nCurScroller)
        else:
            self.verticalScrollBar().setSliderPosition(0)

