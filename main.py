def fact(n):
    if n==0:
        return 1 
    else: 
        return n*fact(n-1)
n=int(input("Enter Number: "))
if n<0:
    print("Please Enter A Valid Number")
else:
    print("Factorial Of Given Number Is: ", fact(n))