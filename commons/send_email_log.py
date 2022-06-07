# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import os,time,datetime
import smtplib
from email.mime.text import MIMEText

'''
    # 首先需要在163邮箱发件人 设置 开启smtp服务
    # 将本脚本 密码处填写 授权码而非邮件 密码
    # msg['From']和msg['To'] 名称不可替换，否则可能被视为垃圾邮件
'''

class Sendlog():

    # 定义发送邮件
    def sendemail(self,file_new):

        # 定义正文
        f = open(file_new, 'rb')
        mail_body = f.read()
        #将byte类型mail_body修改为str
        newmail_body = str(mail_body,encoding="GBK")
        f.close()
        #msg = MIMEText(newmail_body, _subtype='html',_charset='GBK')
        msg = MIMEText(newmail_body, _subtype='plain', _charset='GBK')
        # 发信邮箱
        msg['From'] = 'zjj502690608@163.com'

        # 收件箱
        #msg['To'] = "502690608@qq.com,1140459560@qq.com"
        msg['To'] = "502690608@qq.com"
        # 定义标题
        msg['Subject']=u"自动化测试日志"
        #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
        msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
        # 创建邮件发送对象
        smtp=smtplib.SMTP()
        #连接SMTP服务器，此处用的163的SMTP服务器
        smtp.connect(host='smtp.163.com',port='25')
        # 用户名密码
        smtp.login(user='zjj502690608@163.com',password='YZIWWTJUMJZKMAVZ')

        # 如果只有一个接收者则之作用msg['To']
        smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())

        smtp.quit()
        print('email has send out !')

    # 查找测试报告，调用发邮件功能
    def sendlog(self):
        #result_dir = 'C:/codes/project/walletjiekou/wa_result'
        log_dir = '/dataxone218/logs/'
        lists = os.listdir(log_dir)
        lists.sort(key=lambda fn: os.path.getmtime(log_dir + "\\" + fn) if not os.path.isdir(log_dir + "\\" + fn) else 0)
        print(u'最新测试生成的报告： ' + lists[-1])
        # 找到最新生成的文件
        file_new = os.path.join(log_dir,lists[-1])

        #调用发邮件模块
        self.sendemail(file_new)

if __name__ == '__main__':
    # 执行测试用例
    # runner.run(alltestnames)
    # 执行发邮件
    send = Sendlog()
    send.sendlog()
