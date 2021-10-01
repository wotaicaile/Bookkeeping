# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QDate, QDateTime, QTime

from test.testwritenote import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    记账本小demo
    """

    def __init__(self, parent=None):
        """
        初始化界面
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 弹出日历控件
        self.dateTimeEdit.setCalendarPopup(True)
        # 信号
        self.dateTimeEdit.dateTimeChanged.connect(self.display_date)
        self.comboBox.currentIndexChanged.connect(self.display_weather)

    def display_date(self):
        """把所选择的日期显示在单行文本框中"""

        date = self.dateTimeEdit.date()
        date_info = self.lineEdit_date.setText(date.toString("yyyy-MM-dd dddd"))
        date_info = self.textEdit_write_diary.setPlainText(date.toString("yyyy-MM-dd dddd") + '\n')

    def display_weather(self, weather):
        """把所选择的天气显示在单行文本框中"""

        weather = self.comboBox.currentText()
        self.lineEdit_weather.setText(weather)
        # self.textEdit_write_diary.setPlainText(a + weather)

    @pyqtSlot()
    def on_action_open_triggered(self):
        """
        打开文件，显示在多行文本框中，即显示日记在文本框中
        """
        print("打开")
        filename = QFileDialog.getOpenFileName(self, '打开文件夹', '.')
        # r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        # 关键字with在不再需要访问文件后将其关闭 ，open返回的对象存储在f这个变量当中
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit_write_diary.setPlainText(my_txt)

    @pyqtSlot()
    def on_action_alter_triggered(self):
        """
        修改日记
        """
        print("修改日记")
        filename = QFileDialog.getOpenFileName(self, '打开文件夹', '.')
        # r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        # 关键字with在不再需要访问文件后将其关闭 ，open返回的对象存储在f这个变量当中
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit_write_diary.setPlainText(my_txt)

    @pyqtSlot()
    def on_action_save_triggered(self):
        """
        Slot documentation goes here.
        """
        filename = QFileDialog.getSaveFileName(self, '保存文件', '.')
        with open(filename[0], 'w') as f:
            my_text = self.textEdit_write_diary.toPlainText()
            f.write(my_text)

    @pyqtSlot()
    def on_action_close_triggered(self):
        """
        关闭窗口
        """
        main_Window = QApplication.instance()
        main_Window.quit()

    @pyqtSlot()
    def on_action_about_triggered(self):
        """
        弹出一个对画框
        """
        QMessageBox.information(self, '关于我们', '欢迎使用日记本小程序~')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
