def search_name():
    infile = open("names.txt","r")

    for s in infile:
        # remove leading and trailing spaces and newlines
        line = s.strip()
        if line[0] == 'A':
            print(line)
    
    infile.close()


search_name()
