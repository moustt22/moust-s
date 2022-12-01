num = int(input("Enter the number!"))
sum = 0 
for digit in str(num):
    sum = sum + int(digit)**3

if num == sum:
    print("This is an Armstrong number!")
else:
    print("This is not an Armstrong number")
