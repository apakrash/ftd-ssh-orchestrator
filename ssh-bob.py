'''
This code in intended to SSH to the FTD every 10 min and check the counter seen in the output of cluster exec show asp drop | i cluster-forward-error.
If the counter is seen to increase more than 10, then an email is sent to the admin to take corrective action

'''


from ftd_connector import ftd_connection
import logging
import time
import smtplib
from pythonGmail import *
from pprint import pprint

#change the ip address and credentials accordingly
my_device = {
    "ip": "10.197.225.191",
    "username": "admin",
    "password": "C!sco123"
}

sleeptime = 10 # in seconds

device = ftd_connection(**my_device)

# #  Enabling Logging
logger = logging.getLogger("ftd_connector")
handler = logging.FileHandler('bob.log')
formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

#output = device.send_command_clish("cluster exec  show  asp  drop | include  cluster-forward-error")
#output = device.send_command_clish("cluster exec show asp drop | include cluster-forward-error")
#print(output)

f = open("commands-to-monitor-bob.txt", "r")
commandList = f.readlines()
pprint(commandList)

firstTry = 1
while(1):
    counter = 0
    #output = device.send_command_clish("show cluster info")
    #output = device.send_command_clish("show cluster info conn-distribution")
    for command in commandList:
        #output = device.send_command_clish(command)
        output = device.send_command_expert(command)
        print(output)
        time.sleep(1)
    time.sleep(sleeptime)
    print('--------------------------------------------')
