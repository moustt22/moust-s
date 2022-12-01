n=[]
i=0
while i<50 :
    x=input("Enter next item: ")
    n.append(x)
    i=i+1
for i in range(1,50,2):
    n[i],n[i-1]=n[i-1],n[i]
print(n)