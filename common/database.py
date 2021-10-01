import pymysql


def connectDasebase():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="UserList",
                               charset='utf8')
        print("连接成功")

        return conn
    except Exception as e:
        print(e)
        print("连接数据库失败")


def queryoneIncomeBill(Incometype):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select Income_type from income where Income_type = '%s'" % (Incometype)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，插入语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("查询数据库失败")

def deleteIncomeType(Incometype):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "DELETE FROM income WHERE Income_type = '%s'" % (Incometype)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，插入语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("删除数据库失败")

def queryoneIncomeType():
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select Income_type from income"

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")

def queryoneExpendType():
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select Expend_type from expend"

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def InsertIncomeBill(Incometype, IncomeCount):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "insert into income values('%s',%s)" % (Incometype,IncomeCount)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，插入语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("插入数据库失败")


def AddIncomeBill(Incometype, IncomeCount):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "update income set Income_number = Income_number + %d where Income_type = '%s'" % (
            IncomeCount, Incometype)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，更新语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("更新数据库失败")


def AddExpendBill(Expendtype, ExpendCount):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句
        sql = "update expend set Expend_number = Expend_number + %d where Expend_type = '%s'" % (
            ExpendCount, Expendtype)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，插入语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("插入数据库失败")


def queryAllExpendBill():
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select Expend_type , Expend_number from expend"

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        else:
            return 0
        # 将id和name显示到界面表格上
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data[0][1]))
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def queryAllIncomeBill():
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select Income_type  ,Income_number from Income"

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        else:
            return 0
        # 将id和name显示到界面表格上
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data[0][1]))
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def UpdateAccountList(user, state):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 更新的sql语句
        sql = "update Users set  User_autoState=%s where User_ID =%s" % (state, user)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        UpdataResult = cur.execute(sql)
        if UpdataResult > 0:
            cur.connection.commit()  # 执行commit操作，更新语句才能生效
            print("更新数据库成功")
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("更新数据库失败")


def insertAccountandpassword(user, password, state):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "INSERT INTO Users VALUES (%s,%s,%s) " % (user, password, state)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        insertResult = cur.execute(sql)
        if insertResult > 0:
            cur.connection.commit()  # 执行commit操作，插入语句才能生效
        cur.close()
        conn.close()
        return insertResult
    except Exception as e:
        print(e)
        print("插入数据库失败")


def queryAccountPassword(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select User_password from users where user_id =%s " % user

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data[0][0]
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def queryAccountState(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select User_autoState from users where user_id =%s " % user

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data[0][0]
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def queryAccountandpassword(user, password):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select User_id,User_password from users where  User_id =%s " % (user)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            if data[0][1] == password:
                # 打印测试
                print(data[0][0])
                print(data[0][1])
                print("密码正确")
                return 0
            else:
                return 1
                print("密码错误")
        else:
            return -1
            print("账号不存在")

        # 将id和name显示到界面表格上
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data[0][1]))
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


# 查看账号是否存在
def queryAccount(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select User_id from users where  User_id =%s " % (user)
        result = cur.execute(sql)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        # 输入框为空：
        if result is None:
            return -1
        # 账号存在：
        elif result > 0:
            return 1
        # 账号不存在：
        else:
            return 0
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def queryNoteList(file_path):
    import os
    filesTxt = []
    list = os.listdir(file_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        if list[i][-4:] == ".txt":
            filesTxt.append(list[i][:-4])
    return filesTxt

    #
    #
    # try:
    #
    #     file_path = "C:/Users/liujiana/PycharmProjects/ReadingStatistics/Main/Note/notes/"
    #
    #     newName = re.findall(r'[^\\/:*?"<>|\r\n]+$', file_path)
    #
    #     newName = re.findall(r'(.+?)\.txt', newName[0])
    #
    #     os.system('python markup.py < %s > d:/%s.html ' % (file_path, newName[0]))
    #     # conn = connectDasebase()
    #     # cur = conn.cursor()
    #     # 查询的sql语句
    #     # with open(filename, 'r') as f:
    #     #     my_txt = f.read()
    #     # print(my_txt)
    # except:
    #     print("连接失败")
    #     pass


if __name__ == "__main__":
    pass
