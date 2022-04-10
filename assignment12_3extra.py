def search_age(comparator):
    # prompts user for an age
    age = int(input("Enter an age: "))
    infile = open("names.txt","r")

    # for checking if age is found
    found = False

    for s in infile:
        # remove \n from the str and get the second column
        line = s.strip()
        str_age = line.split(' ')[1]

        if comparator(int(str_age),age):
            print(line)
            found = True
    
    if not found:
        print(f"No person found")

def main():
    print("Choose a search option")
    print("1: Find the ones that are equal to the given age")
    print("2: Find the ones that are equal or greater than the given age")
    print("3: Find the ones that are equal or less than the given age")
    # prompts user for an option
    try:
        option = int(input("Enter option 1, 2 or 3: "))

        if option not in [1,2,3]:
            raise ValueError
        
        if option == 1:
            search_age(lambda a,b:a == b)
        elif option == 2:
            search_age(lambda a,b:a >= b)
        else:
            search_age(lambda a,b:a <= b)
    except ValueError:
        print("Invalid entry.Enter a valid number")


main()
