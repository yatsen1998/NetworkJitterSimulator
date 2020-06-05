# -*- coding: utf-8 -*-
import logging

log_format = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d:%(funcName)s(): %(message)s"
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("network_jitter.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
 
logger.addHandler(handler)
logger.addHandler(console)
        
class logInit:
    
    
    def __init__(self):
        self.logger = logging.getLogger()
        
        