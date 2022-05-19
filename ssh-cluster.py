'''
This code in intended to SSH to the FTD every 10 min and check the counter seen in the output of cluster exec sh asp drop | i cluster-forward-error.
If the counter is seen to increase more than 10, then an email is sent to the admin to take corrective action

'''


from ftd_connector import ftd_connection
import logging
import time
import smtplib
from pythonGmail import *

#change the ip address and credentials accordingly
my_device = {
    "ip": "10.197.241.117",
    "username": "admin",
    "password": "C!sco123"
}

sleeptime = 600 # in seconds

device = ftd_connection(**my_device)

# #  Enabling Logging
logger = logging.getLogger("ftd_connector")
handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

#output = device.send_command_clish("cluster exec  show  asp  drop | include  cluster-forward-error")
#output = device.send_command_clish("cluster exec show asp drop | include cluster-forward-error")
#print(output)

firstTry = 1
while(1):
    counter = 0
    output = device.send_command_clish("cluster exec sh asp drop | i cluster-forward-error")
    outputLines = output.splitlines()
    for line in outputLines:
        if 'Cluster member failed to send data packet over CCL (cluster-forward-error)' in line:
            counter = int(line.split('Cluster member failed to send data packet over CCL (cluster-forward-error)')[1].strip())
            break
    
    if firstTry == 1:
        counterLastIteration = counter
        firstTry = 0
        time.sleep(sleeptime)
        print(counter)
    else:
        print('counter = ' + str(counter))
        print('counterLastIteration = ' + str(counterLastIteration))
        if counter - counterLastIteration > 10:
            print('counter more than 10, sending email')
            sendMail()
        counterLastIteration = counter
        time.sleep(sleeptime)
    print('--------------------------------------------')
