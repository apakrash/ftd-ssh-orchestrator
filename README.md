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

# Troubeshooting/FAQ

1. The script is not doing anything, the code seems stuck

make sure that the following is edited in the code for the cluster that you are testing with in ssh-cluster.py
```
my_device = {
"ip": "10.0.0.1",
"username": "admin",
"password": "C1sco12345"
}
```
2. Still not working, what else can I check

Try to ssh to the cluster ip using the credentials defined above, see if the clish prompt opens.

3. How to verify the history/result of past attempts of running the code.

In the same folder there is a log file called app.log, please check that or checking the exact output being recorded:

```
tail -f app.log
```

# Still Need Support?

If still a problem persists, please raise an issue in the issues section(without mentioning credentials/ip since this is a public forum): https://github.com/apakrash/ftd-cluster-check/issues








