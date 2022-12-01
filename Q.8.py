n=int(input("Enter number of elements: "))
l=[]
for i in range(0,n):
    x=input("Enter next item: ")
    l.append(x)
target=int(input("enter the pos of the element you want to erase: "))
l.remove(l[target-1])
print(l)
