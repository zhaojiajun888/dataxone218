# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import random
from commons.base import Base
from commons.fileopera import Fileopera
from interfaces.publics.gettoken_pa import Get_token


class Publicmethods(Base):

    def __init__(self):
        self.token = Get_token().gettokepa()

    # 获取followid
    def getfollowid(self):
        # 获取当前时间戳
        mils = str(round(time.time()*1000))
        # 获取前6位数字
        strflow = ""
        for num in range(1,7):
            string = str(random.randint(1,9))
            strflow += string
        followid = mils + strflow
        # 定义taskname
        times = time.strftime("%d%H%M%S", time.localtime())
        taskname = "autoda" + times

        # 将taskname和follow_id输入到txt文件中
        contents = str(taskname + "," + followid)
        Fileopera().writefilepa(contents)
