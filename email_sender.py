def send_mail():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import time
    login = "2798ed05237b16"  # enter sender email address
    Password = "54be75888612d5"  # enter sender password
    to_addr = "venkat-729628@inbox.mailtrap.io" # enter receiver email adderss
    smtp = smtplib.SMTP('smtp.mailtrap.io',587 ) # enter your smtp address and Port number

    sender_email = "mailtrap@example.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = to_addr


    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(login,Password)  # will login in to your email account

    subject = "Warning alert Changes made"
    body =  "Changes made  to your file @ " +str(time.ctime())
    msg = f'subject : {subject}\n\n{body}'
    smtp.sendmail(sender_email,to_addr,msg)
    print("mail sent")
    smtp.quit()
