#Open a new Python program file. Define a function named searchname(). In this function, open 
#the file “names.txt” and print its contents using a loop. 
#Which one do you think is better? Why?
#first implementation is better - search_name_1() - because it doesn't remove the last character from the last line.
def search_name_1():
    infile = open("names.txt","r")
    for s in infile:
        print(s)

# prints each line while removing the last character from each line i.e '/n' from 1st to 2nd last line
# but removes age from last line because it does not have a newline character
def search_name_2():
    infile = open("names.txt","r")
    for s in infile:
        print(s[:-1])

search_name_1()
search_name_2()
