x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))
if x + y == z :
    print(x,"+",y,"=",z)
elif x - y == z:
    print(x,"-",y,"=",z)
elif y - x == z:
    print(y,"-",x,"=",z)
elif x * y == z:
    print(x,"*",y,"=",z)
elif x ** y == z:
    print(x,"**",y,"=",z)
elif y ** x == z:
    print(y,"**",x,"=",z)
elif x / y == z:
    print(x,"/",y,"=",z)
elif y / x == z:
    print(y,"/",x,"=",z)
elif x % y == z:
    print(x,"%",y,"=",z)
elif y % x == z:
    print(y,"%",x,"=",z)
else:
    print("No opearators available")