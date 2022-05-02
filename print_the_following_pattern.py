n=int(input())
for i in range(n,0,-1):
    for j in range(0,i-1,1):
        print(" ",end="")
    for k in range(1,n+1,1):
        if(k==1 or k==n or i==1 or i==n):
            print("*",end="")
        else:
            print(" ",end="")
    print()