from ftd_connector import ftd_connection
import logging

my_device = {
    "ip": "10.197.241.117",
    "username": "admin",
    "password": "C!sco123"
}

device = ftd_connection(**my_device)

# #  Enabling Logging
logger = logging.getLogger("ftd_connector")
handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

output = device.send_command_clish("show interface ip brief")
print(output)