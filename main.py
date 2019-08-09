# importing functions from contacts file

from Contacts.login import login
from Contacts.register import user_reg

print("*"*5 + "  WELCOME  " + "*"*5)
choice = int(input("New user ? enter 1 \n"
      "Existing User enter 2: "))
if choice == 1:
    user_reg()
    login()
elif choice == 2:
    login()
