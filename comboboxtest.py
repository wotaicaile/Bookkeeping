# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        country = ["中国", "新加坡", "菲律宾", "澳大利亚", "1", "2", "3", "4", "5", "6", "7", "8"]
        Form.setObjectName("Form")
        Form.resize(1280, 800)

        Form.move(250, 180)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(400, 310, 323, 51))
        self.comboBox.addItems(country)
        # self.comboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.comboBox.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "border-style:none; "
                                    "padding-left:80px;  "  # 字体距离左边的距离
                                    "width:48px; "
                                    "height:24px; "
                                    "font-size:24px; "
                                    "font-family:PingFangSC-Regular,PingFang SC; "
                                    "font-weight:400; "
                                    "color:rgba(93,169,255,1);\n"
                                    "line-height:24px; }\n"

                                    "QComboBox:drop-down {"  # 选择箭头样式
                                    "width:40px;  "
                                    "height:50px; "
                                    "border: none;  "
                                    "subcontrol-position: right center; "  # 位置
                                    "subcontrol-origin: padding;}\n"  # 对齐方式

                                    "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
                                    "border: none; "
                                    "background: transparent; "
                                    "image: url(\"./ui/resource/star.png\");}\n"

                                    "QComboBox:down-arrow:pressed { image: url(\"./ui/resource/star_green.png\"); }\n"  # 选择箭头

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:black; "
                                    "background: transparent; "
                                    "selection-color:rgba(93,169,255,1);"
                                    "selection-background-color: rgba(255,255,255,1);"
                                    "}\n"

                                    "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
                                    "width: 6px;\n"
                                    "height: 100px;"
                                    "background-color: transparent;  }\n"

                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
                                    "border-radius: 3px;   "
                                    "background: rgba(0,0,0,0.1);}\n"

                                    # "QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"  # 划过滚动条，变化
                                    # "background: rgb(90, 91, 93);}\n"

                                    "QComboBox QScrollBar::add-line::vertical{"  # 滚动条上箭头
                                    "border:none;}"
                                    "QComboBox QScrollBar::sub-line::vertical{"  # 滚动条下箭头
                                    "border:none;}"
                                    "")
        self.comboBox.setMaxVisibleItems(5)
        # self.comboBox.setMaxCount(24456232)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.comboBox.setItemText(0, _translate("Form", "111"))
        # self.comboBox.setItemText(1, _translate("Form", "222"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    setupUi1 = Ui_Form()
    setupUi1.setupUi(widget)
    widget.show()
    # widget.showFullScreen()
    sys.exit(app.exec_())
