#!/usr/bin/env python3
# -*-coding: utf-8 -*-

'''
日志：
    1、创建日志记录器logger = logging.getLogger(logger_name)
    2、设置日志记录器的级别 logger.setLevel(logging.INFO)
    3、创建日志处理器 handler = logging.handlers.StreamHandler()
    4、设置日志处理器的级别handler.setLevel(logging.DEBUG)
    5、将日志处理器添加到日志记录器上logger.addHandler(handler)
    6、创建过滤器
    7、将过滤器添加到日志处理器上
    8、将过滤器添加到日志记录器上
'''

import os
import logging
import logging.handlers
import datetime
from TestDemo.config.config import LOG_PATH,CONFIG_FILE
from TestDemo.tool.fileRead import ReadYaml

config = ReadYaml(CONFIG_FILE).getDatas("log")

class Logger(object):

    def __init__(self):

        # 创建一个日志记录器，命名为myLogger
        self.logger = logging.getLogger(config['name'])

        # 将名为root的跟记录器的日志级别设置为NOTSET
        logging.root.setLevel(logging.NOTSET)

        # log存放的名字
        self.log_file_name = config['log_file_name']

        # 备份计数
        self.backup_count = config['backup_count']

        # 日志输出级别
        self.console_output_level = config['console_output_level']
        self.file_output_level = config['file_output_level']

        # 日志输出格式
        self.formatter = logging.Formatter(config['formatter'])
    
    def get_logger(self):

        # 使用if语句判断，避免重复日志
        if not self.logger.handlers:

            # 将日志消息发送到输出到Stream
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=os.path.join(LOG_PATH, self.log_file_name),
                when='D',
                interval=1,
                backupCount=self.backup_count,
                delay=True,
                encoding='utf-8'
            )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
def myLog(func):
    def warpper(*args):
        logger.info("hehe")
        return func
    return warpper

@myLog
def a():
    print("hehe")

a()