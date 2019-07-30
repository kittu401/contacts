import random
import smtplib
import time
def otp():
    new = int(random.random()*1000000)
    global otpn
    otpn = int(round(new,6))
    sender = "2798ed05237b16"  # enter sender email address
    Password = "54be75888612d5"  # enter sender password
    to_addr = "test@localhost" # enter receiver email adderss
    smtp = smtplib.SMTP('smtp.mailtrap.io',587 ) # enter your smtp address and Port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender,Password)  # will login in to your email account

    subject = "Your OTP For file access "
    body =  "OTP For File access "+str(otpn)+ " Generated at @ " +str(time.ctime())
    msg = f'subject : {subject}\n\n{body}'
    smtp.sendmail(sender,to_addr,msg)
    smtp.quit()
    return int(otpn)