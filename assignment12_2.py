def main():
    rep = {1:[],2:[],3:[],4:[],5:[]}

    for num in range(1,101):
        # numbers divisible by 7 and 3
        if num%7 == 0 and num%3 == 0:
            rep[1].append(num)
        
        # numbers divisible by 7 but not 3
        if num%7 == 0 and num%3 != 0:
            rep[2].append(num)
        
        # ODD numbers divisible by 7 but not 3
        if num%2 != 0 and num%7 == 0 and num%3 != 0:
            rep[3].append(num)
        
        # numbers divisible by the sum of its digits
        digit_total = 0
        for digit in str(num):
            digit_total += int(digit)
    
        if num%digit_total == 0:
            rep[4].append(num)
        
        # numbers equal to the square of the sum of its digits
        if num == digit_total**2:
            rep[5].append(num)

    print(f"Numbers that are divisible by 7 and 3: {rep[1]}")
    print(f"Numbers that are divisible by 7 but not 3: {rep[2]}")
    print(f"ODD numbers divisible by 7 but not 3: {rep[3]}")
    print(f"Numbers that are divisible by the sum of its digits: {rep[4]}")
    print(f"Numbers that are equal to the square of the sum of its digits: {rep[5]}")


main()
