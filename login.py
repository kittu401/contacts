def login():
    import pymysql
    db_name = "contacts"
    table = "user_reg"
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    user_email = str(input("Enter your email: "))
    user_email = user_email.lower()
    user_password = str(input("Enter your password : "))
    user_password = user_password.lower()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ' + table + ' WHERE Email = "%s" AND Password = "%s"' %(user_email,user_password))
    db.commit()
    x = cursor.rowcount
    if x > 0:
        for row in cursor:
            email = str(row[2]).lower()
            password = str(row[3]).lower()
            if email == user_email and password == user_password:

                print("Hello " + row[1])
                break
    else :
        print("Enter Valid Credentials")
        login()
