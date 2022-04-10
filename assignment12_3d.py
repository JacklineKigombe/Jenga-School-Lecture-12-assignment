def search_age():
    infile = open("names.txt","r")
    found = False

    for s in infile:
        # remove leading and trailing spaces and newlines
        line = s.strip()

        # get second column
        str_age = line.split(' ')[1]
        
        if str_age == '5':
            print(line)
            found = True
    
    if not found:
        print(f"No person of age 5 found")
    
    infile.close()


search_age()
