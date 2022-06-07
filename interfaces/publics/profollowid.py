# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import random

class Profollowid():

    def followidpa(self):
        # 获取当前时间戳
        mils = str(round(time.time()*1000))
        # 获取前6位数字
        strflow = ""
        for num in range(1,7):
            string = str(random.randint(1,9))
            strflow += string
        flowid = mils + strflow
        return flowid

if __name__ == "__main__":
        p = Profollowid()
        p.followidpa()
