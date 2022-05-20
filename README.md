This code is based on the repo: https://github.com/Viss/toolkit/blob/master/cisco-ssh.py

# Requirement:
- Python 3.x
- Paramiko >= 2.4.2

To install paramiko
```pip install paramiko```

# Download the Zip of the repository and extract it
https://github.com/apakrash/ftd-cluster-check/archive/refs/heads/main.zip

# Changes needed prior to running the script

### in file: ssh-cluster.py: define the ip address and the credentials:
```
my_device = {
    "ip": "10.0.0.1",
    "username": "admin",
    "password": "C1sco12345"
}
```
### in file: pythonGmail.py: define the email address of the intended recipient in the list differenciated by comma: 

```
recv_email = ['apakrashi@cisco.com']
```


#### To run the script

```
python3 ssh-cluster.py &
```
Please note the '&' at the end to make the script run in background.
