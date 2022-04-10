def search_age():
    try:
        infile = open("names.txt","r")

        age = int(input("Enter an age number: "))
        found = False

        for s in infile:
            # remove leading and trailing spaces and newlines
            line = s.strip()

            # second column
            str_age = line.split(' ')[1]
            
            if int(str_age) == age:
                print(line)
                found = True
        
        if not found:
            print(f"No person of age {age} found")
    
        infile.close()
    except ValueError:
        print("Invalid entry.Please enter a valid age number: ")
    except FileNotFoundError:
        print("File not found")

search_age()
