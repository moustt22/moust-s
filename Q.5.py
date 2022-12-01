name= (input("please enter the name: "))
txt= name[::-1]
if name == txt:
    print("this is palindrome")
else:
    print("not palindrome: "+ txt)