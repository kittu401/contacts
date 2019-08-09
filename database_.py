def Contacts():
# importing required libraries
    import pymysql
    import time
# Creating a Database connection
    db_name = "contacts"
    global table
    table = "user_reg"
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    cursor = db.cursor()

# function which performed Database operations

    print(
          "Press 1for Displaying Data -->\n"
          "Press 2 for entering new Data..\n"
          "press 3 for modifying data in table\n"
          "press 4  for deleting details of contact: ")
    value = int(input())
    if value == 1:
        print("Printing Data :\n")
        cursor.execute("SELECT * FROM (%s)" %(table))
        for row in cursor:
            print(row)
    elif value == 2:
        print("Enter New Values to be entered")
        Id = input("Enter First Name: ")
        Name = input("Enter Last Name: ")
        email = input("Enter Age: ")
        Phone = input("Enter Sex: ")
        # query for adding data into table
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s)', (Id, Name, email, Phone, ))
        db.commit()
        print("Data entered Succesfully")

    elif value == 3:
        field_name = input("enter field name to be updated :")
        new_value = str(input("Please enter your new value"))
        print(new_value,type(new_value))
        reference_name = input("enter reference column name :")
        reference_value = input("enter reference value :")
        print('update '+table + ' set ' + field_name+ ' = '+ new_value+' WHERE '+ reference_name+' = '+ reference_value)
        cursor.execute('update '+table + ' set ' + field_name+ ' = '+ new_value+' WHERE '+ reference_name+' = '+ reference_value)
        db.commit()
        print("data modified succesfully ")

    elif value == 4:
        sno = input("enter employee number to be deleted :")
        reference_name = input("enter reference column name :")
        cursor.execute('DELETE FROM '+table + ' WHERE ' + reference_name + ' = '+sno)
        db.commit()
        print('Data From Row no : ' + sno + ' Deleted Successfully')


Contacts()