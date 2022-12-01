start= int(input("please enter first num: "))
end= int(input("please enter second num: "))
a=[]
while start<end :
    if start%9==0 and start%4!=0 :
        a.append(start)
    start=start+1
print(a)    