def search(name2):
    import re# function for checking wether given input present in that file or not
    search_name = input("Enter name to be searched :")
    f = open('%s.txt' % name2)
    for line in f:
        if re.search(search_name, line):
            print(line, end=' ')