num = int(input("Enter the number!"))
sum = 0 

for digit in str(num):
    sum = sum + int(digit)

print("The sum of its digits: "+str(sum))
