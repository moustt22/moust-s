def fibonacci (size):
    first=1
    second=1
    i=0
    while i<size :
        print(first)
        first, second = second, second+ first
        i=i+1

n=int(input("Enter the size"))
fibonacci(n)