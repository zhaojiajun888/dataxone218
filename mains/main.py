# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import unittest
import time
from commons import HTMLTestRunner
from commons.send_email_html import Sendemail
from commons.send_email_fujian import Send_email_fujian
from cases.syncmanage_mm_ca import Syncmanage_mm
from cases.syncmanage_om_ca import Sycnanage_om
from cases.syncmanage_oo_ca import Syncmanage_oo
from cases.syncmanage_tdtd_ca import Syncmanage_tdtd
from send_email_log import Sendlog


testcases = [Syncmanage_mm,Sycnanage_om,Syncmanage_oo,Syncmanage_tdtd]


def test_report():
    """HTMLTestrunner测试报告"""
    testunit = unittest.TestSuite()  # 构建测试套间
    # 循环读取数组中的用例
    for case in testcases:
        testunit.addTest(unittest.makeSuite(case))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    fileName = '/dataxone218/results/' + 'Result_' + current_time + '.html'  # 定义报告路径
    fp = open(fileName, 'wb')  # 测试报告模板
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
    return runner.run(testunit)



if __name__ == '__main__':

    test_report()
    sendemail = Send_email_fujian()
    sendemail.send_be_report()

    sendlog = Sendlog()
    sendlog.sendlog()


