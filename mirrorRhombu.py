n= int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    for k in range(i):
        print(" ",end="")

    print()