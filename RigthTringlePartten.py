n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")    
    print()
     #another way is
for i in range(n):
    print(" "*(n-i-1),end="")
    print ("*"*(i+1))
    