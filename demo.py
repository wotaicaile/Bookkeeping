# python
import json, requests

from PyQt5.QtWidgets import QApplication, QDialog

from ui import Weather


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Weather.Ui_Dialog()
        self.ui.setupUi(self)

    def queryWeather(self):

        r = requests.get("http://api.k780.com/?app=weather.realtime&weaId=167&ag=today,futureDay,lifeIndex,"
                         "%22%22futureHour&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json")

        text_dic = json.loads(r.text)
        state = text_dic['success']

        print(text_dic)  # 结果 {'province': 'GuangDong', 'city': 'ShenZhen'}

        if state == "1":
            area_1 = json.loads(r.text).get('result').get("area_1")
            area_2 = json.loads(r.text).get('result').get("area_2")

            week = json.loads(r.text).get('result').get("realTime").get('week')
            wtNm = json.loads(r.text).get('result').get("realTime").get('wtNm')
            self.ui.textEdit.setText(area_1+'\t'+area_2+'\n'+week+'\t'+wtNm)


        else:
            self.ui.textEdit.setText("获取失败！")



    def clearText(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    import sys

    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
