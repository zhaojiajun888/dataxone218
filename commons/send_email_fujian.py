# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Send_email_fujian():
    """
        发送beautiful测试报告（作为附件）
    """
    def send_be_report(self):
        # 数据集
        sender = 'zjj502690608@163.com'
        receiver = '502690608@qq.com'
        smtpserver = 'smtp.163.com'
        username = 'zjj502690608@163.com'
        password = 'YZIWWTJUMJZKMAVZ'
        mail_title = '主题：自动化测试报告'

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = Header(mail_title, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('beautiful测试报告，详见附件', 'plain', 'utf-8'))

        # # 构造附件1（附件为TXT格式的文本）
        # att1 = MIMEText(open('text1.txt', 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="text1.txt"'
        # message.attach(att1)

        # # 构造附件2（附件为JPG格式的图片）
        # att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
        # message.attach(att2)

        # 构造附件3（附件为HTML格式的网页）
        log_dir = '/dataxone218/results'
        lists = os.listdir(log_dir)
        lists.sort(
            key=lambda fn: os.path.getmtime(log_dir + "\\" + fn) if not os.path.isdir(log_dir + "\\" + fn) else 0)
        print(u'最新测试生成的报告： ' + lists[-1])
        # 找到最新生成的文件
        file_new = os.path.join(log_dir, lists[-1])
        att3 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename='+file_new+''
        message.attach(att3)

        # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
        smtpObj = smtplib.SMTP_SSL(smtpserver)
        smtpObj.connect(smtpserver,465)
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功！！！")
        smtpObj.quit()


if __name__ == "__main__":
    send = Send_email_fujian()
    send.send_be_report()
