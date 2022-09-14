import requests
from requests.auth import HTTPBasicAuth
import time

url = 'https://cxd.cisco.com/home/'
username = 'casenumber'
password = 'token'
auth = HTTPBasicAuth(username, password)
#path = 'C:/Users/apakrash/OneDrive - Cisco/Documents/python/firepower-rest-api/'
filename = 'HDC1-CS.log'

while(1)
    f = open(filename, 'rb')
    r = requests.put(url + filename, f, auth=auth, verify=False)
    r.close()
    f.close()
    print('return code = ',dir(r))
    print(r.status_code)
    time.sleep(10)
