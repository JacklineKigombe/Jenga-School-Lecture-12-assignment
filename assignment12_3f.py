def search_name():
    # prompt user for a name and convert only the first letter to upper case others letters to lowercase
    name = input("Enter a name: ").title()

    if not name.isalpha():
        print("Invalid entry.Name cannot be a number")
        return
    
    # read input file
    infile = open("names.txt","r")

    # for checking if a name is found
    found = False

    count = len(name)

    for s in infile:
        # remove leading and trailing spaces and newlines
        line = s.strip()

        # get the first column
        first_name = line.split(' ')[0]

        if first_name[:count] == name:
            print(line)
            found = True
    
    if not found:
        print(f"{name} not found")
    

    infile.close()

def search_age():
    # prompts user for an age
    age = int(input("Enter an age: "))

    infile = open("names.txt","r")

    # for checking if age is found
    found = False

    for s in infile:
        # remove leading and trailing spaces and newlines
        line = s.strip()

        # get second column
        str_age = line.split(' ')[1]

        if int(str_age) == age:
            print(line)
            found = True
    
    if not found:
        print(f"No person of age {age} found")
    

    infile.close()

def main():
    print("Choose a search option - either 1 or 2")
    print("1: Search with name")
    print("2: Search with age")
    # prompts user for an option
    try:
        option = int(input("Enter option 1 or 2: "))

        if option not in [1,2]:
            raise ValueError
        
        if option == 1:
            search_name()
        else:
            search_age()
    except ValueError:
        print("Invalid entry.Enter a valid number")


main()
