from PyQt5.QtWidgets import QFileDialog


# self.action_open.clicked.connect(self.clearWidget)
from common.aboutFile import file_path


def on_noteBtn_clicked(self):
    self.initwidget()
    self.tabWidget.setVisible(False)
    self.textEdit_note.setVisible(True)
    self.textEdit_note.clear()
    self.savenotepushButton.setVisible(True)
    self.querybackpBn.setVisible(False)


def on_savenotepushButton_clicked(self):
    filename=QFileDialog.getSaveFileName(self,'save file',file_path+'/未命名.txt')
    # r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    # 关键字with在不再需要访问文件后将其关闭 ，open返回的对象存储在f这个变量当中
    try:
        with open(filename[0], 'w+') as f:
            my_txt = self.textEdit_note.toPlainText()
            f.write(my_txt)
    except:
        pass




def on_action_open_triggered(self):
    self.tabWidget.setVisible(False)
    """
    打开文件，显示在多行文本框中，即显示日记在文本框中
    """
    print("打开")
    filename = QFileDialog.getOpenFileName(self, '打开文件夹', '.')
    # r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    # 关键字with在不再需要访问文件后将其关闭 ，open返回的对象存储在f这个变量当中
    try:
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit_note.setPlainText(my_txt)
    except:
        pass
