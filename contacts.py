import re    # importing regular expression library
import os    # importing OS module
file_name = input("enter filename : ")      # Takes file name as input

# creates file path and checks given file name presented or not
x = os.path.isfile('E:\python\python work space\webScraping\db\\'+file_name+'.txt')

# please change file path according to your working directory in your system


def contacts():         # function for adding data to file
    name = input("Enter Name :")
    number = input("Enter Number :")
    f = open('%s.txt' % file_name, 'a')  # opens file on append mode so that data wont get replaced
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
            f = open('%s.txt' % file_name, 'a')
            f.write(name + ' ,' + number )
            f.write("\n")
            print("Contact saved Succesfully")
            f.close()
        else:
            break


def search():               # function for checking wether given input present in that file or not
    search_name = input("Enter name to be searched :")
    f = open('%s.txt' % file_name)
    for line in f:
        if re.search(search_name, line):
            print(line, end=' ')