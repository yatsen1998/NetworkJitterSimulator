# -*- coding: utf-8 -*-
import logging

class logInit:
    def __init__():
        
    
    def print_time(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                            filename='NetworkJitter.log',
                            filemode='w',
                            level=logging.INFO)
        
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),'')