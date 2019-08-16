def Contacts(id_num,name):
# importing required libraries
    import pymysql
    import time
# Creating a Database connection
    db_name = "contacts"
    table = "contacts"
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    cursor = db.cursor()

# function which performed Database operations

    print(
          "Press 1 for Displaying Data -->\n"
          "Press 2 for entering new Data..\n"
          "press 3 for modifying data in table\n"
          "press 4  for deleting details of contact: ")
    value = int(input())
    if value == 1:

        print("Displaying your contacts :\n")
        cursor.execute("SELECT * FROM (%s) Where Ref_id = (%s)" %(table,id_num))
        for row in cursor:
            print(row[0] + " "+ row[1])
    elif value == 2:
        print("Enter New contact details :")

        n_name = str(input("Enter Name : "))
        phone = str(input("Enter Number : "))
        r_id = id_num
        r_name = name

        # query for adding data into table
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s)', (n_name,phone,r_id,r_name ))
        db.commit()
        print("Contact Saved")
        while(True):
            choice = str(input("Do you want add more ..? \n"
                           "1 For yes :\n"
                           "2 For no :"))
            if choice == "yes":
                n_name = str(input("Enter Name : "))
                phone = str(input("Enter Number : "))
                r_id = id_num
                r_name = name

                # query for adding data into table
                cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s)', (n_name, phone, r_id, r_name))
                db.commit()
                print("Contact Saved")
            else:
                break

    elif value == 3:

        new_num = str(input("Please enter your new number :"))
        reference_id = input("enter ref id :")
        cursor.execute('update '+table + ' set Number = '+ new_num+' WHERE Id = '+ reference_id)
        db.commit()
        print("data modified succesfully ")
        while (True):  # never ending loop until you select option no 2
            choice = str(input("Do you want to edit more ..? \n"
                               "1 For yes :\n"
                               "2 For no :"))
            if choice == "yes":
                f_name = input("enter contact name to be updated :")
                new_num = str(input("Please enter your new number :"))
                reference_id = input("enter ref id :")
                cursor.execute('update '+table + ' set Number = '+ new_num+' WHERE Id = '+ reference_id)
                db.commit()
                print("data modified succesfully ")
            else:
                break

    elif value == 4:
        num = input("enter employee number to be deleted :")
        cursor.execute('DELETE FROM '+table + ' WHERE Number = '+num)
        db.commit()
        print('Number Deleted ')
        while (True):  # never ending loop until you select option no 2
            choice = str(input("Do you want to delete more ..? \n"
                               "1 For yes :\n"
                               "2 For no :"))
            if choice == "yes":
                num = input("enter employee number to be deleted :")
                cursor.execute('DELETE FROM ' + table + ' WHERE Number = ' + num)
                db.commit()
                print('Number Deleted ')
            else:
                break