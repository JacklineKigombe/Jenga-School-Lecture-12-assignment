def search_name_1():
    infile = open("names.txt","r")

    letter = input("Enter a letter: ")
    letter = letter.upper()

    found = False

    for s in infile:
        line = s.strip()

        if line[0] == letter:
            print(line)
            found = True
    
    if not found:
        print(f"No person with name starting with letter {letter} found")
    
    infile.close()

# user can search with a longer string
def search_name_2():
    infile = open("names.txt","r")

    # get user input and convert to title case
    letters = input("Enter first few letters of a name: ").title()

    found = False

    count = len(letters)

    for s in infile:
        line = s.strip()
        if line[:count] == letters:
            print(line)
            found = True
    
    if not found:
        print(f"No person with name starting with {letters} found")
    
    infile.close()
    

search_name_1()
search_name_2()
