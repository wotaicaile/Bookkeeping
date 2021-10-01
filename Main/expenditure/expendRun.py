from common.database import AddExpendBill
from testshuzhuangtu import pietableExpend


def on_bilBtn_save_expend_clicked(self):
    print("save2")
    self.massage_expend.setVisible(True)
    Expendtype = self.expend_usetype.currentText()
    ExpendCount = int(self.billlineEdit_billnumber_2.text())
    if AddExpendBill(Expendtype, ExpendCount):
        self.massage_expend.setVisible(True)
        self.massage_expend.setText("记录成功！")
        pietableExpend()
    else:
        self.massage_expend.setText("记录失败！")