from PyQt5.QtGui import QImage, QPixmap

from common import aboutFile
from common.database import queryAllIncomeBill, queryAllExpendBill
import matplotlib.pyplot as plt  # 导入绘图包

from testInsert import MainDialogImgBW


def pietableExpend():
    datas = []
    labels = []
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    datasExpend = queryAllExpendBill()
    for i in range(len(datasExpend)):
        print(datasExpend[i][1])
        datas.append(datasExpend[i][1])
        print(datasExpend[i][0])
        labels.append(datasExpend[i][0])
    plt.pie(x=datas, labels=labels, autopct='%3.1f%%')  # 以时间为标签，总计成交笔数为数据绘制饼图，并显示3位整数一位小数
    plt.title('支出图')  # 加标题
    plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    plt.savefig(aboutFile.image_Expendpath)  # 保存

    plt.clf()  # 清除缓存


def pietableIncome():
    datas = []
    labels = []
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    #

    datasIncome = queryAllIncomeBill()

    for i in range(len(datasIncome)):
        print(datasIncome[i][1])
        datas.append(datasIncome[i][1])
        print(datasIncome[i][0])
        labels.append(datasIncome[i][0])
    plt.pie(x=datas, labels=labels, autopct='%3.1f%%')  # 以时间为标签，总计成交笔数为数据绘制饼图，并显示3位整数一位小数
    plt.title('收入图')  # 加标题
    plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    plt.savefig(aboutFile.image_Incomepath)  # 保存

    plt.clf()  # 清除缓存
    # self.la('D:/test.png')


def zhifangtuIncome():
    # -*- coding: utf-8 -*-
    datas = []
    labels = []
    listbar = []
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    #
    dataszhiIncome = queryAllIncomeBill()
    for i in range(len(dataszhiIncome)):
        print(dataszhiIncome[i][1])
        datas.append(dataszhiIncome[i][1])
        print(dataszhiIncome[i][0])
        labels.append(dataszhiIncome[i][0])
        listbar.append(i)
        plt.bar(i + 1, datas[i], label=labels[i])
    print(dataszhiIncome)

    #
    # plt.bar([2, 4, 6, 8, 10], [4, 6, 8, 13, 15], label='graph 2')

    # params

    # x: 条形图x轴
    # y：条形图的高度
    # width：条形图的宽度 默认是0.8
    # bottom：条形底部的y坐标值 默认是0
    # align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

    plt.legend()

    plt.xlabel('类型')
    plt.ylabel('金额')

    # plt.title(u'测试例子——条形图', FontProperties=font)
    plt.savefig(aboutFile.image_Incomepath)  # 保存

    plt.clf()  # 清除缓存


def ShowIncomeImage(self, selfimage_Incomepath):
    self.label_satatisticIncome.setPixmap(
        QPixmap(selfimage_Incomepath))


def ShowExpendImage(self, selfimage_Expendpath):
    self.label_satatisticIncome.setPixmap(
        QPixmap(selfimage_Expendpath))


def showImage(self, flag):
    if flag == 0:
        self.label_satatisticIncome.setPixmap(
            QPixmap(aboutFile.image_Incomepath))
    elif flag == 1:
        self.label_satatisticEpend.setPixmap(QPixmap(aboutFile.image_Expendpath))


def initpie():
    pietableExpend()
    pietableIncome()
    zhifangtuIncome()


if __name__ == "__main__":
    pass
