from common.database import AddIncomeBill, InsertIncomeBill, queryoneIncomeBill
from testshuzhuangtu import pietableIncome


def on_bilBtn_save_clicked(self):
    print("on_bilBtn_save_clicked")
    Incometype = self.billcomboBox_usetype.currentText()
    IncomeCount = int(self.billlineEdit_billnumber.text())
    print(Incometype,IncomeCount)
    try:
        if queryoneIncomeBill(Incometype):
            AddIncomeBill(Incometype, IncomeCount)
            self.massage_income.setVisible(True)
            self.massage_income.setText("记录成功！")
            pietableIncome()
        else:
            InsertIncomeBill(Incometype, IncomeCount)
    except:
        self.massage_income.setText("记录失败！")


