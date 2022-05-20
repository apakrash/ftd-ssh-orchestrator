import smtplib


#the from account is created for this prupose | change the recv_email accordingly
def sendMail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender_email = 'noreply.ftd@gmail.com'
    recv_email = 'apakrash@cisco.com'
    password = 'C!sco123'
    # Authentication
    s.login(sender_email, password)

    # message to be sent
    message = "sample mail"

    # sending the mail
    s.sendmail(sender_email, recv_email, message)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    sendMail()
