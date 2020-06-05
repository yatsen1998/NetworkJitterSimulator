# -*- coding: utf-8 -*-

import time
import random

from config_reader import readConfig
from remote_linker import remoteLink
#from log_loader import logInit
         
cluster_info = readConfig('config.json')
cluster_info.parse()

linker = remoteLink(cluster_info.hosts[0],
                    cluster_info.port, 
                    cluster_info.userName,
                    cluster_info.passWord)
ssh = linker.ssh_loader()


class TestJudge:
    """
        Judge whether the test passes
        HCLI base on python2.7 ?
    """
    pass

class networkJitter:
    
    #创建sshclient
    
    def __init__(self, ssh, hostname, interval, elapse_time, ex_NIC, in_NIC):
        self.ssh = ssh
        self.hostname = hostname
        self.interval = interval
        self.elapse_time = elapse_time
        self.ex_NIC = ex_NIC
        self.in_NIC = in_NIC    

    def test_set_delay_ex(self,ssh):
        """
            Testcase1: set delayed packet to external NIC

        """
        # self.print_time()
        #logging.info(self.hostname + " Set Delay Packet" + '\n')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(self.hostname + " Set Delay Packet to "+ self.ex_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.ex_NIC +
                                                 " root netem delay 10ms 5ms 5%")
    
    def test_set_delay_in(self,ssh):
        """
            Testcase2: set delayed packet to internal NIC

        """
        print(self.hostname + " Set Delay Packet to "+ self.in_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.in_NIC +
                                                 " root netem delay 10ms 5ms 5%")
    
    def test_set_loss_ex(self,ssh):
        """
            Testcase3: set packet loss to external NIC

        """
        print(self.hostname + " Set Packet Loss to "+ self.ex_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.ex_NIC +
                                                 " root netem loss 20%")

    def test_set_loss_in(self,ssh):
        """
            Testcase4: set packet loss to internal NIC

        """
        print(self.hostname + " Set Packet Loss to "+ self.in_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.in_NIC +
                                                 " root netem loss 20%")
    
    def test_set_dup_ex(self,ssh):
        """
            Testcase5: set duplicate packet to external NIC

        """        
        print(self.hostname + " Set Duplicate Packet to "+ self.ex_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.ex_NIC +
                                                 " root netem duplicate 20%")
    
    def test_set_dup_in(self,ssh):
        """
            Testcase6: set duplicate packet to internal NIC

        """
        print(self.hostname + " Set Duplicate Packet to "+ self.in_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.in_NIC +
                                                 " root netem duplicate 20%")
    
    def test_set_corrupt_ex(self,ssh):
        """
            Testcase7: set corrupt packet to external NIC

        """
        print(self.hostname + " Set Corrupt Packet to "+ self.ex_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.ex_NIC +
                                                 " root netem corrupt 20%")
    
    def test_set_corrupt_in(self,ssh):
        """
            Testcase8: set corrupt packet to internal NIC

        """
        print(self.hostname + " Set Corrupt Packet to "+ self.in_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.in_NIC +
                                                 " root netem corrupt 20%")
    
    def test_set_scrambled_ex(self,ssh):
        """
            Testcase9: set scrambled packet to external NIC

        """
        print(self.hostname + " Set Scrambled Packet to "+ self.ex_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.ex_NIC +
                                                 " root netem delay 10 reorder 20% 20%")
    
    def test_set_scrambled_in(self,ssh):
        """
            Testcase10: set scrambled packet to internal NIC

        """       
        print(self.hostname + " Set Scrambled Packet to "+ self.in_NIC)
        
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc add dev " + 
                                                 self.in_NIC +
                                                 " root netem delay 10 reorder 20% 20%")
    
    def clean_ex(self,ssh):
        """
            Clean rules set to external NIC

        """
        #print(self.hostname + " Clean command "+ self.ex_NIC)
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc del dev " + 
                                                 self.ex_NIC + " root")
    
    def clean_in(self,ssh):
        """
            Clean Rules set to internal NIC

        """
        #print(self.hostname + " Clean command "+ self.in_NIC)
        stdin, stdout, stderr = ssh.exec_command("sudo tc qdisc del dev " + 
                                                 self.in_NIC + " root")
        

    def test_set_mixed_jitter(self, ssh, interval, elapse_time):
        """
            Testcase11: set a network condition to certain NIC
            
        """
        timeout = time.time() + elapse_time
        Rule_map = ["test_set_delay_ex","test_set_delay_in",
                    "test_set_loss_ex","test_set_loss_in",
                    "test_set_dup_ex","test_set_dup_in",
                    "test_set_corrupt_ex","test_set_corrupt_in",
                    "test_set_scrambled_ex","test_set_scrambled_in"]
        while 1:
            eval("self."+random.choice(Rule_map))(ssh)
            
            if time.time() > timeout:
                break
            
            time.sleep(interval)
            self.clean_ex(ssh)
            self.clean_in(ssh)
            time.sleep(interval)     

    def run(self):
        while 1:
            self.test_set_mixed_jitter(self.ssh, self.interval, self.elapse_time)
            
        self.clean_ex(ssh)
        self.clean_in(ssh)
    
        self.ssh.ssh_close(ssh)

jitter=networkJitter(
                ssh,
                cluster_info.hosts[0],
                cluster_info.interval, 
                cluster_info.elapseTime,
                cluster_info.NICInfo['external_NIC'],
                cluster_info.NICInfo['internal_NIC'])

jitter.run()
