# -*- coding: utf-8 -*-
import logging

class logInit:
    log_format = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d:%(funcName)s(): %(message)s"
    
    def __init__():
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                            filename='NetworkJitter.log',
                            filemode='w',
                            level=logging.INFO)
    
    def print_time(self):
        pass
        
        