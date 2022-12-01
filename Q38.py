strng = input("Enter a string!")
def count(subject):
    digit = 0
    letter = 0
    for chr in subject:
        if chr.isdigit():
            digit = digit + 1
        elif chr.isalpha():
            letter = letter + 1
        else:
            pass
    print ("The number of letters is:",letter)
    print ("The number of digits is:", digit)

count(strng)


