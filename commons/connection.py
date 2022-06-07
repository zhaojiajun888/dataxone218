# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import pymysql
from commons.log import loggers


class Connmysql():

    def select(self,sql):
        """
            封装数据库查询数据并返回
        :param sql:
        :return:
        """
        try:
            con = pymysql.connect(host="10.0.0.140",user="root",password="dsgdata",
                                  database="automation_dsg_db_new")
            cursor = con.cursor()
            cursor.execute(sql)
            #获取数据
            data = cursor.fetchall()
            cursor.close()
            con.close()
            return data
        except Exception as e:
            loggers.info(e)


if __name__ == "__main__":

    pass