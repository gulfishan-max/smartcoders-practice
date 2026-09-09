n=int(input("enter the number:"))
k=int(input("enter the position:"))
if n&(1<<k):
    print("the bit is set")
else:
    print("the bit is  not a set")    