def core():
    import os
    from Contacts.contacts import contacts
    from Contacts.Search import search
    from Contacts.email_sender import send_mail
    file_name = input("Enter File Name :")
    x = os.path.isfile('E:\python\python work space\webScraping\Contacts\\'+file_name+'.txt')
    # please change file path according to your working directory in your system
    if x is True:
        contacts(file_name)
        send_mail()
        search(file_name)

    elif x is False:
        contacts(file_name)
        search(file_name)

# reference link
'''https://stackoverflow.com/questions/21839803/how-to-append-new-data-onto-a-new-line'''