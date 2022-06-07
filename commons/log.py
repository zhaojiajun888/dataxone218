#coding=UTF-8
# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import logging

class Logger(object):

    def __init__(self):
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        # 指定日志路径
        self.log_file_name = '/dataxone218/logs/test.log'
        # 日志输出
        self.console_output_level = 'INFO'
        self.file_output_level = 'INFO'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s ')
    def get_logger(self):
        """封装logger"""
        if not self.logger.handlers:#避免重复日志
            # logging.StreamHandler()  控制台输出
            console_handler = logging.StreamHandler()
            # 指明最终输出中日志记录的布局（为处理器选择一个格式化器）
            console_handler.setFormatter(self.formatter)
            # 指定logger将会处理的最低的安全等级日志信息
            console_handler.setLevel(self.console_output_level)
            # 从记录器对象中添加处理程序对象
            self.logger.addHandler(console_handler)

            # 清空日志文件
            with open(self.log_file_name,"r+") as file:
                file.truncate(0)
            # logging.FileHandler()  向文件输出日志信息
            file_handler = logging.FileHandler(self.log_file_name)
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            return self.logger

loggers = Logger().get_logger()


