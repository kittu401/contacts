def send_mail():
    import smtplib
    sender = " "  # enter sender email address
    Password = " "  # enter sender password
    to_addr = " " # enter receiver email adderss
    smtp = smtplib.SMTP(# smptaddress ,#port number ) # enter your smtp address and Port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender,password=Password)  # will login in to your email account

    subject = # give your email subject
    body =  # enter your message body
    msg = f'subject : {subject}\n\n{body}'
    smtp.sendmail(sender,to_addr,msg)
    print("mail sent")
    smtp.quit()