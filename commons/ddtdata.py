# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

from commons.connection import Connmysql

class Ddtdata():

    def ddtdata(self,sql):
        """
            数据库获取数据，返回（[]）形式数据，并去掉testname
        :param sql:
        :return:
        """
        # 获取数据库数据
        co = Connmysql()
        sqldata = co.select(sql)
        listdata= []

        for i in sqldata:
            data = list(i)
            listdata.append(data[1:])
        ddtdata = tuple(listdata)
        return ddtdata

if __name__ == "__main__":
    dd = Ddtdata()
    dd.ddtdata("SELECT * FROM partnerdata where testname='login_in'")




