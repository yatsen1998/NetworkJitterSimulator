# -*- coding: utf-8 -*-
import os
import sys
import json


class ReadConfig:
    def __init__(self, filename):
        self.configPath = filename
        self.clusterId = None
        self.hosts = None
        self.port = None
        self.username = None
        self.password = None
        self.interval = None
        self.elapseTime = None
        self.NICInfo = None

    def parse(self):
        """
        Parse config file to get cluster information
        
        """
        if os.path.exists(self.configPath):
            # print(self.configPath)
            json_data = json.load(open(self.configPath, 'r'))
        else:
            sys.exit("ERROR: Cannot find config file!")

        self.clusterId = json_data['clusterId']
        self.hosts = json_data['hosts']
        self.port = json_data['port']
        self.username = json_data['username']
        self.password = json_data['password']
        self.interval = json_data['interval']
        self.elapseTime = json_data['elapse_time']
        self.NICInfo = json_data['NICInfo']
