# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import paramiko
from io import StringIO,BytesIO
from commons.log import loggers
class Linuxopera():

    hname = "10.0.0.65"
    uname = "liutt"
    pwd = "liutt"
    # 创建连接
    def linuxcommand(self,commands,host=hname,username=uname,password=pwd):
        # 创建ssh对象
        client = paramiko.SSHClient()
        # 如果之前没有,连接过的ip,会出现选择yes或者no的操作,自动选择yes
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # 连接服务器
        client.connect(hostname=host,port=22,username=username,password=password)
        # # 创建命令
        # command = "ls"
        # 执行命令
        stdin, stdout, stderr = client.exec_command(commands)
        # 获取结果
        result = stdout.read().decode('utf-8')
        print(result)
        # 关闭链接
        client.close()

    # 读取文件内容到内存
    def linux_readfile(self,paths,host=hname,username=uname,password=pwd):
        # 创建ssh对象
        client = paramiko.SSHClient()
        # 如果之前没有,连接过的ip,会出现选择yes或者no的操作,自动选择yes
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # 连接服务器
        client.connect(hostname=host, port=22, username=username, password=password)
        sftpclient = client.open_sftp()
        results = sftpclient.open(paths)
        """将读取的文件内容放入内存"""
        try:
            s = StringIO()
            for line in results:
                s.write(line)
            # 将内存中的内容打印到log
            contents = s.getvalue()
            loggers.info(contents)
            # 释放内存
            s.close()
        finally:
            results.close()



if __name__ == "__main__":
    l = Linuxopera()
    # l.linuxcommand("ls")
    l.linux_readfile("/dsg/liutt/defaultPath/testclone02/dt_testclone02/config/yloader.ini")