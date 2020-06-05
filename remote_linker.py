# -*- coding: utf-8 -*-
#import logging
import paramiko

from config_reader import readConfig

cluster_info = readConfig('config.json')
cluster_info.parse()

class remoteLink:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        
    def ssh_loader(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(self.hostname, self.port, self.username, self.password)
        print("SSH to "+ self.hostname)
        
        return ssh
        