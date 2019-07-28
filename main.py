# importing functions from contacts file
import os
from Contacts.contacts import contacts,search
from Contacts.contacts import file_name
from Contacts.mail_test import send_mail

x = os.path.isfile('E:\python\python work space\webScraping\Contacts\\'+file_name+'.txt')

# please change file path according to your working directory in your system

if x is True:
    contacts()
    send_mail()
    search()

elif x is False:
    contacts()
    search()

# reference link
'''https://stackoverflow.com/questions/21839803/how-to-append-new-data-onto-a-new-line'''