# -*- coding: utf-8 -*-
import logging
import os.path
import time

        
class logInit(object):
    
    
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        
        
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getsmd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d:%(funcName)s(): %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
 
     def getlog(self):
         return self.logger
        