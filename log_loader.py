# -*- coding: utf-8 -*-
import logging
import os.path
import time

        
class logInit(object):
    
    
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        
        
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # another handler to print to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # define format
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d:%(funcName)s(): %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
 
    def getlog(self):
         return self.logger
        