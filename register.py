

def user_reg():

    import pymysql
    db_name = "contacts"
    table = "user_reg"
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    print("Conntcted to "+ table)
    cursor = db.cursor()
    Name = str(input("Enter  Name: "))
    Name = Name.lower()
    Email = str(input("Enter Email : "))
    Email = Email.lower()
    Password = str(input("Enter Password: "))
    Password = Password.lower()
    cursor.execute('SELECT * FROM ' + table + ' WHERE Email = "%s" AND Password = "%s"' % (Email, Password))
    db.commit()
    x = cursor.rowcount
    if x > 0:
        for row in cursor:
            email = str(row[2]).lower()
            if email == Email:
                print("Email Already registered")
                user_reg()
    elif x <= 0:
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s)', (" ", Name, Email, Password))
        db.commit()
        print("Hello " + Name + " You've Registered successfully")


