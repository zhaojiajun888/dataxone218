# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


import time
import unittest
from BeautifulReport import BeautifulReport
from cases.syncmanage_mm_ca import Syncmanage_mm
from cases.syncmanage_om_ca import Sycnanage_om
from cases.syncmanage_oo_ca import Syncmanage_oo
from cases.syncmanage_tdtd_ca import Syncmanage_tdtd
from commons.send_email_log import Sendlog
from commons.send_email_fujian import Send_email_fujian


testcases = [Syncmanage_mm,Sycnanage_om,Syncmanage_oo,Syncmanage_tdtd]

def test_report():

    """Beautifulreport测试报告"""
    testunit = unittest.TestSuite()  # 构建测试套间
    # 循环读取数组中的用例
    for case in testcases:
        testunit.addTest(unittest.makeSuite(case))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    fileName = '/dataxone218/results/'  # 定义报告路径
    BeautifulReport(testunit).report(description="接口自动化测试报告",filename="beautifulreport" + current_time,
                                     report_dir=fileName)
    # 发送附件邮件
    sendemail = Send_email_fujian()
    sendemail.send_be_report()

    # 发送log
    sendlog = Sendlog()
    sendlog.sendlog()
if __name__ == '__main__':

    test_report()
    # sendemail = Sendemail()
    # sendemail.sendreport()
    #
    # sendlog = Sendlog()
    # sendlog.sendlog()


