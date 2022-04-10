a = 2
b = 3
c = 123

if a > b:
    print("It can't be! ")
else:
    print("Here we go. ")

if c%b == 0:
    a = 4

if c == a*b:
    print("Where are we? ")
else:
    print("Are we there yet? ")

if c >= a*b:
    if a > b:
        print("Close to the end. ")
    elif a == b:
        print("All equal! ")
    else:
        print("Same order. ")
elif c > a:
    if a != b:
        print("Back to start ")
    else:
        print("What did we do now? ")
