s=input("Enter a string: ")
ans=""
for i in s:
    if i!='z' and i.isalpha():
        ans+=chr(ord(i)+1)

    elif i=='z':
        ans+='a'
print(ans)
