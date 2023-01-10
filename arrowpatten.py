n= int(input())
for  i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(n): 
        print("*",end="")
    print()       

    #Rhombus stare patten5

for  i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n): 
        print("*",end="")
    print()       