import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication

from Main.Income.incomRun import on_bilBtn_save_clicked
from Main.Note.noteRun import on_noteBtn_clicked, on_savenotepushButton_clicked
from Main.expenditure.expendRun import on_bilBtn_save_expend_clicked
from common import aboutFile
from common.aboutFile import file_path

from common.database import queryNoteList, queryAllIncomeBill, queryAllExpendBill, AddIncomeBill, InsertIncomeBill, \
    queryoneIncomeType, queryoneExpendType, deleteIncomeType

from testshuzhuangtu import showImage, initpie, ShowIncomeImage
from ui.star_ui.start import Ui_Form as form_ok


class window_ok(QtWidgets.QWidget, form_ok):
    filesTxt = []
    noteslistIsClear = 0
    datas = []
    labels = []

    def __init__(self, user):
        super(window_ok, self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setupUi(self)

        self.noteBtn.clicked.connect(lambda: on_noteBtn_clicked(self))

        self.queryBtn.clicked.connect(self.on_queryBtn_clicked_triggered)
        self.notelistWidget.itemClicked.connect(self.item_click)
        self.savenotepushButton.clicked.connect(lambda: on_savenotepushButton_clicked(self))

        self.querybackpBn.clicked.connect(self.on_queryBtn_clicked_triggered)

        # self.StatisticsBtn.clicked.connect(lambda: pietable(0))
        self.StatisticsBtn.clicked.connect(self.showpietable)
        self.billtabWidget_2.currentChanged.connect(self.on_billabWidge_clicked)

        self.bilBtn_save.clicked.connect(lambda: on_bilBtn_save_clicked(self))
        self.expend_save.clicked.connect(lambda: on_bilBtn_save_expend_clicked(self))

        self.delete_typelabel.clicked.connect(self.on_delete_typelabel_clicked)
        self.settingBtn.clicked.connect(self.on_settingBtn_clicked)
        self.currentuser.setText(user)
        self.cancellation_2.clicked.connect(self.exit)

        # self.label_bill.setVisible(False)
        # self.billlabel_type.setVisible(False)
        # self.billcomboBox_type.setVisible(False)
        # self.billlineEdit_billnumber.setVisible(False)
        # self.billlabel_sign.setVisible(False)
        #
        # self.billlabel_type.setVisible(False)

        # self.bilBtn_save.setVisible(False)
        # self.billBtn_cancel.setVisible(False)
        # self.billtabWidget.setVisible(False)

        self.SerachLine3.textChanged.connect(self.serachNotes)
        self.clearSearchbtn.clicked.connect(self.clearSearch)
        self.writebillbtn.clicked.connect(self.showwritebill)
        self.nextpage.clicked.connect(self.showzhilitu)
        self.save_path.clicked.connect(self.on_save_path_clicked)
        self.addLable.clicked.connect(self.on_addLable_clicked)


        self.initwidget()

    def initwidget(self):



        self.billtabWidget.setVisible(False)
        self.billtabWidget_2.setVisible(False)
        self.tabWidget.setVisible(False)
        self.textEdit_note.setVisible(False)
        self.querybackpBn.setVisible(False)
        self.massage_income.setVisible(False)
        self.massage_expend.setVisible(False)
        self.frame_2.setVisible(False)
        self.savenotepushButton.setVisible(False)
        self.typelabel.setVisible(False)
        self.save_typelabel.setVisible(False)
        self.delete_typelabel.setVisible(False)
        self.checkBoxIncome.setVisible(False)
        self.checkBoxExpend.setVisible(False)


    def exit(self):
        self.close()
        self.cancellation_2.close()

    def on_addLable_clicked(self):
        self.initwidget()
        self.typelabel.setVisible(True)
        self.save_typelabel.setVisible(True)
        self.delete_typelabel.setVisible(True)
        self.checkBoxIncome.setVisible(True)
        self.checkBoxExpend.setVisible(True)
        self.save_typelabel.disconnect()
        self.save_typelabel.clicked.connect(self.on_save_typelabel_clicked)


    def on_delete_typelabel_clicked(self):

        deleteIncomeType(self.typelabel.text())

    @pyqtSlot()
    def on_save_typelabel_clicked(self):
        flag = 0
        count = self.billcomboBox_usetype.count()
        # 遍历billcomboBox_usetype中的标签
        if self.checkBoxIncome.isChecked():
            for i in range(count):
                if self.typelabel.text() == self.billcomboBox_usetype.itemText(i):
                    print("添加失败")
                    flag = 1
            if flag == 0:
                self.billcomboBox_usetype.addItem(self.typelabel.text())
                InsertIncomeBill(self.typelabel.text(), 0)
                print("添加成功")
                    # self.billcomboBox_usetype.removeItem(self.typelabel.text())



    def on_save_path_clicked(self):
        file_path = self.savepath.text().strip()
        str = "当前路径" + file_path
        self.label_hintPath.setText(str)

    def on_settingBtn_clicked(self):
        self.initwidget()
        str = "当前路径" + aboutFile.file_path
        self.label_hintPath.setText(str)
        self.frame_2.setVisible(True)

    def showzhilitu(self):
        ShowIncomeImage(self, aboutFile.image_zhipath)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def loadnotelistWidgetdata(self):
        print("loadnotelistWidgetdata")
        self.filesTxt = queryNoteList(aboutFile.file_path)
        # print(self.filesTxt)
        # 将文件遍历出来
        it = iter(self.filesTxt)  # 创建迭代器对象
        for x in it:
            self.notelistWidget.addItem(x)

        # print(results, end="\n")
    def loadincomelistWidgetdata(self):

        print("loadincomelistWidgetdata")
        datasIncome = queryAllIncomeBill()
        # 将收入遍历出来
        for i in range(len(datasIncome)):
            str = "%s,%s"%(datasIncome[i][0],datasIncome[i][1])
            print(str)
            self.incomelistWidget.addItem(str)

    def loadoutlistWidgetdata(self):

        print("loadoutlistWidgettdata")
        datasExpend = queryAllExpendBill()
        # 将收入遍历出来
        for i in range(len(datasExpend)):
            str = "%s,%s" % (datasExpend[i][0], datasExpend[i][1])
            print(str)
            self.outlistWidget.addItem(str)

    def on_queryBtn_clicked_triggered(self):
        self.initwidget()
        self.notelistWidget.clear()
        self.incomelistWidget.clear()
        self.outlistWidget.clear()
        self.loadnotelistWidgetdata()
        self.loadincomelistWidgetdata()
        self.loadoutlistWidgetdata()
        self.tabWidget.setVisible(True)

        self.textEdit_note.setVisible(False)
        self.querybackpBn.setVisible(False)
        print("queryBtn_clicked")

    def showwritebill(self):
        self.initwidget()
        self.billcomboBox_usetype.clear()
        self.expend_usetype.clear()
        self.billtabWidget.setVisible(True)
        self.incometab_2.setVisible(True)
        self.expendtab_2.setVisible(True)
        data1 = queryoneIncomeType()
        for i in range(len(data1)):
            self.billcomboBox_usetype.addItem(data1[i][0])
        data2 = queryoneExpendType()
        for i in range(len(data2)):
            self.expend_usetype.addItem(data2[i][0])

        # self.label_bill.setVisible(True)
        # self.billlabel_type.setVisible(True)
        # self.billcomboBox_type.setVisible(True)
        # self.billlineEdit_billnumber.setVisible(True)
        # self.billlabel_sign.setVisible(True)
        #
        # self.billlabel_type.setVisible(True)
        # self.billcomboBox_usetype.setVisible(True)
        # self.bilBtn_save.setVisible(True)
        # self.billBtn_cancel.setVisible(True)

    def showpietable(self):
        self.initwidget()
        self.billtabWidget_2.setVisible(True)
        initpie()
        showImage(self, 0)
        showImage(self, 1)
        self.incometab_2.setVisible(False)

    def on_billabWidge_clicked(self):
        page = self.billtabWidget_2.currentIndex()
        print("on_billabWidge_clicked")
        showImage(self, page)

        # self.label_bill.setVisible(False)
        # self.billlineEdit_billnumber.setVisible(False)
        # self.billlabel_sign.setVisible(False)
        # self.billlabel_type.setVisible(False)
        # self.billcomboBox_usetype.setVisible(False)
        #
        # self.bilBtn_save.setVisible(False)
        # self.billBtn_cancel.setVisible(False)
        # self.massage_income.setVisible(False)

    def clearSearch(self):
        self.SerachLine3.clear()
        print("clearSearch")

    def item_click(self):
        print("item_click")
        self.tabWidget.setVisible(False)  # 关掉面板，因为这个时候可能之前打开了这个面板
        self.textEdit_note.setVisible(True)
        self.querybackpBn.setVisible(True)
        self.querybackpBn.move(810, 10)
        filename = file_path + self.notelistWidget.currentItem().text() + ".txt"
        print(filename)
        try:
            with open(filename, 'r') as f:
                my_txt = f.read()
                self.textEdit_note.setText(my_txt)
                self.textEdit_note.setPlainText(my_txt)

        except:
           print("失败")

    def serachNotes(self):
        print("serachNotes")
        temp = -1
        serachNote = self.SerachLine3.text()
        print(serachNote)
        # print("1")
        # # if serachNote == self.filesTxt:
        # print(self.notelistWidget.item(3).text())

        # 获取listwidget中条目数
        count = self.notelistWidget.count()
        # 遍历listwidget中的内容
        for i in range(count):
            if serachNote == self.filesTxt[i]:
                temp = i
            else:
                pass
        if temp > -1:  # 找到了
            self.notelistWidget.clear()
            self.notelistWidget.addItem(serachNote)
            self.noteslistIsClear = 1
        if self.noteslistIsClear == 1 and self.SerachLine3.text() == "":
            self.notelistWidget.clear()
            self.loadnotelistWidgetdata()
            self.noteslistIsClear = 0


if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = window_ok("未登录")
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
