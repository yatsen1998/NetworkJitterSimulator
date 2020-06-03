# -*- coding: utf-8 -*-

import time
import random
import paramiko
import logging
import multiprocessing

hostname = ['172.16.202.14', '172.16.202.15', '172.16.202.16']

port = '22'
username = 'hcd'
password = 'hcd'

delay_ex_cmd = "sudo tc qdisc add dev enp1s0f0 root netem delay 10ms 5ms 5%"
delay_in_cmd = "sudo tc qdisc add dev ib0 root netem delay 10ms 5ms 10%"
loss_ex_cmd = "sudo tc qdisc add dev enp1s0f0 root netem loss 20%"
loss_in_cmd = "sudo tc qdisc add dev ib0 root netem loss 20%"
dup_ex_cmd = "sudo tc qdisc add dev enp1s0f0 root netem duplicate 20%"
dup_in_cmd = "sudo tc qdisc add dev ib0 root netem duplicate 20%"
corrupt_ex_cmd = "sudo tc qdisc add dev enp1s0f0 root netem corrupt 20%"
corrupt_in_cmd = "sudo tc qdisc add dev ib0 root netem corrupt 20%"
scambled_ex_cmd = "sudo tc qdisc add dev enp1s0f0 root netem delay 10ms reorder 20% 20%"
scambled_in_cmd = "sudo tc qdisc add dev ib0 root netem delay 10ms reorder 20% 20%"
clean_ex_cmd = "sudo tc qdisc del dev enp1s0f0 root"
clean_in_cmd = "sudo tc qdisc del dev ib0 root"

class RemoteLink():
    def __init__(self, hostname, port, username, password, interval, timer):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.interval = interval
        self.timer = timer
    
    def Print_time(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                            filename='NetworkJitter.log',
                            filemode='w',
                            level=logging.INFO)
        
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
    def ssh_connect(self):

        ssh = paramiko.SSHClient()   #创建sshclient
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(self.hostname, self.port, self.username, self.password)
        # stdin, stdout, stderr = ssh.exec_command("pwd")
        # print(stdin)
        
        self.Set_Mixed_Jitter(ssh, self.interval, self.timer)
        stdin, stdout, stderr = ssh.exec_command(clean_ex_cmd)
        
        ssh.close()


    def Set_Mixed_Jitter(self, ssh, interval, timer):
        timeout = time.time() + timer
        while 1:
            
            option = random.randint(1,5)
            if option == 1:
                self.Print_time()
                logging.info(self.hostname + " Set Delay Packet" + '\n')
                print(self.hostname + " Set Delay Packet")
                stdin, stdout, stderr = ssh.exec_command(delay_in_cmd)
            
            if option == 2:
                self.Print_time()
                logging.info(self.hostname + " Set Loss Packet" + '\n')
                print(self.hostname + " Set Delay Packet")
                stdin, stdout, stderr = ssh.exec_command(loss_in_cmd)
                
            if option == 3:
                self.Print_time()
                logging.info(self.hostname + " Set Duplicate Packet" + '\n')
                print(self.hostname + " Set Duplicate Packet" + '\n')
                stdin, stdout, stderr = ssh.exec_command(dup_in_cmd)
                
            if option == 4:
                self.Print_time()
                logging.info(self.hostname + " Set Corrupt Packet" + '\n')
                print(self.hostname + " Set Corrupt Packet")
                stdin, stdout, stderr = ssh.exec_command(corrupt_in_cmd)
                
            if option == 5:
                self.Print_time()
                logging.info(self.hostname + " Set Scambled Packet" + '\n')
                print(self.hostname + " Set Scambled Packet")
                stdin, stdout, stderr = ssh.exec_command(scambled_in_cmd)
            
            if time.time() > timeout:
                break
            
            time.sleep(interval)
            stdin, stdout, stderr = ssh.exec_command(clean_ex_cmd)
            time.sleep(interval)     





link=[]
link1=RemoteLink(hostname[0], port, username, password, 60, 600)
link2=RemoteLink(hostname[1], port, username, password, 60, 600)
link3=RemoteLink(hostname[2], port, username, password, 60, 600)

link.append(link1)
link.append(link2)
link.append(link3)


def worker_1():
    link1.ssh_connect()

def worker_2():
    link2.ssh_connect()

def worker_3():
    link3.ssh_connect()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = ())
    p2 = multiprocessing.Process(target = worker_2, args = ())
    p3 = multiprocessing.Process(target = worker_3, args = ())

    p1.start()
    p2.start()
    p3.start()

    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))

