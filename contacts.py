def contacts(name1):         # function for adding data to file
    name = input("Enter Name :")
    number = input("Enter Number :")
    f = open('%s.txt' % name1, 'a')  # opens file on append mode so that data wont get replaced
    f.write(name + ' ,' + number)
    f.write("\n")       # writes data into next line
    print("Contact saved Succesfully")
    f.close()
    while (True):       # never ending loop until you select option no 2
        choice = int(input("Do you want more ..? \n"
                           "1 For yes :\n"
                           "2 For no :"))
        if choice == 1:
            name = input("Enter Name :")
            number = input("Enter Number :")
            f = open('%s.txt' % name1, 'a')
            f.write(name + ' ,' + number )
            f.write("\n")
            print("Contact saved Succesfully")
            f.close()
        else:
            break
    